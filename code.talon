os: mac
and app.bundle: com.microsoft.VSCode
-
commie: key(cmd-/)

downer: key(ctrl-d)
scroll down: key(ctrl-d)
scroll up: key(ctrl-u)
upper: key(ctrl-u)

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

crosser: user.vscode("workbench.action.navigateEditorGroups")

remove unused: user.vscode("remove-unused-imports.main")

document this: user.vscode("docthis.documentThis")

new folder: user.vscode("explorer.newFolder")

file keep: user.vscode("workbench.action.keepEditor")

please rewrap: key("alt-q")

# for selecting a quick pick item
choose <number_small>: key("down:{number_small-1} enter")
choose up <number_small>: key("up:{number_small} enter")

copy command: user.copy_command_id()
copy command <number_small>:
    key("down:{number_small-1}")
    sleep(350ms)
    user.copy_command_id()

run test: user.vscode("testing.runAtCursor")
decorations: user.vscode("cursorless.toggleDecorations")

re folk: key(cmd-1)

complete:
    key(tab)
    key(enter)

# https://github.com/cursorless-dev/cursorless/wiki/Common-recommendations
then: skip()

react apostrophe: "&apos;"

maven package:
    user.vscode("maven.goal.execute")
    sleep(350ms)
    insert("package\n")

package and run:
    user.vscode("workbench.action.tasks.runTask")
    sleep(350ms)
    insert("packageAndRun\n")
    sleep(100ms)
    key(enter)

panel max: key(cmd-shift-k)
panel right: user.vscode("workbench.action.positionPanelRight")
panel (bottom | bot): user.vscode("workbench.action.positionPanelBottom")

{user.search_engine} scout <user.cursorless_target>:
    text = user.cursorless_get_text(cursorless_target)
    user.search_with_search_engine(search_engine, text)

imports fix:
    user.vscode_add_missing_imports()
    sleep(100ms)
    user.vscode("editor.action.organizeImports")

entry new:
    mimic("pre file this post section this slap slap hash hash pad date insert slap slap")
