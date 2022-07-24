os: mac
os: windows
-
# TODO: separate operating system specific features into their own files
settings():
    user.screenshot_folder = "~/Desktop"
    user.cursorless_settings_directory = "talon_umbrella/cursorless-settings"

(pad | padding): insert(" ")

# terminal helpers
change dir: insert("cd ")
change dir back:
    insert("cd ..")
    key(enter)
make dir: insert("mkdir ")
vintage: insert("vim ")
vintage disk:
    insert(":wq")
    key(enter)
term clear: key(ctrl-l)
term copy: insert("cp ")
term cat: insert("cat ")
term list: insert("ls ")
term move: insert("mv ")
term remove: insert("rm ")
term code: insert("code .")
term code here:
    insert("code .")
    key(enter)
snap dome: insert("snabbdom")

# switch to last application
go switch:
    key(cmd-tab)

disk: key(cmd-s)

# windowing commands from rectangle
maximise:
    key(cmd-shift-m)
snap middle:
    key(ctrl-alt-shift-`)
make smaller:
    key(ctrl-alt--)
make larger:
    key(ctrl-alt-=)

# javascript
consol log:
    insert("console.log()")
    key(left)

node pack: insert("npm ")
node pack install: insert("npm install ")
node pack uninstall: insert("npm uninstall ")
node pack install save: insert("npm install --save ")
node pack install save dev: insert("npm install --save-dev ")
node pack start: insert("npm start ")
node pack run: insert("npm run ")
node pack help: insert("npm help ")

yarn: insert("yarn")
yarn add: insert("yarn add ")
yarn add dev: insert("yarn add --dev ")
yarn dev: insert("yarn dev")
yarn dev watch: insert("yarn dev -w")
