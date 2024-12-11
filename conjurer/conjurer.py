from talon import Module, Context, app
import json
from websockets.sync.client import connect

mod = Module()
mod.list(
    "conjurer_action",
    desc="List of all conjurer actions without arguments",
)
mod.list(
    "conjurer_action_with_args",
    desc="List of all conjurer actions with arguments",
)


ctx = Context()
ctx.lists["user.conjurer_action"] = {
    "play": "togglePlay",
    "pause": "togglePlay",
    "go to beginning": "goToBeginning",
    "go to begin": "goToBeginning",
    "beginning": "goToBeginning",
    "begin": "goToBeginning",
    "go to end": "goToEnd",
    "zoom in": "zoomIn",
    "zoom out": "zoomOut",
    "experience copy": "copyExperience",
}
ctx.lists["user.conjurer_action_with_args"] = {
    "layer": "selectLayer",
    "go": "goToTime",
    "move": "moveBlockForwardRelative",
    "move back": "moveBlockBackwardRelative",
    "put": "moveBlockAbsolute",
    "extend": "extendBlockRelative",
    "shrink": "shrinkBlockRelative",
    "extend until": "extendBlockAbsolute",
}


def send_action_message(action: str, *, value: bool | int | str | None = None):
    with connect("ws://127.0.0.1:5174") as websocket:
        # will wait 5 seconds for the server to close the connection normally
        websocket.close_timeout = 0.01
        websocket.send(
            json.dumps(
                {
                    "type": "action",
                    "appId": "conjurer",
                    "action": action,
                    "value": value,
                }
            )
        )


@mod.action_class
class ConjurerActions:
    def conjurer_send_action_with_args(action: str, value_type: str, value: int | str):
        """Send action message with arguments to conjurer app"""
        if value_type == "int":
            send_action_message(action, value=int(value))
        elif value_type == "str":
            send_action_message(action, value=str(value))
        elif value_type == "bool":
            send_action_message(action, value=True if value else False)

    def conjurer_send_action(action: str):
        """Send action message to conjurer app"""
        # app.notify(f"action: {action}")
        send_action_message(action)
