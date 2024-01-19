tag: browser
-

hints: user.rango_command_without_target("toggleHints")

knock <user.rango_target>:
    user.rango_command_with_target("clickElement", rango_target)

down: user.rango_command_without_target("scrollDownPage")
