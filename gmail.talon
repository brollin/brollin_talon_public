tag: browser
browser.host: mail.google.com
-

expand all: key(;)
go inbox:
    key(g)
    key(i)

# lichess stuff

^hello$: "Hello,\n\n"
^regards$: key(ctrl-shift-e)
^sign off$:
    key(enter)
    key(enter)
    key(ctrl-shift-e)
    key(cmd-enter)
archive$: "e"
hermes: key(ctrl-shift-g)
