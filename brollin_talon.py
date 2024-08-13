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

mode_color = {
    "sleep": "8f0000",
    "command": "008f00",
    "mixed": "00008f",
    "dictation": "8f008f",
}


class BrollinOverlay:
    talon_awake = True
    screen = ui.screens()[0]
    overlay_text = ""
    mode = "command"

    def __init__(self) -> None:
        self.mcanvas = canvas.Canvas.from_screen(self.screen)
        self.mcanvas.register("draw", self.draw)
        self.mcanvas.freeze()

    def draw(self, canvas):
        canvas.paint.textsize = 16
        canvas.paint.text_align = canvas.paint.TextAlign.CENTER

        text_rectangle = canvas.paint.measure_text(self.overlay_text)[1].inset(-4)

        bar_rectangle = ui.Rect(
            self.screen.width / 3,
            0,
            self.screen.width / 3,
            text_rectangle.height - 4 if len(self.overlay_text) else 7,
        )

        def draw_bar():
            canvas.paint.color = mode_color[self.mode]
            canvas.paint.style = Paint.Style.FILL
            canvas.draw_rect(bar_rectangle)

        def draw_text():
            if not len(self.overlay_text):
                return

            canvas.paint.color = "ffffff"
            canvas.draw_text(
                self.overlay_text,
                self.screen.width / 2,
                text_rectangle.height * 0.65,
            )

        draw_bar()
        draw_text()

    def redraw(self):
        self.mcanvas.unregister("draw", self.draw)
        self.mcanvas.register("draw", self.draw)
        self.mcanvas.freeze()

    def set_awake(self, awake=True):
        self.mode = "command" if awake else "sleep"
        self.redraw()

    def set_mode(self, mode):
        self.mode = mode
        self.redraw()

    def set_overlay_text(self, new_text: str):
        self.overlay_text = new_text
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
        brollin_overlay.set_awake(False)

    def wake_talon():
        """Turn talon on"""
        actions.speech.enable()
        brollin_overlay.set_awake(True)

    def set_talon_mode_color(mode: str):
        """Set talon mode color"""
        brollin_overlay.set_mode(mode)

    def open_file_in_vscode(path: str):
        """Open a given file path with VSCode"""
        command = "open -a 'Visual Studio Code' " + path
        actions.user.system_command_nb(command)

    def open_path_with_default_program(path: str):
        """Open path with default program"""
        actions.user.system_command_nb("open " + path)
