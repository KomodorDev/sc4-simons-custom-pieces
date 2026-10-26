import Foundation

/// Translates the builder's log into a few user-facing milestones.
/// The original bytes are still written unchanged to the full log.
struct ReadableProgress {
    private var pending = ""
    private var shown = Set<String>()
    private var missingPreviews = false
    private var skippedUninstallerFiles = 0
    private var indexingErrors = 0
    private var parseErrors = 0
    private var otherWarnings = false
    private var reportedErrors = false

    var hasContentErrors: Bool {
        reportedErrors || parseErrors > 0 || indexingErrors > skippedUninstallerFiles
    }

    mutating func consume(_ text: String, final: Bool = false) -> [String] {
        pending += text
        var messages: [String] = []
        while let newline = pending.firstIndex(of: "\n") {
            let line = String(pending[..<newline])
            pending.removeSubrange(...newline)
            if let message = translate(line), shown.insert(message).inserted {
                messages.append(message)
            }
        }
        if final && !pending.isEmpty {
            let line = pending
            pending = ""
            if let message = translate(line), shown.insert(message).inserted {
                messages.append(message)
            }
        }
        return messages
    }

    var notes: [String] {
        var result: [String] = []
        if skippedUninstallerFiles > 0 {
            result.append("Skipped the game's uninstaller data; it does not contain playable content.")
        }
        if missingPreviews {
            result.append("Some special objects have no preview; details are in the log.")
        }
        if parseErrors > 0 || indexingErrors > skippedUninstallerFiles {
            result.append("Some game content could not be read; details are in the log.")
        }
        if reportedErrors {
            result.append("The builder reported an error; check the saved log before trying again.")
        }
        if otherWarnings {
            result.append("The builder reported additional warnings; details are in the log.")
        }
        return result
    }

    private mutating func translate(_ line: String) -> String? {
        if line.contains("Thumbnail render failed") || line.contains("Unable to load model bounds") || line.contains("Did not manage to resolve model TGI") {
            missingPreviews = true
        } else if line.contains("[warning]") && line.contains("unins000.dat, not a DBPF file?") {
            skippedUninstallerFiles += 1
        } else if line.contains("[warning]") {
            otherWarnings = true
        }
        if line.contains("[error]") || line.contains("[critical]") { reportedErrors = true }

        if line.contains("Initializing plugin scanner") {
            return "Reading installed game content and mods…"
        }
        if line.contains("Indexing progress:"), let values = captures("Indexing progress: ([0-9]+)/([0-9]+) files processed", in: line) {
            return "Processed \(values[0]) of \(values[1]) files."
        }
        if line.contains("Indexing complete:"), let values = captures("Indexing complete: ([0-9]+) files processed, [0-9]+ entries indexed, ([0-9]+) errors", in: line) {
            indexingErrors = Int(values[1]) ?? 0
            return "Finished reading \(values[0]) files."
        }
        if line.contains("Processing exemplar/cohort records") {
            return "Creating previews for buildings, objects, and plants…"
        }
        if line.contains("Scan complete:"), let values = captures("Scan complete: ([0-9]+) buildings with lots, ([0-9]+) lots, ([0-9]+) parse errors", in: line) {
            parseErrors = Int(values[2]) ?? 0
            return "Found \(values[0]) buildings and \(values[1]) lots."
        }
        if line.contains("Exported "), let values = captures("Exported ([0-9]+) (building|prop|flora) thumbnails", in: line) {
            let type = ["building": "building", "prop": "object", "flora": "plant"][values[1]] ?? "content"
            return "Saved \(values[0]) \(type) previews."
        }
        return nil
    }

    private func captures(_ pattern: String, in line: String) -> [String]? {
        guard let expression = try? NSRegularExpression(pattern: pattern),
              let match = expression.firstMatch(in: line, range: NSRange(line.startIndex..., in: line)) else { return nil }
        return (1..<match.numberOfRanges).compactMap { index in
            Range(match.range(at: index), in: line).map { String(line[$0]) }
        }
    }
}
