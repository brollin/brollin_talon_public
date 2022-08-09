from talon import Module, Context, ui, ctrl, canvas, screen, actions
from dataclasses import dataclass
from talon.skia import Paint, Image
from talon.types import point

mod = Module()
mod.list("conquest_cardinal", desc="cardinal directions for songs of conquest movement")
mod.tag(
    "conquest_grid_activated", desc="Tag indicates whether the conquest grid is showing"
)
ctx = Context()
ctx.lists["user.conquest_cardinal"] = [
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
]

GRID_WIDTH = 90
GRID_HEIGHT = 75


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
        self.x += column * GRID_WIDTH
        self.y += row * GRID_HEIGHT


id_to_position = {}
position_to_id = {}
id_index1 = 0
id_index2 = 0
for row in range(-4, 5):
    for col in range(-4, 5):
        id_to_position[grid_letters[id_index1] + grid_letters[id_index2]] = (row, col)
        position_to_id[(row, col)] = grid_letters[id_index1] + grid_letters[id_index2]

        id_index2 = (id_index2 + 1) % len(grid_letters)
        if id_index2 == 0:
            id_index1 += 1


class ConquestController:
    def __init__(self):
        self.active = False
        self.board_size = 0
        self.mcanvas = None
        self.rect = None
        self.screen = None
        self.show_text = True
        self.visible = False

    def setup(self, *, rect: ui.Rect = None, visible: bool = True):
        self.screen = ui.screens()[0]

        # temp
        if rect is not None:
            self.rect = rect
            self.board_size = rect.height
            self.square_size = self.board_size // 8

        if rect is not None:
            self.rect = rect

        if self.mcanvas is None:
            self.mcanvas = canvas.Canvas.from_screen(self.screen)
        else:
            self.mcanvas.unregister("draw", self.draw_world_grid)

        if visible:
            self.mcanvas.register("draw", self.draw_world_grid)
            self.mcanvas.freeze()
            self.visible = True
        self.active = True

    def show(self):
        if self.visible:
            return
        self.mcanvas.register("draw", self.draw_world_grid)
        self.mcanvas.freeze()
        self.visible = True

    def hide(self):
        if not self.visible:
            return
        self.mcanvas.unregister("draw", self.draw_world_grid)
        self.visible = False

    def close(self):
        if not self.active:
            return
        self.mcanvas.unregister("draw", self.draw_world_grid)
        self.mcanvas.close()
        self.mcanvas = None
        self.visible = False
        self.active = False

    def draw_world_grid(self, canvas):
        paint = canvas.paint

        def draw_grid():
            pass
            # for i in range(9):
            #     canvas.draw_line(
            #         self.rect.x + i * self.square_size,
            #         self.rect.y,
            #         self.rect.x + i * self.square_size,
            #         self.rect.y + 8 * self.square_size,
            #     )
            #     canvas.draw_line(
            #         self.rect.x,
            #         self.rect.y + i * self.square_size,
            #         self.rect.x + 8 * self.square_size,
            #         self.rect.y + i * self.square_size,
            #     )

        def draw_text():
            canvas.paint.text_align = canvas.paint.TextAlign.CENTER
            for row in range(-4, 5):
                for col in range(-4, 5):
                    text_string = position_to_id[(row, col)]
                    text_rect = canvas.paint.measure_text(text_string)[1]
                    background_rect = text_rect.copy()
                    position = Position(self.screen.width / 2, self.screen.height / 2)
                    background_rect.center = point.Point2d(
                        position.x + col * GRID_WIDTH,
                        position.y + row * GRID_HEIGHT,
                    )
                    background_rect = background_rect.inset(-2)
                    paint.color = "9999996f"
                    paint.style = Paint.Style.FILL
                    canvas.draw_rect(background_rect)

                    paint.color = "ffff00bf"
                    canvas.draw_text(
                        text_string,
                        position.x + col * GRID_WIDTH,
                        position.y + row * GRID_HEIGHT + text_rect.height / 4,
                    )

        paint.stroke_width = 1
        paint.color = "ff0000ff"
        draw_grid()

        paint.textsize = 16
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


conquest_controller = ConquestController()


@mod.action_class
class ConquestActions:
    def conquest_grid_activate():
        """Activate the grid"""
        rect = ui.Rect(100, 100, 1000, 1000)
        conquest_controller.setup(rect=rect)
        ctx.tags = ["user.conquest_grid_activated"]

    def conquest_grid_show():
        """Show the grid"""
        conquest_controller.show()

    def conquest_grid_hide():
        """Hide the grid while remaining activated"""
        conquest_controller.hide()

    def conquest_grid_close():
        """Close the active grid"""
        ctx.tags = []
        conquest_controller.close()

    def conquest_cardinal_move_1d(direction: str, magnitude: int, mode: str):
        """Move mouse in one dimension"""
        conquest_controller.go_cardinal(direction, magnitude, mode=mode)

    def conquest_cardinal_move_2d(
        direction: str, magnitude: int, direction2: str, magnitude2: int, mode: str
    ):
        """Move mouse in two dimensions"""
        conquest_controller.go_cardinal(
            direction, magnitude, direction2, magnitude2, mode=mode
        )

    def conquest_id_move(letter1: str, letter2: str):
        """Move to a square by id"""
        conquest_controller.go_to_id(letter1 + letter2)
