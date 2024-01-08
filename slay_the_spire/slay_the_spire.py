import time
import typing
from talon import Module, Context, ui, ctrl, canvas, screen, actions
from talon.skia import Paint, Image
from talon.types import point

mod = Module()
ctx = Context()

enemy_profiles = {
    "slimes": {1: "li", 2: "ln"},
    "fungi": {1: "lg", 2: "lm"},
    "gremlin": {1: "jg", 2: "jj", 3: "jn"},
    "bronze": {1: "gh", 2: "gl", 3: "hr"},
    "jaws": {1: "ld", 2: "lj", 3: "lr"},
    "reptile": {1: "ii", 2: "im", 3: "ir"},
    "collector": {1: "id", 2: "ih", 3: "in"},
}


class SpireController:
    mcanvas = None
    screen = None
    visible = False
    label_to_position = {}
    enemy_to_label = {}
    label_to_enemy = {}

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

        self.setup_grid()

    def setup_grid(self):
        letters = [
            "a",
            "b",
            "c",
            "d",
            "g",
            "h",
            "i",
            "j",
            "l",
            "m",
            "n",
            "p",
            "r",
            "t",
            "w",
            "y",
        ]
        for row in range(12):
            for col in range(15):
                label = letters[row] + letters[col]
                self.label_to_position[label] = point.Point2d(
                    self.screen.width / 2 - 400 + col * 135,
                    self.screen.height / 4 + row * 68,
                )

    def map_enemy(self, enemy_string: str, label_parts: typing.List[str]):
        enemy = int(enemy_string)
        label = "".join(label_parts)
        if label not in self.label_to_position.keys():
            print(f"could not find label {label}")
            return

        if (
            enemy in self.enemy_to_label
            and self.enemy_to_label[enemy] in self.label_to_enemy
        ):
            del self.label_to_enemy[self.enemy_to_label[enemy]]
        self.enemy_to_label[enemy] = label
        self.label_to_enemy[label] = enemy
        self.redraw()

    def auto_map(self, profile_number: int):
        if profile_number == 1:
            self.enemy_to_label = {1: "im"}
        elif profile_number == 2:
            self.enemy_to_label = {1: "lj", 2: "ln"}
        elif profile_number == 3:
            self.enemy_to_label = {1: "lh", 2: "ll", 3: "ln"}
        elif profile_number == 4:
            self.enemy_to_label = {1: "lh", 2: "lj", 3: "lm", 4: "lr"}
        elif profile_number == 5:
            self.enemy_to_label = {1: "ld", 2: "lh", 3: "lj", 4: "mm", 5: "lr"}
        elif profile_number == 6:
            self.enemy_to_label = {1: "jg", 2: "jj", 3: "jp"}

        # reverse the mapping
        self.label_to_enemy = {v: k for k, v in self.enemy_to_label.items()}

        self.redraw()
        self.go_to_enemy(1)

    def auto_map_by_text(self, profile: str):
        global enemy_profiles
        if profile in enemy_profiles:
            self.enemy_to_label = enemy_profiles[profile]

        # reverse the mapping
        self.label_to_enemy = {v: k for k, v in self.enemy_to_label.items()}

        self.redraw()
        self.go_to_enemy(1)

    def clear_enemies(self):
        self.enemy_to_label = {}
        self.label_to_enemy = {}
        self.redraw()

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

    def go_to_enemy(self, enemy: int):
        print(self.enemy_to_label)
        print(self.label_to_enemy)
        if enemy not in self.enemy_to_label:
            print(f"enemy {enemy} not found")
            return
        position = self.label_to_position[self.enemy_to_label[enemy]]
        ctrl.mouse_move(position.x, position.y)


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

    def spire_map_enemy(enemy_and_label: typing.List[str]):
        """Map an enemy location"""
        # if len(enemy_and_label) % 3 == 0:
        #     for i in range(0, len(enemy_and_label), 3):
        #         print(i)
        #         spire_controller.map_enemy(
        #             enemy_and_label[i], enemy_and_label[i + 1 : i + 3]
        #         )

        if len(enemy_and_label) % 2 == 0:
            for i in range(0, len(enemy_and_label), 2):
                spire_controller.map_enemy((i // 2) + 1, enemy_and_label[i : i + 2])
        spire_controller.close()
        spire_controller.go_to_enemy(1)

    def spire_clear_enemies():
        """Clear all enemies"""
        spire_controller.clear_enemies()

    def spire_remap_enemies():
        """Remap all enemies"""
        spire_controller.clear_enemies()
        spire_controller.setup(visible=True)

    def spire_activate_grid():
        """Activate grid for mapping enemies"""
        spire_controller.setup(visible=True)

    def spire_auto_map(number: int):
        """Auto map enemies"""
        spire_controller.auto_map(number)

    def spire_auto_map_by_text(profile: str):
        """Auto map enemies"""
        spire_controller.auto_map_by_text(profile)

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
