from talon import Module, Context, ui, ctrl, actions
from dataclasses import dataclass

mod = Module()
mod.list('conquest_cardinal', desc='cardinal directions for songs of conquest movement')
ctx = Context()
ctx.lists['user.conquest_cardinal'] = [
    'north', 'west', 'south', 'east',
]

GRID_WIDTH = 90
GRID_HEIGHT = 80

@dataclass
class Position:
    x: int
    y: int

    def translate(self, delta_x: int, delta_y: int):
        self.x += delta_x
        self.y += delta_y

    def vector_translate(self, direction: str, magnitude: int):
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

class ConquestController:
    def go_cardinal(self, direction: str, magnitude: int, direction2="", magnitude2=0, mode=""):
        if mode == "relative":
            position = Position(actions.mouse_x(), actions.mouse_y())
        else:
            screen = ui.screens()[0]
            position = Position(screen.width / 2, screen.height / 2)

        position.vector_translate(direction, magnitude)
        if direction2 != "":
            position.vector_translate(direction2, magnitude2)

        ctrl.mouse_move(position.x, position.y)
        # if click >= 0:
        #     time.sleep(0.1)
        #     ctrl.mouse_click(button=click, down=True)
        #     time.sleep(0.1)
        #     ctrl.mouse_click(button=click, up=True)

conquest_controller = ConquestController()

@mod.action_class
class ConquestActions:
    def conquest_cardinal_move_1d(direction: str, magnitude: int, mode: str):
        """Move mouse in one dimension"""
        conquest_controller.go_cardinal(direction, magnitude, mode=mode)

    def conquest_cardinal_move_2d(direction: str, magnitude: int, direction2: str, magnitude2: int, mode: str):
        """Move mouse in two dimensions"""
        conquest_controller.go_cardinal(direction, magnitude, direction2, magnitude2, mode=mode)
