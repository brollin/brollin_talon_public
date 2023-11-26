from talon import Module, Context, ctrl, actions
import time

from ..brollin_talon import brollin_overlay

mod = Module()
mod.list("parrot_sound", desc="List of all parrot sounds")


@mod.capture(
    rule="( <self.any_alphanumeric_key> | click | right click | nothing | second | enter )"
)
def alphanumeric_or_action(m) -> str:
    "any alphanumeric key"
    return str(m)


ctx = Context()
ctx.lists["user.parrot_sound"] = {"tongue": "tongue_click", "caveman": "caveman"}

sound_to_action = {}

profiles = {
    "second": {"tongue_click": "second"},
    "scroller": {"tongue_click": "scroll", "caveman": "switch_direction"},
}

scroll_direction = 1

DEBUG = False


@mod.action_class
class ParrotActions:
    def do_mapped_parrot_action(sound: str):
        """Do the currently assigned parrot action"""
        global scroll_direction
        action = "<unassigned>"
        if sound in sound_to_action:
            action = sound_to_action[sound]
            if len(action) == 1:
                actions.key(action)
            elif "click" in action:
                button = 1 if "right" in action else 0
                ctrl.mouse_click(button=button, down=True)
                time.sleep(0.1)
                ctrl.mouse_click(button=button, up=True)
            elif "second" in action:
                actions.core.repeat_command()
            elif "scroll" in action:
                actions.mouse_scroll(y=100 * scroll_direction)
            elif "switch_direction" in action:
                scroll_direction *= -1
            else:
                actions.key(action)

        if DEBUG == True:
            print(f"DOING    parrot({sound}): {action}")

    def assign_parrot_action(sound: str, action: str):
        """Assign a parrot action"""
        global sound_to_action
        if "nothing" in action and sound == "all":
            sound_to_action = {}
            action = "<unassigned>"
        elif "nothing" in action and sound in sound_to_action:
            del sound_to_action[sound]
            action = "<unassigned>"
        else:
            sound_to_action[sound] = action

        print(f"ASSIGNED parrot({sound}): {action}")
        brollin_overlay.set_sound_to_action(sound_to_action)

    def unassign_parrot_action(sound: str):
        """Unassign a parrot action"""
        actions.user.assign_parrot_action(sound, "nothing")

    def set_parrot_profile(profile: str):
        """Set a parrot profile"""
        if profile not in profiles:
            print("profile not found")
            return

        global sound_to_action
        sound_to_action = profiles[profile]
        brollin_overlay.set_sound_to_action(sound_to_action)
