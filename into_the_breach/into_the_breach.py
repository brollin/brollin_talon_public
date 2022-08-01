from talon import Module, Context, ui, ctrl
import time
import typing

mod = Module()
ctx = Context()

files = ["a", "b", "c", "d", "e", "f", "g", "h"]
ranks = ["1", "2", "3", "4", "5", "6", "7", "8"]

BOX_WIDTH = 220
BOX_HEIGHT = 8 / 11 * BOX_WIDTH

def coordinate_to_position(coordinate: typing.List[str]):
    screen = ui.screens()[0]
    center_x = screen.width / 2
    center_y = screen.height / 2

    column = files.index(coordinate[0])
    row = int(coordinate[1]) - 1

    a1_x = center_x
    a1_y = center_y + 3.5 * BOX_HEIGHT

    x = a1_x + column * 0.5 * BOX_WIDTH - row * 0.5 * BOX_WIDTH
    y = a1_y - column * 0.5 * BOX_HEIGHT - row * 0.5 * BOX_HEIGHT
    return (x, y)

class BreachGrid:
    def __init__(self):
        pass

    def go_to_tile(self, coordinates, click):
        x, y = coordinate_to_position(coordinates)
        ctrl.mouse_move(x, y)
        if click == "click":
            time.sleep(0.1)
            ctrl.mouse_click(button=0, down=True)
            time.sleep(0.1)
            ctrl.mouse_click(button=0, up=True)

bg = BreachGrid()

@mod.action_class
class ChessGridActions:
    def breach_go_to_tile(coordinates: typing.List[str], click: str):
        """Go to a square"""
        if len(coordinates) not in [2, 4]:
            return
        if not coordinates[0] in files \
            or not coordinates[1] in ranks \
            or len(coordinates) == 4 and \
            (not coordinates[2] in files
             or not coordinates[3] in ranks):
            return

        bg.go_to_tile(coordinates, click)
