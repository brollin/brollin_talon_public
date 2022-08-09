from talon import Module, Context, ui, ctrl, canvas, screen, actions, clip
import json

mod = Module()
ctx = Context()


@mod.action_class
class BrollinActions:
    def copy_command_id():
        """Copy the command id of the focused menu item"""
        actions.key("tab:2 enter")
        actions.sleep("750ms")
        json_text = actions.edit.selected_text()
        command_id = json.loads(json_text)["command"]
        actions.app.tab_close()
        clip.set_text(command_id)
