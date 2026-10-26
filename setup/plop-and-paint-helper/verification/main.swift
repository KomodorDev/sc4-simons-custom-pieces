import Foundation

// Offline verification against the successful recorded rebuild. This does not
// invoke the builder, open a window, or change the installed game or its log.
let log = try Data(contentsOf: URL(fileURLWithPath: "/Users/simonhinterreiter/Documents/SimCity 4 Windows/Setup logs/Plop and Paint cache rebuild.log"))
var progress = ReadableProgress()
var messages: [String] = []
for offset in stride(from: 0, to: log.count, by: 257) {
    let chunk = log[offset..<min(offset + 257, log.count)]
    messages += progress.consume(String(decoding: chunk, as: UTF8.self))
}
messages += progress.consume("", final: true)
messages += progress.notes
let output = messages.joined(separator: "\n")
precondition(messages.count < 30, "Output should remain concise")
precondition(output.contains("Processed 2 of 798 files."))
precondition(output.contains("Found 486 buildings and 1932 lots."))
precondition(output.contains("Saved 1988 object previews."))
precondition(output.contains("Some special objects have no preview"))
precondition(output.contains("Skipped the game's uninstaller data"))
precondition(!output.contains("0x") && !output.contains("/Users/") && !output.contains("[debug]"))
precondition(!progress.hasContentErrors, "A skipped uninstaller file is not unreadable game content")
print(output)
print("\nPASS: \(log.count) raw log bytes became \(messages.count) readable messages; warnings retained and no content errors reported.")
