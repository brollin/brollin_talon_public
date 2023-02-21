os: mac
and app.bundle: com.microsoft.VSCode
-
commie: key(cmd-/)

scroll down: key(ctrl-d)
scroll up: key(ctrl-u)

search: key(cmd-shift-f)
result last: user.vscode("search.action.focusPreviousSearchResult")
result next: user.vscode("search.action.focusNextSearchResult")

ref last: user.vscode("references-view.prev")
ref next: user.vscode("references-view.next")

# TODO make these language specific
to do comment: insert("// TODO: ")
op empty lambda: insert("() => ")

tab move left: user.vscode("workbench.action.moveEditorLeftInGroup")
tab move right: user.vscode("workbench.action.moveEditorRightInGroup")
tab move left group: user.vscode("workbench.action.moveEditorToLeftGroup")
tab move right group: user.vscode("workbench.action.moveEditorToRightGroup")
tab closer: user.vscode("workbench.action.closeEditorsToTheRight")

crossed: user.vscode("workbench.action.navigateEditorGroups")

remove unused: user.vscode("typescript.removeUnusedImports")

panel max: key("cmd-shift-k")
please rewrap: key("alt-q")

# for selecting a quick pick item
pick <number_small>: key("down:{number_small-1} enter")
pick up <number_small>: key("up:{number_small} enter")

copy command: user.copy_command_id()
copy command <number_small>:
    key("down:{number_small-1}")
    sleep(350ms)
    user.copy_command_id()

run test: user.vscode("testing.runAtCursor")

to do open:
    key(cmd-p)
    sleep(200ms)
    insert("/Users/ben.rollin/todo.md")
    sleep(200ms)
    key(enter)

re folk: key(cmd-1)
