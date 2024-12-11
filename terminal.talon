node pack: insert("npm ")
node pack install: insert("npm install ")
node pack clean install: insert("npm ci ")
node pack uninstall: insert("npm uninstall ")
node pack install save: insert("npm install --save ")
node pack install save dev: insert("npm install --save-dev ")
node pack start: insert("npm start ")
node pack run dev: insert("npm run dev ")
node pack help: insert("npm help ")
node pack init: insert("npm init ")
node pack test: insert("npm test ")

node pack run [<user.text>]:
    insert("npm run ")
    insert(text or "")

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
yarn typecheck: insert("yarn typecheck ")
yarn lint: insert("yarn lint ")
yarn (dev | dove): insert("yarn dev")
yarn dev watch: insert("yarn dev -w")
yarn db generate: insert("yarn db:generate")
yarn db [local] setup: insert("yarn db:local:setup")
yarn db [local] migrate: insert("yarn db:local:migrate")
yarn db [local] studio: insert("yarn db:local:studio")
yarn db prod setup: insert("yarn db:prod:setup")
yarn db prod migrate: insert("yarn db:prod:migrate")
yarn db prod studio: insert("yarn db:prod:studio")
yarn db [prod] download: insert("yarn db:prod:download")

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

pip install: insert("pip3 install ")

brew install: insert("brew install ")
brew link: insert("brew link ")
brew link force: insert("brew link --force")
brew link force go: insert("brew link --force go@1.1")
brew unlink: insert("brew unlink ")

# lichess
ui build: insert("ui/build -cdr")
