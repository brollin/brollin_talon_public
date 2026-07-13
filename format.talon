mode: command
mode: dictation
-
# Select all, then apply "model fix grammar". Works in command, mixed, and dictation.
format that: user.select_all_and_fix_grammar()

# Override community vscode/Cursor "format that" (was document format).
app: vscode
mode: command
mode: dictation
-
format all: user.select_all_and_fix_grammar()
