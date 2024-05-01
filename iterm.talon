app: iterm2
-
drain: key(alt-left)
step: key(alt-right)
scratcher: key(alt-backspace)
complete:
    key(tab)
    key(enter)
yes and:
    key(y)
    key(enter)
no and:
    key(n)
    key(enter)

tab last: key("cmd-shift-[")
tab next: key("cmd-shift-]")

# terminal helpers
term change: insert("cd ")
term change <user.text>:
    insert("cd ")
    insert(text)
    key(tab)
term change back: insert("cd ..\n")
term change last: insert("cd -\n")
make dir: insert("mkdir ")
vintage: insert("vim ")
vintage disk:
    insert(":wq")
    key(enter)
term clear: key(ctrl-l)
term copy: insert("cp ")
term cat: insert("cat ")
term diff: insert("diff ")
term list: insert("ls ")
term move: insert("mv ")
term remove: insert("rm ")
term open: insert("open ")
term open here: insert("open .\n")
term code: insert("code ")
term code here: insert("code .\n")
term reverse: key(ctrl-r)
term talon: insert("cd ~/.talon/user/talon_umbrella\n")
term talon log: insert("tail -f ~/.talon/talon.log\n")
# term talon log: insert("grc tail -f ~/.talon/talon.log\n")
term projects: insert("cd ~/projects && c\n")
term desktop: insert("cd ~/Desktop && c\n")
term clever: insert("cd $CODE_HOME\n")
term search: insert("rg ")
