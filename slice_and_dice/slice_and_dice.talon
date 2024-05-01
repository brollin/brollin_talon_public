os: mac
and app.bundle: com.tann.dice.desktop
-
north: user.mouse_cardinal_move_1d("up", 75)
^north <user.ordinals>$: user.mouse_cardinal_move_1d("up", 75 * ordinals)
^north <number> times$: user.mouse_cardinal_move_1d("up", 75 * number)
south: user.mouse_cardinal_move_1d("down", 75)
^south <user.ordinals>$: user.mouse_cardinal_move_1d("down", 75 * ordinals)
^south <number> times$: user.mouse_cardinal_move_1d("down", 75 * number)
west: user.mouse_cardinal_move_1d("left", 75)
^west <user.ordinals>$: user.mouse_cardinal_move_1d("left", 75 * ordinals)
^west <number> times$: user.mouse_cardinal_move_1d("left", 75 * number)
east: user.mouse_cardinal_move_1d("right", 75)
^east <user.ordinals>$: user.mouse_cardinal_move_1d("right", 75 * ordinals)
^east <number> times$: user.mouse_cardinal_move_1d("right", 75 * number)

invent: key(i)
end turn: key(space)
continue: key(enter)

word: skip()
phrase: skip()
say: skip()
hammer: skip()

# turn off repeater ordinals
<user.ordinals>: skip()

inventory [<number>]: user.flex_grid_go_to_point("inventory", number or 1, 1)
item [<number>]: user.flex_grid_go_to_point("item", number or 1, -1)
hero [<number>]: user.flex_grid_go_to_point("hero", number or 1, 1)
go hero [<number>]: user.flex_grid_go_to_point("hero", number or 1, -1)
click hero [<number>]: user.flex_grid_go_to_point("hero", number or 1, 0)
^ten$: user.flex_grid_go_to_point("hero", 10, 0)

put <number>:
    user.mouse_drag(0)
    sleep(0.1)
    user.flex_grid_go_to_point("inventory", number or 1, -1)
    sleep(0.1)
    user.mouse_drag_end()

<number> heroes:
    user.flex_grid_map_points_by_raw_location_range("hero", number, 163, 105, 163, 1185)
    user.flex_grid_points_toggle(0)

ten heroes:
    user.flex_grid_map_points_by_raw_location_range("hero", 10, 163, 105, 163, 1185)
    user.flex_grid_points_toggle(0)

five heroes:
    user.flex_grid_map_points_by_raw_location_range("hero", 5, 163, 195, 163, 1095)
    user.flex_grid_points_toggle(0)

four heroes:
    user.flex_grid_map_points_by_raw_location_range("hero", 4, 163, 240, 163, 1050)
    user.flex_grid_points_toggle(0)

two heroes:
    user.flex_grid_map_points_by_raw_location_range("hero", 2, 163, 400, 163, 850)
    user.flex_grid_points_toggle(0)


^spell$: user.flex_grid_go_to_point("spell", 1, 0)
^top spell$: user.flex_grid_go_to_point("up", 1, 0)
^bottom spell$: user.flex_grid_go_to_point("down", 1, 0)


enemy [<number>]: user.flex_grid_go_to_point("enemy", number or 1, -1)

side [<number>]: user.flex_grid_go_to_point("sides", number or 1, 0)
top [side] [<number>]: user.flex_grid_go_to_point("top", number or 1, 0)
bottom [side] [<number>]: user.flex_grid_go_to_point("bottom", number or 1, 0)

