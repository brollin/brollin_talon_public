os: mac
os: windows
-

# enable emojis everywhere
tag(): user.emoji

# TODO: separate operating system specific features into their own files
settings():
    user.screenshot_folder = "~/Desktop"
    user.cursorless_settings_directory = "talon_umbrella/cursorless-settings"

(pad | padding): insert(" ")

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

folk (gmail | mail):
    user.switcher_focus("firefox")
    key(cmd-1)

folk text:
    user.switcher_focus("firefox")
    key(cmd-2)

folk calendar:
    user.switcher_focus("firefox")
    key(cmd-3)

folk slack:
    user.switcher_focus("firefox")
    key(cmd-4)

folk discord:
    user.switcher_focus("firefox")
    key(cmd-5)

folk zulip:
    user.switcher_focus("firefox")
    key(cmd-6)

folk main:
    user.switcher_focus("firefox")
    key(cmd-7)

folk Spotify:
    user.switcher_focus("chrome")
    key(cmd-1)

question [mark]: "?"

secret fire: "se.cretfi.re"

pad stack: " :"
pad dash: " -"
key(f5): user.toggle_talon()

center: user.move_to_spot("center")

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

to do open: user.open_file_in_vscode("/Users/ben.rollin/.talon/user/talon_umbrella/brollin_talon/todo.md")
health open: user.open_file_in_vscode("/Users/ben.rollin/.talon/user/talon_umbrella/brollin_talon/health.md")
game open: user.open_file_in_vscode("/Users/ben.rollin/.talon/user/talon_umbrella/brollin_talon/game.md")
spire open: user.open_file_in_vscode("/Users/ben.rollin/spire.md")
