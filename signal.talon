os: mac
and app.bundle: org.whispersystems.signal-desktop
-

message <number_small>:
    key(cmd-f)
    key(tab)
    repeat(number_small - 1)
    key(enter)

voice message:
    key(tab)
    key(tab)
    key(enter)
    user.sleep_talon()
