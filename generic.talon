os: mac
os: windows
-
# TODO: separate operating system specific features into their own files
settings():
    user.screenshot_folder = "~/Desktop"
    user.cursorless_settings_directory = "talon_umbrella/cursorless-settings"

(pad | padding): insert(" ")

clippy: edit.paste()
clipsy: edit.copy()

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
term clever: insert("cd $CODE_HOME\n")
term search: insert("rg ")
snap dome: insert("snabbdom")

# activate homerow (gives clicking hints)
slinks: key(cmd-shift-space)

# switch to last application
go switch: key(cmd-tab)

disk: key(cmd-s)
do again: core.repeat_phrase()

# javascript
consol log:
    insert("console.log()")
    key(left)

node pack: insert("npm ")
node pack install: insert("npm install ")
node pack clean install: insert("npm ci ")
node pack uninstall: insert("npm uninstall ")
node pack install save: insert("npm install --save ")
node pack install save dev: insert("npm install --save-dev ")
node pack start: insert("npm start ")
node pack run: insert("npm run ")
node pack run dev: insert("npm run dev ")
node pack help: insert("npm help ")
node pack init: insert("npm init ")

node pack ex: insert("npx ")
node pack ex webpack: insert("npx webpack ")
node pack ex <user.text>:
    insert("npx ")
    insert(text)

yarn: insert("yarn ")
yarn <user.text>: insert("yarn " + text)
yarn add: insert("yarn add ")
yarn add dev: insert("yarn add --dev ")
yarn upgrade: insert("yarn upgrade ")
yarn remove: insert("yarn remove ")
yarn build: insert("yarn build ")
yarn lint: insert("yarn lint ")
yarn (dev | dove): insert("yarn dev")
yarn dev watch: insert("yarn dev -w")

pip install: insert("pip3 install ")

brew install: insert("brew install ")
brew link: insert("brew link ")
brew link force: insert("brew link --force")
brew link force go: insert("brew link --force go@1.1")
brew unlink: insert("brew unlink ")

node version use: insert("nvm use ")
node version use <user.number_string>:
    insert("nvm use ")
    insert(number_string)
    key(enter)

node version alias: insert("nvm alias default ")
node version alias <user.number_string>:
    insert("nvm alias default ")
    insert(number_string)
    key(enter)

node version install: insert("nvm install ")

rectangle top right: key(ctrl-alt-i)

folk gmail:
    user.switcher_focus("firefox")
    key(cmd-1)

folk work [gmail]:
    user.switcher_focus("firefox")
    key(cmd-2)

folk calendar:
    user.switcher_focus("firefox")
    key(cmd-3)

folk slack:
    user.switcher_focus("firefox")
    key(cmd-4)

folk Spotify:
    user.switcher_focus("firefox")
    key(cmd-5)

folk discord:
    user.switcher_focus("firefox")
    key(cmd-6)

folk zulip:
    user.switcher_focus("firefox")
    key(cmd-7)

folk main:
    user.switcher_focus("firefox")
    key(cmd-8)

bit warden:
    key(cmd-shift-l)

question [mark]: "?"

secret fire: "se.cretfi.re"

pad stack: " :"
key(f5): user.toggle_talon()
