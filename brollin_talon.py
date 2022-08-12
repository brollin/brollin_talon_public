from talon import Module, Context, ui, ctrl, canvas, screen, actions, clip
from talon.skia import Paint, Image
import json

mod = Module()
ctx = Context()


screen = ui.screens()[0]
talon_awake = True


def draw(canvas):
    canvas.paint.color = "008f00" if talon_awake else "8f0000"
    canvas.paint.style = Paint.Style.FILL
    canvas.draw_rect(ui.Rect(screen.width / 3, 0, screen.width / 3, 4))


mcanvas = canvas.Canvas.from_screen(screen)
mcanvas.register("draw", draw)
mcanvas.freeze()


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
        global talon_awake
        talon_awake = True if toggle == 1 else False
        mcanvas.unregister("draw", draw)
        mcanvas.register("draw", draw)
        mcanvas.freeze()
