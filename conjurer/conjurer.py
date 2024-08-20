from talon import Module, Context, app
import json
from websockets.sync.client import connect

mod = Module()
# mod.list(
#     "tracker_target",
#     desc="List of all tracker targets",
# )
# mod.list(
#     "tracker_day",
#     desc="List of terms that can select a day",
# )

# target_types = [
#     {"key": "vitamins", "aliases": [], "type": "bool"},
#     {"key": "dragonBook", "aliases": ["dragon", "dragon book"], "type": "bool"},
#     {"key": "craftBook", "aliases": ["craft", "craft book"], "type": "bool"},
#     {"key": "healthWork", "aliases": ["health"], "type": "bool"},
#     {"key": "walk", "aliases": [], "type": "bool"},
#     {"key": "somatics", "aliases": [], "type": "bool"},
#     {"key": "shower", "aliases": [], "type": "bool"},
#     {"key": "fruit", "aliases": [], "type": "bool"},
#     {"key": "journal", "aliases": [], "type": "bool"},
#     {"key": "mood", "aliases": [], "type": "int"},
#     {"key": "pain", "aliases": [], "type": "int"},
#     {"key": "nonStandardSitting", "aliases": ["sitting"], "type": "int"},
#     {"key": "walking", "aliases": [], "type": "int"},
#     {"key": "wakeTime", "aliases": ["wake", "wake time"], "type": "int"},
#     {"key": "sleepTime", "aliases": ["sleep", "sleep time"], "type": "int"},
#     {
#         "key": "disruptedTime",
#         "aliases": ["disrupted", "disrupted time", "disrupt"],
#         "type": "int",
#     },
#     {"key": "notes", "aliases": [], "type": "str"},
# ]

# target_map = {}
# for target_type in target_types:
#     target_map[target_type["key"]] = target_type["key"]
#     for alias in target_type["aliases"]:
#         target_map[alias] = target_type["key"]

ctx = Context()
# ctx.lists["user.tracker_target"] = target_map
# ctx.lists["user.tracker_day"] = {
#     "today": "today",
#     "yesterday": "yesterday",
#     "tomorrow": "tomorrow",
#     # "next": "next",
#     # "last": "last",
#     "Sunday": "Sunday",
#     "Monday": "Monday",
#     "Tuesday": "Tuesday",
#     "Wednesday": "Wednesday",
#     "Thursday": "Thursday",
#     "Friday": "Friday",
#     "Saturday": "Saturday",
# }


def send_action_message(
    action: str, *, target: str = "", value: bool | int | str | None = None
):
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
                    "target": target,
                }
            )
        )


@mod.action_class
class ConjurerActions:
    def conjurer_send_action_with_args(
        action: str, target: str, value_type: str, value: int | str
    ):
        """Send action message with arguments to conjurer app"""
        if value_type == "int":
            send_action_message(action, target=target, value=int(value))
        elif value_type == "str":
            send_action_message(action, target=target, value=str(value))
        elif value_type == "bool":
            send_action_message(action, target=target, value=True if value else False)

    def conjurer_send_action(action: str, value: str):
        """Send action message to conjurer app"""
        app.notify(f"action: {action}, value: {value}")
        send_action_message(action, value=value)
