# activate homerow (gives clicking hints)
^coat$: key(cmd-shift-space)

# activate homerow (searches for text)
^coat <user.text>$:
    key(ctrl-alt-shift-f18)
    sleep(0.1)
    insert(text)
