import AppKit
import Foundation
import Darwin

private let toolsDirectory = URL(fileURLWithPath: "/Users/simonhinterreiter/Applications/SC4 Plop and Paint Tools", isDirectory: true)
private let gameDirectory = "/Users/simonhinterreiter/Applications/SimCity 4 Windows.app/Contents/SharedSupport/prefix/drive_c/GOG Games/SimCity 4 Deluxe Edition"
private let pluginsDirectory = "/Users/simonhinterreiter/Documents/SimCity 4 Windows/Plugins"
private let logURL = URL(fileURLWithPath: "/Users/simonhinterreiter/Documents/SimCity 4 Windows/Setup logs/Plop and Paint cache rebuild.log")
private let lockURL = toolsDirectory.appendingPathComponent(".cache-rebuild.lock", isDirectory: true)

private enum HelperError: LocalizedError {
    case gameOpen
    case alreadyRunning
    case missingBuilder
    case processCheckFailed

    var errorDescription: String? {
        switch self {
        case .gameOpen:
            return "SimCity 4 is still running. Quit the game, then click Rebuild again."
        case .alreadyRunning:
            return "A rebuild is already running, or an earlier rebuild did not close normally. Wait for it to finish. If no rebuild is running, the helper’s lock folder needs to be removed."
        case .missingBuilder:
            return "The content builder is missing or cannot run. Its expected location is shown below."
        case .processCheckFailed:
            return "The helper could not check whether SimCity 4 is running. Nothing was rebuilt."
        }
    }
}

private func checkGameClosed() throws {
    let process = Process()
    let output = Pipe()
    process.executableURL = URL(fileURLWithPath: "/bin/ps")
    process.arguments = ["-axo", "command="]
    process.standardOutput = output
    process.standardError = FileHandle.nullDevice
    try process.run()
    let data = output.fileHandleForReading.readDataToEndOfFile()
    process.waitUntilExit()
    guard process.terminationStatus == 0 else { throw HelperError.processCheckFailed }
    let commands = String(decoding: data, as: UTF8.self)
    if commands.components(separatedBy: .newlines).contains(where: { $0.contains("preloader SimCity 4.exe") }) {
        throw HelperError.gameOpen
    }
}

final class AppDelegate: NSObject, NSApplicationDelegate, NSWindowDelegate {
    private var window: NSWindow!
    private var rebuildButton: NSButton!
    private var closeButton: NSButton!
    private var spinner: NSProgressIndicator!
    private var statusLabel: NSTextField!
    private var outputView: NSTextView!
    private var busy = false
    private var displayedOutput = ""

    func applicationDidFinishLaunching(_ notification: Notification) {
        installMenu()
        window = NSWindow(contentRect: NSRect(x: 0, y: 0, width: 650, height: 430),
                          styleMask: [.titled, .closable, .miniaturizable], backing: .buffered, defer: false)
        window.title = "Rebuild SimCity Content"
        window.delegate = self
        window.isReleasedWhenClosed = false
        window.center()

        let content = window.contentView!
        let title = NSTextField(labelWithString: "Refresh Plop and Paint’s content list")
        title.font = .systemFont(ofSize: 20, weight: .semibold)
        title.frame = NSRect(x: 24, y: 377, width: 602, height: 28)
        content.addSubview(title)

        let explanation = NSTextField(wrappingLabelWithString: "After adding or removing mods, quit SimCity 4 and click Rebuild.\nThis refreshes the searchable list and small preview pictures. It may take several minutes. Keep the game closed until it finishes.")
        explanation.font = .systemFont(ofSize: 13)
        explanation.frame = NSRect(x: 24, y: 297, width: 602, height: 69)
        content.addSubview(explanation)

        spinner = NSProgressIndicator(frame: NSRect(x: 24, y: 263, width: 18, height: 18))
        spinner.style = .spinning
        spinner.controlSize = .small
        spinner.isDisplayedWhenStopped = false
        content.addSubview(spinner)

        statusLabel = NSTextField(wrappingLabelWithString: "Ready. Your saved cities are not changed by rebuilding.")
        statusLabel.font = .systemFont(ofSize: 13, weight: .medium)
        statusLabel.frame = NSRect(x: 50, y: 243, width: 576, height: 42)
        content.addSubview(statusLabel)

        let scroll = NSScrollView(frame: NSRect(x: 24, y: 81, width: 602, height: 157))
        scroll.borderType = .bezelBorder
        scroll.hasVerticalScroller = true
        scroll.autohidesScrollers = true
        outputView = NSTextView(frame: scroll.bounds)
        outputView.isEditable = false
        outputView.isSelectable = true
        outputView.font = .systemFont(ofSize: 12)
        outputView.textContainerInset = NSSize(width: 7, height: 7)
        outputView.isHorizontallyResizable = false
        outputView.isVerticallyResizable = true
        outputView.autoresizingMask = [.width]
        outputView.textContainer?.widthTracksTextView = true
        outputView.string = "Progress will appear here."
        scroll.documentView = outputView
        content.addSubview(scroll)

        let logLabel = NSTextField(labelWithString: "A detailed log is saved in your SimCity 4 Windows → Setup logs folder.")
        logLabel.font = .systemFont(ofSize: 11)
        logLabel.textColor = .secondaryLabelColor
        logLabel.frame = NSRect(x: 24, y: 56, width: 602, height: 17)
        content.addSubview(logLabel)

        closeButton = NSButton(title: "Close", target: self, action: #selector(close))
        closeButton.bezelStyle = .rounded
        closeButton.frame = NSRect(x: 424, y: 16, width: 92, height: 32)
        content.addSubview(closeButton)

        rebuildButton = NSButton(title: "Rebuild", target: self, action: #selector(rebuild))
        rebuildButton.bezelStyle = .rounded
        rebuildButton.keyEquivalent = "\r"
        rebuildButton.frame = NSRect(x: 524, y: 16, width: 102, height: 32)
        content.addSubview(rebuildButton)

        window.makeKeyAndOrderFront(nil)
        NSApp.activate(ignoringOtherApps: true)
    }

    private func installMenu() {
        let menu = NSMenu()
        let applicationItem = NSMenuItem()
        menu.addItem(applicationItem)
        let appMenu = NSMenu()
        appMenu.addItem(withTitle: "Quit Rebuild SimCity Content", action: #selector(NSApplication.terminate(_:)), keyEquivalent: "q")
        applicationItem.submenu = appMenu
        let editItem = NSMenuItem()
        menu.addItem(editItem)
        let editMenu = NSMenu(title: "Edit")
        editMenu.addItem(withTitle: "Copy", action: #selector(NSText.copy(_:)), keyEquivalent: "c")
        editMenu.addItem(withTitle: "Select All", action: #selector(NSText.selectAll(_:)), keyEquivalent: "a")
        editItem.submenu = editMenu
        NSApp.mainMenu = menu
    }

    @objc private func rebuild() {
        guard !busy else { return }
        busy = true
        rebuildButton.isEnabled = false
        closeButton.isEnabled = false
        spinner.startAnimation(nil)
        statusLabel.stringValue = "Checking that the game is closed…"
        statusLabel.textColor = .labelColor
        displayedOutput = ""
        outputView.string = ""

        DispatchQueue.global(qos: .userInitiated).async { [weak self] in
            self?.runRebuild()
        }
    }

    private func appendOutput(_ message: String) {
        DispatchQueue.main.async { [weak self] in
            guard let self = self else { return }
            self.displayedOutput += message
            // Keep the window responsive; the on-disk log retains all output.
            if self.displayedOutput.count > 24_000 {
                self.displayedOutput = String(self.displayedOutput.suffix(20_000))
            }
            self.outputView.string = self.displayedOutput
            self.outputView.scrollToEndOfDocument(nil)
        }
    }

    private func runRebuild() {
        let fileManager = FileManager.default
        var ownsLock = false
        var log: FileHandle?
        var succeeded = false
        var finalMessage = "Rebuild could not start. Read the details below, then try again."
        var progress = ReadableProgress()
        defer {
            try? log?.close()
            if ownsLock { try? fileManager.removeItem(at: lockURL) }
            finish(success: succeeded, message: finalMessage)
        }

        func record(_ message: String, show: Bool = false) {
            if let data = message.data(using: .utf8) { try? log?.write(contentsOf: data) }
            if show { appendOutput(message) }
        }

        do {
            try checkGameClosed()
            let builder = toolsDirectory.appendingPathComponent("SC4PlopAndPaintCacheBuilder")
            guard fileManager.isExecutableFile(atPath: builder.path) else {
                appendOutput("Expected builder: \(builder.path)\n")
                throw HelperError.missingBuilder
            }
            // mkdir succeeds only for the process that creates this directory.
            // Foundation's directory creation can also accept an existing directory.
            if Darwin.mkdir(lockURL.path, mode_t(0o700)) != 0 {
                let failure = errno
                if failure == EEXIST {
                    throw HelperError.alreadyRunning
                }
                throw NSError(domain: NSPOSIXErrorDomain, code: Int(failure),
                              userInfo: [NSFilePathErrorKey: lockURL.path])
            }
            ownsLock = true
            try "\(ProcessInfo.processInfo.processIdentifier)\n".write(to: lockURL.appendingPathComponent("pid"), atomically: true, encoding: .utf8)
            try fileManager.createDirectory(at: logURL.deletingLastPathComponent(), withIntermediateDirectories: true)
            if !fileManager.fileExists(atPath: logURL.path) {
                guard fileManager.createFile(atPath: logURL.path, contents: nil) else {
                    throw CocoaError(.fileWriteUnknown)
                }
            }
            log = try FileHandle(forWritingTo: logURL)
            try log?.truncate(atOffset: 0)
            record("Plop and Paint content rebuild\nStarted: \(Date())\nBuilder: \(builder.path)\n\n")
            // Check again immediately before starting the builder.
            try checkGameClosed()
            DispatchQueue.main.async { [weak self] in
                self?.statusLabel.stringValue = "Rebuilding the content list and preview pictures…"
            }

            let process = Process()
            let output = Pipe()
            process.executableURL = builder
            process.currentDirectoryURL = toolsDirectory
            process.arguments = ["--scan", "--game", gameDirectory, "--plugins", pluginsDirectory,
                                 "--locale", "English", "--render-thumbnails", "--thumbnail-size", "44"]
            process.standardOutput = output
            process.standardError = output
            process.standardInput = FileHandle.nullDevice
            try process.run()
            while true {
                let data = output.fileHandleForReading.availableData
                if data.isEmpty { break }
                try? log?.write(contentsOf: data)
                let messages = progress.consume(String(decoding: data, as: UTF8.self))
                if !messages.isEmpty { appendOutput(messages.joined(separator: "\n") + "\n") }
            }
            process.waitUntilExit()
            let lastMessages = progress.consume("", final: true)
            if !lastMessages.isEmpty { appendOutput(lastMessages.joined(separator: "\n") + "\n") }
            if !progress.notes.isEmpty { appendOutput("\n" + progress.notes.joined(separator: "\n") + "\n") }
            record("\nFinished: \(Date())\nExit code: \(process.terminationStatus)\n")
            if process.terminationReason == .exit && process.terminationStatus == 0 {
                succeeded = !progress.hasContentErrors
                if progress.hasContentErrors {
                    finalMessage = "Finished with reported problems. Read the notes below before starting the game."
                } else {
                    appendOutput("\nFinished. Your content list is ready.\n")
                    finalMessage = "Finished. You can start SimCity 4 and press O in a city to open Plop and Paint."
                }
            } else {
                appendOutput("\nThe builder stopped before completing the rebuild. Its error details are saved in the log.\n")
                finalMessage = "The rebuild did not finish successfully. Read the progress below or the saved log before trying again."
            }
        } catch {
            record("\n\(error.localizedDescription)\n", show: true)
            if case HelperError.gameOpen = error {
                finalMessage = "Quit SimCity 4, then click Rebuild again."
            }
        }
    }

    private func finish(success: Bool, message: String) {
        DispatchQueue.main.async { [weak self] in
            guard let self = self else { return }
            self.busy = false
            self.spinner.stopAnimation(nil)
            self.rebuildButton.isEnabled = true
            self.closeButton.isEnabled = true
            self.statusLabel.stringValue = message
            self.statusLabel.textColor = success ? .systemGreen : .systemRed
        }
    }

    @objc private func close() {
        if !busy { NSApp.terminate(nil) }
    }

    func windowShouldClose(_ sender: NSWindow) -> Bool {
        if busy {
            statusLabel.stringValue = "Please keep this window open until the rebuild finishes."
            return false
        }
        return true
    }

    func applicationShouldTerminateAfterLastWindowClosed(_ sender: NSApplication) -> Bool { true }

    func applicationShouldTerminate(_ sender: NSApplication) -> NSApplication.TerminateReply {
        if busy {
            statusLabel.stringValue = "Please keep this window open until the rebuild finishes."
            return .terminateCancel
        }
        return .terminateNow
    }
}

let application = NSApplication.shared
let delegate = AppDelegate()
application.setActivationPolicy(.regular)
application.delegate = delegate
application.run()
