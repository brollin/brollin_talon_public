os: mac
and app.bundle: com.redhookgames.Darkest
-

# more info: https://talon.wiki/unofficial_talon_docs/#built-in-talon-settings
settings():
    user.mouse_wheel_down_amount = 60
    key_hold = 32

# borrowed some of these from: https://github.com/ziemus/talon_voice_games/blob/master/Darkest%20Dungeon/darkest_dungeon.talon
touch:
    user.mouse_drag(0)
    sleep(0.1)
    user.mouse_drag_end()

righty:
    user.mouse_drag(1)
    sleep(0.1)
    user.mouse_drag_end()

hero next: key(e)
hero last: key(q)

trinket sell | torch down:
    key("shift:down")
    user.mouse_drag(0)
    sleep(0.1)
    user.mouse_drag_end()
    key("shift:up")

torch snuff out:
    key("shift-ctrl:down")
    user.mouse_drag(0)
    sleep(0.1)
    user.mouse_drag_end()
    key("shift-ctrl:up")

gear | inventory:
    key(tab)

take all:
    key(space)

torch:
    key(t)

help:
    key(h)

skill [<number>]$: user.flex_grid_go_to_point("action", number or 1, -1)
skill next$: user.flex_grid_go_to_point_relative("action", 1)
skill last$: user.flex_grid_go_to_point_relative("action", -1)

enemy [<number>]$: user.flex_grid_go_to_point("enemy", number or 1, -1)
enemy next$: user.flex_grid_go_to_point_relative("enemy", 1)
enemy last$: user.flex_grid_go_to_point_relative("enemy", -1)

deck(pedal_middle:down): user.mouse_drag(0)
deck(pedal_middle:up): user.mouse_drag_end()

parrot(shush): user.flex_grid_deactivate()
