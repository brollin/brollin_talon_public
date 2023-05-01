sporc {user.service}: user.sporc_service_gui(service, "")
sporc {user.service} [service] prod: user.sporc_service_gui(service, "prod")
sporc {user.service} [service] dev: user.sporc_service_gui(service, "dev")
sporc {user.service} [service] local: user.sporc_service_gui(service, "local")

link {user.service} [service] [prod]: user.sporc_link(service, "prod")
link {user.service} [service] dev: user.sporc_link(service, "dev")
link {user.service} [service] local: user.sporc_link(service, "local")
link {user.service} [service] git: user.sporc_link(service, "git")

repo {user.service} [service]: user.sporc_repo(service)

open {user.service} [service] [prod]: user.sporc_open(service, "prod")
open {user.service} [service] dev: user.sporc_open(service, "dev")
open {user.service} [service] local: user.sporc_open(service, "local")
open {user.service} [service] git: user.sporc_open(service, "git")

code {user.service} [service]: user.sporc_code(service)
term change {user.service} [service]: user.sporc_change_directory(service)
