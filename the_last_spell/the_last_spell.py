from talon import Module, Context, ui, ctrl, canvas, screen, actions
from dataclasses import dataclass
from talon.skia import Paint, Image
from talon.types import point
import time

mod = Module()
mod.list("spell_cardinal", desc="cardinal directions for songs of spell movement")
mod.tag("spell_grid_activated", desc="Tag indicates whether the spell grid is showing")
ctx = Context()
ctx.lists["user.spell_cardinal"] = [
    "north",
    "west",
    "south",
    "east",
]

grid_letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "k",
    "l",
    "m",
    "n",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "w",
    "y",
    "z",
]

GRID_WIDTH = 112
GRID_HEIGHT = 84
# number of rose and columns. cannot be more than the length of the grid_letters array
GRID_SIZE = 10


@dataclass
class Position:
    x: int
    y: int

    def translate(self, delta_x: int, delta_y: int):
        self.x += delta_x
        self.y += delta_y

    def cardinal_translate(self, direction: str, magnitude: int):
        delta_x = 0
        delta_y = 0
        if direction == "north":
            delta_y = -magnitude * GRID_HEIGHT
        elif direction == "south":
            delta_y = magnitude * GRID_HEIGHT
        elif direction == "west":
            delta_x = -magnitude * GRID_WIDTH
        elif direction == "east":
            delta_x = magnitude * GRID_WIDTH

        self.translate(delta_x, delta_y)

    def grid_translate(self, row, column):
        self.x += row * -GRID_WIDTH // 2 + column * GRID_WIDTH // 2
        self.y += row * -GRID_HEIGHT // 2 - column * GRID_HEIGHT // 2


# initialize id_to_position, position_to_id dictionaries
id_to_position = {}
position_to_id = {}
row_letter_index = -1
for row in range(-GRID_SIZE, GRID_SIZE + 1):
    row_letter_index += 1
    column_letter_index = -1
    for col in range(-GRID_SIZE, GRID_SIZE + 1):
        column_letter_index += 1
        id = grid_letters[row_letter_index] + grid_letters[column_letter_index]
        id_to_position[id] = (row, col)
        position_to_id[(row, col)] = id


class SpellController:
    def __init__(self):
        self.active = False
        self.mcanvas = None
        self.rect = None
        self.screen = None
        self.show_text = True
        self.visible = False

    def setup(self, *, rect: ui.Rect = None, visible: bool = True):
        self.screen = ui.screens()[0]

        if rect is not None:
            self.rect = rect

        if self.mcanvas is None:
            self.mcanvas = canvas.Canvas.from_screen(self.screen)
        else:
            self.mcanvas.unregister("draw", self.draw_isometric_grid)

        if visible:
            self.mcanvas.register("draw", self.draw_isometric_grid)
            self.mcanvas.freeze()
            self.visible = True
        self.active = True

    def show(self):
        if self.visible:
            return
        self.mcanvas.register("draw", self.draw_isometric_grid)
        self.mcanvas.freeze()
        self.visible = True

    def hide(self):
        if not self.visible:
            return
        self.mcanvas.unregister("draw", self.draw_isometric_grid)
        self.visible = False

    def close(self):
        if not self.active:
            return
        self.mcanvas.unregister("draw", self.draw_isometric_grid)
        self.mcanvas.close()
        self.mcanvas = None
        self.visible = False
        self.active = False

    def draw_isometric_grid(self, canvas):
        paint = canvas.paint

        def draw_grid():
            pass

        def draw_text():
            canvas.paint.text_align = canvas.paint.TextAlign.CENTER
            for row in range(-GRID_SIZE, GRID_SIZE + 1):
                for col in range(-GRID_SIZE, GRID_SIZE + 1):
                    position = Position(self.screen.width / 2, self.screen.height / 2)
                    position.grid_translate(row, col)

                    text_string = position_to_id[(row, col)]
                    text_rect = canvas.paint.measure_text(text_string)[1]

                    background_rect = text_rect.copy()
                    background_rect.center = point.Point2d(position.x, position.y)
                    background_rect.width -= 2
                    background_rect.height -= 1
                    background_rect.x += 1

                    paint.color = "000000ff"
                    paint.style = Paint.Style.FILL
                    canvas.draw_rect(background_rect)

                    paint.color = "bfbf00ff"
                    canvas.draw_text(
                        text_string,
                        position.x,
                        position.y + text_rect.height / 4,
                    )

        paint.stroke_width = 1
        paint.color = "ff0000ff"
        draw_grid()

        paint.textsize = 13
        if self.show_text:
            draw_text()

    def go_cardinal(
        self, direction: str, magnitude: int, direction2="", magnitude2=0, mode=""
    ):
        if mode == "relative":
            position = Position(actions.mouse_x(), actions.mouse_y())
        else:
            position = Position(self.screen.width / 2, self.screen.height / 2)

        position.cardinal_translate(direction, magnitude)
        if direction2 != "":
            position.cardinal_translate(direction2, magnitude2)

        ctrl.mouse_move(position.x, position.y)
        # if click >= 0:
        #     time.sleep(0.1)
        #     ctrl.mouse_click(button=click, down=True)
        #     time.sleep(0.1)
        #     ctrl.mouse_click(button=click, up=True)

    def go_to_id(self, id):
        (row, column) = id_to_position[id]
        position = Position(self.screen.width / 2, self.screen.height / 2)
        position.grid_translate(row, column)
        ctrl.mouse_move(position.x, position.y)


spell_controller = SpellController()


@mod.action_class
class SpellActions:
    def spell_grid_activate():
        """Activate the grid"""
        rect = ui.Rect(100, 100, 1000, 1000)
        spell_controller.setup(rect=rect)
        ctx.tags = ["user.spell_grid_activated"]

    def spell_grid_show():
        """Show the grid"""
        spell_controller.show()

    def spell_grid_hide():
        """Hide the grid while remaining activated"""
        spell_controller.hide()

    def spell_grid_close():
        """Close the active grid"""
        ctx.tags = []
        spell_controller.close()

    def spell_id_move(letter1: str, letter2: str, mouse_button: int):
        """Move to a square by id"""
        spell_controller.go_to_id(letter1 + letter2)
        if mouse_button > -1:
            time.sleep(0.05)
            ctrl.mouse_click(button=mouse_button, down=True)
            time.sleep(0.05)
            ctrl.mouse_click(button=mouse_button, up=True)

    def spell_double_click():
        """Perform a double click"""
        ctrl.mouse_click(button=0, down=True)
        time.sleep(0.05)
        ctrl.mouse_click(button=0, up=True)
        time.sleep(0.05)
        ctrl.mouse_click(button=0, down=True)
        time.sleep(0.05)
        ctrl.mouse_click(button=0, up=True)

    # unused commands below

    def spell_cardinal_move_1d(direction: str, magnitude: int, mode: str):
        """Move mouse in one dimension"""
        spell_controller.go_cardinal(direction, magnitude, mode=mode)

    def spell_cardinal_move_2d(
        direction: str, magnitude: int, direction2: str, magnitude2: int, mode: str
    ):
        """Move mouse in two dimensions"""
        spell_controller.go_cardinal(
            direction, magnitude, direction2, magnitude2, mode=mode
        )
