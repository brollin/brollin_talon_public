os: mac
-

# TODO: get global hotkeys working so we don't have to switch to OBS first

^obs stop [stream]$:
    user.switcher_focus("obs")
    key(ctrl-alt-f11)

^(obs scene | obscene) spire$:
    user.switcher_focus("obs")
    key(ctrl-alt-f12)

^(obs scene | obscene) (be right back | burb)$:
    user.switcher_focus("obs")
    key(ctrl-alt-f13)

^(obs scene | obscene) global$:
    user.switcher_focus("obs")
    key(ctrl-alt-f16)

^obs mike off$:
    user.switcher_focus("obs")
    key(ctrl-alt-f14)

^obs mike on$:
    user.switcher_focus("obs")
    key(ctrl-alt-f15)
