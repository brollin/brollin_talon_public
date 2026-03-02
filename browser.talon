tag: browser
-

hints: user.rango_command_without_target("toggleHints")

spike <user.rango_target>:
    user.rango_command_with_target("clickElement", rango_target)

down: user.rango_command_without_target("scrollDownPage")

bit warden:
    key(cmd-shift-l)

bit password:
    key(cmd-shift-9)

address | address bar | go address | go url: browser.focus_address()
address copy | url copy | copy address | copy url:
    browser.focus_address()
    sleep(50ms)
    edit.copy()

go forward: browser.go_forward()
go backward: browser.go_back()
