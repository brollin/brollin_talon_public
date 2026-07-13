os: mac
os: windows
-

# enable emojis everywhere
tag(): user.emoji

# TODO: separate operating system specific features into their own files
settings():
    user.screenshot_folder = "~/Desktop"
    user.cursorless_settings_directory = "talon_umbrella/cursorless-settings"

<number_small>: "{number_small}"

(pad | padding): insert(" ")
pound: insert(" ")
question [mark]: "?"
pad stack: " :"
pad dash: " -"
leper: "("
riper: ")"

^drowse [<phrase>]$: speech.disable()

clippy: edit.paste()
clipsy: edit.copy()

snap dome: insert("snabbdom")

# switch to last application
go switch: key(cmd-tab)

disk: key(cmd-s)

# javascript
consol log:
    insert("console.log()")
    key(left)

rectangle top right: key(ctrl-alt-i)

# Use the command "running list" to see names of running apps
(focus | folk) (gmail | mail):
    user.switcher_focus("Firefox")
    key(cmd-1)

(focus | folk) calendar:
    user.switcher_focus("Firefox")
    key(cmd-2)

(focus | folk) zulip:
    user.switcher_focus("Zulip")

(focus | folk) fox:
    user.switcher_focus("Firefox")

(focus | folk) Spotify:
    user.switcher_focus("Spotify")
    key(cmd-1)

(focus | folk) to do:
    user.open_file_in_obsidian("/Users/ben.rollin/BensObsidianVault/todo.md")

(focus | folk) curse:
    user.switcher_focus("Cursor")


secret fire: "se.cretfi.re"

center: user.move_to_spot("center")

key(f5): user.toggle_talon()
computer sleep:
    user.move_to_spot("apple")
    sleep(0.1)
    mouse_click(0)
    sleep(0.1)
    key("down:{6}")
    user.sleep_talon()

^<number> point <number>$:
    insert(number_1)
    insert(".")
    insert(number_2)

to do open: user.open_file_in_cursor("/Users/ben.rollin/BensObsidianVault/todo.md")
health open: user.open_file_in_cursor("/Users/ben.rollin/BensObsidianVault/health.md")
journal open: user.open_file_in_cursor("/Users/ben.rollin/BensObsidianVault/journal.md")
game open: user.open_file_in_cursor("/Users/ben.rollin/BensObsidianVault/Game\ Dev.md")

Spotify hunt <user.text>:
    user.switcher_focus("chrome")
    user.rango_run_action_on_reference("clickElement", "search")
    insert(text)

wake up: skip()

open <user.system_path>: user.open_path_with_default_program(system_path)

stowner: user.mouse_scroll_down(8)
supper: user.mouse_scroll_up(8)

scrapey: key("escape:{5}")

cargo run: insert("cargo run")
