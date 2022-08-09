os: mac
and app.bundle: com.microsoft.VSCode
-
scroll down:
    key(ctrl-d)

scroll up:
    key(ctrl-u)

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
tab closer: user.vscode("workbench.action.closeEditorsToTheRight")

panel max: key("cmd-shift-k")

# for selecting a quick pick item
pick <number_small>: key("down:{number_small-1} enter")
pick up <number_small>: key("up:{number_small} enter")

copy command: user.copy_command_id()
copy command <number_small>:
    key("down:{number_small-1}")
    sleep(350ms)
    user.copy_command_id()
