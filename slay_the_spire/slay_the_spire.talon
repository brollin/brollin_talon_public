os: mac
and app.bundle: net.java.openjdk.cmd
-
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
spire grid: user.spire_activate_grid()
done:
    user.spire_close_grid()
    user.spire_enemy(1)
bug: user.spire_handle_bug()
booty: user.spire_go_to_booty()
confirm:
    key(enter)
    user.spire_handle_bug()
shop <number_small>: user.spire_shop_item(number_small)
