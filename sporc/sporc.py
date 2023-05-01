import time
import typing
from talon import Module, Context, ui, ctrl, canvas, screen, actions, imgui, clip
from .services import services, get_full_github_path, get_local_repo_path

mod = Module()
ctx = Context()

mod.tag("sporc_gui_showing", desc="The sporc gui is visible")

# get_list_from_csv(
#     "websites.csv",
#     headers=("URL", "Spoken name"),
#     default=website_defaults,
# )
mod.list("service", desc="A service with endpoints")
ctx.lists["self.service"] = {key: key for key in services}


def get_editor_app() -> ui.App:
    editor_names = [
        "Visual Studio Code",
        "Code",
        "VSCodium",
        "Codium",
        "code-oss",
    ]

    for app in ui.apps(background=False):
        if app.name in editor_names:
            return app

    raise RuntimeError("Draft editor is not running")


class SporcController:
    showing = False
    service = ""
    endpoint = 0

    def service_text(self, service_spoken: str) -> str:
        return services[service_spoken]["domains"]["prod"]

    def show_service_gui(self, service_spoken: str, environment: str):
        self.environment = (
            environment if environment in ["prod", "dev", "local"] else "dev"
        )
        self.service = service_spoken

        self.showing = True
        ctx.tags = ["user.sporc_gui_showing"]
        choose_endpoint_gui.show()

    def hide_service_gui(self):
        self.showing = False
        ctx.tags = []
        choose_endpoint_gui.hide()

    def choose_number(self, number: int):
        service = services[sporc_controller.service]
        url = (
            service["domains"][self.environment] + service["endpoints"][number]["path"]
        )

        # TODO: don't automatically copy to clipboard
        clip.set_text(url)

        actions.user.switcher_focus_app(get_editor_app())
        # Wait additional time for talon context to update.
        actions.sleep("200ms")
        actions.app.tab_open()
        actions.insert(url)

        self.hide_service_gui()

    def repo(self, service_spoken: str):
        service = services[service_spoken]
        repo = service["id"]

        actions.insert(repo)

    def open(self, service_spoken: str, environment: str):
        service = services[service_spoken]

        if environment == "git":
            actions.user.open_url(get_full_github_path(service))
            return

        self.environment = (
            environment if environment in ["prod", "dev", "local"] else "prod"
        )
        url = service["domains"][environment]

        actions.user.open_url(url)

    def insert_link(self, service_spoken: str, environment: str):
        service = services[service_spoken]

        if environment == "git":
            url = get_full_github_path(service)
        else:
            self.environment = (
                environment if environment in ["prod", "dev", "local"] else "prod"
            )
            url = service["domains"][environment]

        actions.insert(url)

    def open_vscode(self, service_spoken: str):
        service = services[service_spoken]

        command = "open -a 'Visual Studio Code' " + get_local_repo_path(service)
        actions.user.system_command_nb(command)

    def open_repo_directory(self, service_spoken: str):
        service = services[service_spoken]

        command = "cd " + get_local_repo_path(service)
        actions.insert(command)
        actions.key("enter")


sporc_controller = SporcController()


@imgui.open()
def choose_endpoint_gui(gui: imgui.GUI):
    gui.text("Choose #:")
    gui.spacer()

    service = services[sporc_controller.service]
    for index, endpoint in enumerate(service["endpoints"]):
        gui.text(str(index) + ".\t" + endpoint["method"] + "\t" + endpoint["name"])

    gui.spacer()
    if gui.button("Cancel"):
        choose_endpoint_gui.hide()


@mod.action_class
class SporcActions:
    def sporc_service_text(service_spoken: str) -> str:
        """Type the text of a service's default endpoint"""
        return sporc_controller.service_text(service_spoken)

    def sporc_service_gui(service_spoken: str, environment: str):
        """Show the sporc gui for the spoken service"""
        sporc_controller.show_service_gui(service_spoken, environment)

    def sporc_gui_hide():
        """Hide the sporc gui"""
        sporc_controller.hide_service_gui()

    def sporc_gui_choose_number(number: int):
        """Choose an option in the sporc gui"""
        sporc_controller.choose_number(number)

    def sporc_repo(service_spoken: str):
        """Insert the name of a repo"""
        sporc_controller.repo(service_spoken)

    def sporc_open(service_spoken: str, environment: str):
        """Open the service in the browser"""
        sporc_controller.open(service_spoken, environment)

    def sporc_link(service_spoken: str, environment: str):
        """Insert the service link (URL)"""
        sporc_controller.insert_link(service_spoken, environment)

    def sporc_code(service_spoken: str):
        """Open the service repository in VS code"""
        sporc_controller.open_vscode(service_spoken)

    def sporc_change_directory(service_spoken: str):
        """Open the service repository in terminal"""
        sporc_controller.open_repo_directory(service_spoken)
