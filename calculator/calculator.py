import time
import typing
from talon import Module, Context, ui, ctrl, cron, canvas, screen, actions
from talon.skia import Paint, Image
from talon.types import point

mod = Module()
mod.list(
    "calculator_operation",
    desc="List of all supported mathematical calculator operations",
)

ctx = Context()
ctx.lists["user.calculator_operation"] = {
    "plus": "+",
    "minus": "-",
    "times": "*",
    "divided by": "/",
}


previous_result = None


class CalculatorController:
    mcanvas = None
    screen = None
    visible = False

    def __init__(self) -> None:
        self.setup(visible=False)

    def setup(self, *, visible: bool = True):
        self.screen = ui.screens()[0]

        if self.mcanvas is None:
            self.mcanvas = canvas.Canvas.from_screen(self.screen)
        else:
            self.mcanvas.unregister("draw", self.draw)

        if visible:
            self.mcanvas.register("draw", self.draw)
            self.mcanvas.freeze()
            self.visible = True

    def show(self):
        if self.visible:
            return
        self.mcanvas.register("draw", self.draw)
        self.mcanvas.freeze()
        self.visible = True

    def hide(self):
        if not self.visible:
            return
        self.mcanvas.unregister("draw", self.draw)
        self.visible = False

    def close(self):
        if not self.visible:
            return
        self.mcanvas.unregister("draw", self.draw)
        self.mcanvas.close()
        self.mcanvas = None
        self.visible = False

    def redraw(self):
        if not self.visible:
            return
        self.mcanvas.unregister("draw", self.draw)
        self.mcanvas.register("draw", self.draw)
        self.mcanvas.freeze()

    def draw(self, canvas):
        paint = canvas.paint
        paint.stroke_width = 1
        paint.color = "ff0000ff"
        paint.textsize = 30
        canvas.paint.text_align = canvas.paint.TextAlign.CENTER

        text = f"{self.number1} {self.operation} {self.number2} = {self.result}"
        text_rect = canvas.paint.measure_text(text)[1]
        background_rect = text_rect.copy()
        background_rect.center = point.Point2d(
            self.screen.width / 2,
            self.screen.height / 2,
        )
        background_rect = background_rect.inset(-10)
        paint.color = "999999ff"
        paint.style = Paint.Style.FILL
        canvas.draw_rect(background_rect)

        paint.color = "0f42b5ff"
        canvas.draw_text(
            text,
            background_rect.center.x,
            background_rect.center.y + text_rect.height / 3,
        )

    def calculate(self, operation: str, number1: int, number2: int):
        # print(f"Calculating: {number1} {operation} {number2}")

        self.visible = True
        self.operation = operation
        self.number1 = number1
        self.number2 = number2
        self.result = eval(f"{number1} {operation} {number2}")
        self.redraw()
        cron.after("2s", self.hide)


calculator_controller = CalculatorController()


@mod.action_class
class CalculatorActions:
    def calculator_calculate(operation: str, number1: int, number2: int):
        """Perform a calculation"""
        calculator_controller.calculate(operation, number1, number2)
