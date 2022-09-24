os: mac
# and app.bundle: com.parallels.desktop.console
-

zoom in: user.mouse_scroll_up()
zoom out: user.mouse_scroll_down()

spell grid: user.spell_grid_activate()
spell show: user.spell_grid_show()
spell hide: user.spell_grid_hide()
spell (off | close): user.spell_grid_close()

go <user.letter> <user.letter>: user.spell_id_move(letter_1, letter_2)

hero one: key(f1)
hero two: key(f2)
hero three: key(f3)
hero four: key(f4)
hero five: key(f5)
hero six: key(f6)
hero seven: key(f7)
