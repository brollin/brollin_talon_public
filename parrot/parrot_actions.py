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


profiles = {
    "zoomer": {"tongue_click": "second"},
    "scroller": {"tongue_click": "scroll"},
}


DEBUG = False


class Parrot:
    profile = ""
    scroll_direction = 1

    sound_to_action = {}

    def get_profile_overlay_text(self) -> str:
        if self.profile == "zoomer":
            return "zoomer"
        elif self.profile == "scroller":
            return "scroller" + (" (down)" if self.scroll_direction == 1 else " (up)")

        return self.profile


parrot = Parrot()


@mod.action_class
class ParrotActions:
    def do_mapped_parrot_action(sound: str):
        """Do the currently assigned parrot action"""
        action = "<unassigned>"
        if sound in parrot.sound_to_action:
            action = parrot.sound_to_action[sound]
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
                actions.mouse_scroll(y=150 * parrot.scroll_direction)
            else:
                actions.key(action)

        if DEBUG == True:
            print(f"DOING    parrot({sound}): {action}")

    def assign_parrot_action(sound: str, action: str):
        """Assign a parrot action"""
        if "nothing" in action and sound == "all":
            parrot.sound_to_action = {}
            action = "<unassigned>"
        elif "nothing" in action and sound in parrot.sound_to_action:
            del parrot.sound_to_action[sound]
            action = "<unassigned>"
        else:
            parrot.sound_to_action[sound] = action

        print(f"ASSIGNED parrot({sound}): {action}")

        text = "      ".join(
            ": ".join(key_value) for key_value in parrot.sound_to_action.items()
        )
        brollin_overlay.set_overlay_text(text)

    def unassign_parrot_action(sound: str):
        """Unassign a parrot action"""
        actions.user.assign_parrot_action(sound, "nothing")

    def set_parrot_profile(profile: str):
        """Set a parrot profile"""
        if profile not in profiles:
            print("profile not found")
            return

        parrot.profile = profile
        parrot.sound_to_action = profiles[profile]

        brollin_overlay.set_overlay_text(parrot.get_profile_overlay_text())

    def parrot_special_action(action: str):
        """Do a special parrot action"""
        if action == "flip":
            parrot.scroll_direction *= -1
            brollin_overlay.set_overlay_text(parrot.get_profile_overlay_text())
