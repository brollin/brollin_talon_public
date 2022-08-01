os: mac
and app.bundle: unity.Lavapotion.SongsOfConquest
and not mode: sleep
-
# ^go north <user.any_alphanumeric_key>+$:
#     user.go_absolute(any_alphanumeric_key_list, -1)

# for example: go 1 north
go <number> {user.conquest_cardinal}:
    user.conquest_cardinal_move_1d(conquest_cardinal_1, number_1, "")
# for example: go 1 north 3 east
go <number> {user.conquest_cardinal} <number> {user.conquest_cardinal}:
    user.conquest_cardinal_move_2d(conquest_cardinal_1, number_1, conquest_cardinal_2, number_2, "")

# relative equivalents
and <number> {user.conquest_cardinal}:
    user.conquest_cardinal_move_1d(conquest_cardinal_1, number_1, "relative")
and <number> {user.conquest_cardinal} <number> {user.conquest_cardinal}:
    user.conquest_cardinal_move_2d(conquest_cardinal_1, number_1, conquest_cardinal_2, number_2, "relative")

# parrot(tongue_click):
# 	# mouse_click(0)

parrot(caveman):
	mouse_click(0)

