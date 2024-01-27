os: mac
and app.bundle: net.java.openjdk.cmd
-

settings():
    user.mouse_wheel_down_amount = 300


item <number_small>: user.spire_item(number_small)
item use: user.spire_use_item()
relic <number_small>: user.spire_relic(number_small)
enemy <number_small>: user.spire_enemy(number_small)
^enemy$: user.spire_enemy(1)
click enemy <number_small>: user.spire_enemy(number_small, 0)
^map <user.any_alphanumeric_key>+$: user.spire_map_enemy(any_alphanumeric_key_list)
^map [enemies]$: user.spire_activate_grid()
^unmap [enemies]$: user.spire_clear_enemies()
^remap [enemies]$: user.spire_remap_enemies()
spire open: user.spire_activate_grid()
(map or | mapper) <number_small>: user.spire_auto_map(number_small)
(map or | mapper) <user.text>: user.spire_auto_map_by_text(text)
spire close:
    user.spire_close_grid()
    user.spire_enemy(1)
bug: user.spire_handle_bug()
booty: user.spire_go_to_booty()
confirm:
    key(enter)
    user.spire_handle_bug()
shop <number_small>: user.spire_shop_item(number_small)
third: key(ctrl)
fourth: key(ctrl)
fifth: key(ctrl)
sixth: key(ctrl)
seventh: key(ctrl)
eighth: key(ctrl)
ninth: key(ctrl)

(head | use | tug) <user.number_string>:
    insert(number_string)
    sleep(0.1)
    mouse_click(0)

use ten: key(ctrl)
use: key(ctrl)
word <user.text>: spire_enemy(number_small)

info:
    user.mouse_drag(1)
    sleep(0.1)
    user.mouse_drag_end()

touchy:
    user.mouse_drag(0)
    sleep(0.1)
    user.mouse_drag_end()

