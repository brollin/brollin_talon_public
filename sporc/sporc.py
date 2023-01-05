import time
import typing
from talon import Module, Context, ui, ctrl, canvas, screen, actions
from .services import services

mod = Module()
ctx = Context()

mod.list(
    "service",
    desc="A service with endpoints",
)
ctx.lists["self.service"] = {key: key for key in services}


class SporcController:
    def service_text(self, service_spoken: str) -> str:
        return services[service_spoken]["domains"]["prod"]


sporc_controller = SporcController()


@mod.action_class
class SporcActions:
    def sporc_service_text(service_spoken: str) -> str:
        """Type the text of a service's default endpoint"""
        return sporc_controller.service_text(service_spoken)
