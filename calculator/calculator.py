from math import comb
from talon import Module, Context, ui, ctrl, cron, canvas, screen, actions
from talon.skia import Paint, Image
from talon.types import point

mod = Module()
mod.list(
    "calculator_operation",
    desc="List of all supported mathematical calculator operations",
)
mod.list(
    "calculator_spire_operation",
    desc="List of all supported Slay the Spire calculator operations",
)

ctx = Context()
ctx.lists["user.calculator_operation"] = {
    "plus": "+",
    "minus": "-",
    "times": "*",
    "divided by": "/",
    "choose": "choose",
}
ctx.lists["user.calculator_spire_operation"] = {
    "weaken": "weaken",
    "vulnerable": "vulnerable",
    "both": "weaken and vulnerable",
    "super weaken": "super weaken",
}

spire_operation_factor = {
    "weaken": 0.75,
    "vulnerable": 1.5,
    "weaken and vulnerable": 9 / 8,
    "super weaken": 0.6,
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
        self.mcanvas.freeze()
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

        text = self.display_text
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
        if operation == "choose":
            self.result = comb(number1, number2)
        else:
            self.result = eval(f"{number1} {operation} {number2}")
        self.display_text = f"{number1} {operation} {number2} = {self.result}"

        self.visible = True
        self.redraw()

    def spire_calculate(self, operation: str, number1: int):
        self.result = spire_operation_factor[operation] * number1
        floored_result = int(self.result)
        self.display_text = f"{operation} {number1} = {self.result} = {floored_result}"

        self.visible = True
        self.redraw()


calculator_controller = CalculatorController()


@mod.action_class
class CalculatorActions:
    def calculator_calculate(operation: str, number1: int, number2: int):
        """Perform a calculation"""
        calculator_controller.calculate(operation, number1, number2)

    def calculator_spire_calculate(spire_operation: str, number1: int):
        """Perform a calculation"""
        calculator_controller.spire_calculate(spire_operation, number1)

    def calculator_hide():
        """Hide the calculator canvas"""
        calculator_controller.hide()
