sporc {user.service}: user.sporc_service_gui(service, "")
prod {user.service} [service]: user.sporc_service_gui(service, "prod")
dev {user.service} [service]: user.sporc_service_gui(service, "dev")
local {user.service} [service]: user.sporc_service_gui(service, "local")

link {user.service} [service] [prod]: user.sporc_link(service, "prod")
link {user.service} [service] dev: user.sporc_link(service, "dev")
link {user.service} [service] local: user.sporc_link(service, "local")
link {user.service} [service] git: user.sporc_link(service, "git")

repo {user.service} [service]: user.sporc_repo(service)

open {user.service} [service] [prod]: user.sporc_open(service, "prod")
open {user.service} [service] dev: user.sporc_open(service, "dev")
open {user.service} [service] local: user.sporc_open(service, "local")
open {user.service} [service] git: user.sporc_open(service, "git")
