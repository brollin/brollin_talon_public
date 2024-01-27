import time
import typing
from talon import Module, Context, ui, ctrl, canvas, screen, actions
from talon.skia import Paint, Image
from talon.types import point

mod = Module()
ctx = Context()


class SpireController:
    mcanvas = None
    screen = None
    visible = False

    enemies = []

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
        paint.textsize = 20
        canvas.paint.text_align = canvas.paint.TextAlign.CENTER
        for label, position in self.label_to_position.items():
            text = label
            enemy = False
            if label in self.label_to_enemy:
                text = str(self.label_to_enemy[label]) + ": " + label
                enemy = True
            text_rect = canvas.paint.measure_text(text)[1]
            background_rect = text_rect.copy()
            background_rect.center = point.Point2d(
                position.x,
                position.y,
            )
            background_rect = background_rect.inset(-2)
            paint.color = "9999996f"
            paint.style = Paint.Style.FILL
            canvas.draw_rect(background_rect)

            paint.color = "ffff00bf" if not enemy else "ff0000bf"
            canvas.draw_text(
                text,
                position.x,
                position.y + text_rect.height / 4,
            )

    def remap_enemies(self):
        import urllib.request
        import json

        monster_data = json.loads(
            urllib.request.urlopen("http://localhost:10463/monsters").read()
        )

        # flip the y coordinates
        for monster in monster_data["monsters"]:
            monster["y"] = self.screen.height - monster["y"]

        self.enemies = monster_data["monsters"]

    def go_to_enemy(self, enemy_number: int):
        if len(self.enemies) < enemy_number:
            print(f"enemy #{enemy_number} not found")
            return

        enemy = self.enemies[enemy_number - 1]

        ctrl.mouse_move(enemy["x"], enemy["y"])


spire_controller = SpireController()


@mod.action_class
class SpireActions:
    def spire_item(number: str):
        """Mouseover an item/potion"""
        ctrl.mouse_move(775 + 72 * int(number), 50)

    def spire_relic(number: str):
        """Mouseover a relic"""
        ctrl.mouse_move(-20 + 96 * int(number), 140)

    def spire_enemy(number: int, click: int = -1):
        """Mouseover an enemy"""
        spire_controller.go_to_enemy(number)
        if click >= 0:
            time.sleep(0.1)
            ctrl.mouse_click(button=click, down=True)
            time.sleep(0.1)
            ctrl.mouse_click(button=click, down=False)

    def spire_remap_enemies():
        """Remap all enemies"""
        spire_controller.remap_enemies()
        spire_controller.go_to_enemy(1)

    def spire_activate_grid():
        """Activate grid for mapping enemies"""
        spire_controller.setup(visible=True)

    def spire_close_grid():
        """Close grid for mapping enemies"""
        spire_controller.close()

    def spire_handle_bug():
        """Handle an annoying bug"""
        ctrl.mouse_move(1973.0, 1359.0)
        time.sleep(0.1)
        ctrl.mouse_move(2073, 1359.0)
        time.sleep(0.1)
        ctrl.mouse_move(2073, 1200)
        time.sleep(0.1)
        spire_controller.go_to_enemy(1)

    def spire_go_to_booty():
        """Go to the first loot item"""
        ctrl.mouse_move(1719.0, 560.0)

    def spire_shop_item(number: int):
        """Go to the specified shop item"""
        if number <= 3:
            ctrl.mouse_move(1760.0 + 250 * (number - 1), 908.0)
        else:
            ctrl.mouse_move(1760.0 + 250 * (number - 4), 908.0 + 300)

    def spire_use_item():
        """Use the shop item"""
        x, y = ctrl.mouse_pos()
        ctrl.mouse_click(button=0)
        time.sleep(0.1)
        ctrl.mouse_move(x, y + 200)
        time.sleep(0.1)
        ctrl.mouse_click(button=0)
