tag: browser
browser.host: localhost:3000
-

# track {user.conjurer_target}: user.conjurer_send_action_with_args("track", conjurer_target, "bool", 1)
# untrack {user.conjurer_target}: user.conjurer_send_action_with_args("track", conjurer_target, "bool", 0)

# track {user.conjurer_target} <number>: user.conjurer_send_action_with_args("track", conjurer_target, "int", number)

testing: user.conjurer_send_action("action", "testing")
