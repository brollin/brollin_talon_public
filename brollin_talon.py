from typing import Dict
from talon import Module, Context, ui, ctrl, canvas, screen, actions, clip, noise
from talon.skia import Paint, Image
import json

mod = Module()
ctx = Context()


def testing_pop(active):
    print("Heard pop")


def testing_hiss(active):
    print("Heard hiss")


# noise.register("pop", testing_pop)
# noise.register("hiss", testing_hiss)


class BrollinOverlay:
    talon_awake = True
    screen = ui.screens()[0]
    sound_to_action = {}

    def __init__(self) -> None:
        self.mcanvas = canvas.Canvas.from_screen(self.screen)
        self.mcanvas.register("draw", self.draw)
        self.mcanvas.freeze()

    def draw(self, canvas):
        canvas.paint.textsize = 16
        canvas.paint.text_align = canvas.paint.TextAlign.CENTER
        text = "      ".join(
            ": ".join(key_value) for key_value in self.sound_to_action.items()
        )
        text_rectangle = canvas.paint.measure_text(text)[1].inset(-4)

        bar_rectangle = ui.Rect(
            self.screen.width / 3,
            0,
            self.screen.width / 3,
            text_rectangle.height if len(self.sound_to_action) else 7,
        )

        def draw_bar():
            canvas.paint.color = "008f00" if self.talon_awake else "8f0000"
            canvas.paint.style = Paint.Style.FILL
            canvas.draw_rect(bar_rectangle)

        def draw_text():
            if not len(self.sound_to_action):
                return

            canvas.paint.color = "ffffff"
            canvas.draw_text(
                text,
                self.screen.width / 2,
                text_rectangle.height * 3 / 4,
            )

        draw_bar()
        draw_text()

    def redraw(self):
        self.mcanvas.unregister("draw", self.draw)
        self.mcanvas.register("draw", self.draw)
        self.mcanvas.freeze()

    def set_awake(self, awake=True):
        self.talon_awake = awake
        self.redraw()

    def set_sound_to_action(self, sound_to_action: Dict):
        self.sound_to_action = sound_to_action
        self.redraw()


brollin_overlay = BrollinOverlay()


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

    def show_talon_overlay(toggle: int):
        """Show an overlay indicating whether talon is awake"""
        brollin_overlay.set_awake(True if toggle == 1 else False)

    def toggle_talon():
        """Toggle talon on or off"""
        if not actions.speech.enabled():
            actions.user.wake_talon()
        else:
            actions.user.sleep_talon()

    def sleep_talon():
        """Turn talon off"""
        actions.speech.disable()
        actions.user.show_talon_overlay(0)

    def wake_talon():
        """Turn talon on"""
        actions.speech.enable()
        actions.user.show_talon_overlay(1)
