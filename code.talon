os: mac
and app.bundle: com.microsoft.VSCode
-
scroll down:
    key(ctrl-d)

scroll up:
    key(ctrl-u)

yarn dev: insert("yarn dev")
yarn dev watch: insert("yarn dev -w")

search: key(cmd-shift-f)
result last: key(shift-f4)
result next: key(f4)

# TODO make these language specific
to do comment: insert("// TODO ")
op empty lambda: insert("() => ")

tab move left: user.vscode("workbench.action.moveEditorLeftInGroup")
tab move right: user.vscode("workbench.action.moveEditorRightInGroup")
tab move left group: user.vscode("workbench.action.moveEditorToLeftGroup")
tab move right group: user.vscode("workbench.action.moveEditorToRightGroup")
