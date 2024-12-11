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
