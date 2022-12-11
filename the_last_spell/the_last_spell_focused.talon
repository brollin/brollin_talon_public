os: mac
and app.bundle: com.parallels.desktop.console
-

zoom in: user.mouse_scroll_up()
zoom out: user.mouse_scroll_down()

spell grid: user.spell_grid_activate()
spell show: user.spell_grid_show()
spell hide: user.spell_grid_hide()

go <user.letter> <user.letter>: user.spell_id_move(letter_1, letter_2, -1)
click <user.letter> <user.letter>: user.spell_id_move(letter_1, letter_2, 0)

go good: mouse_move(2101.0, 720.0)
go bad: mouse_move(1337.0, 720.0)

hero one: key(f1)
hero two: key(f2)
hero three: key(f3)
hero four: key(f4)
hero five: key(i)
hero six: key(f6)
hero seven: key(f7)

hero next: "."
hero last: "\\"

defences: "{"
buildings: "}"
turn end turn: key(f9)
city stash: key(f10)
info: "'"
shop: "`"
oracle: "/"
tavern: ";"

weapons: key(tab)
skill: key(backspace)
turbo: key(space)
rotate: ","
undo move: key(delete)

double: user.spell_double_click()

command wax: mouse_move(1337.0, 720.0)
