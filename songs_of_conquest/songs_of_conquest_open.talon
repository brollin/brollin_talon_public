os: mac
and app.bundle: unity.Lavapotion.SongsOfConquest
and not mode: sleep
-

# for example: go 1 north
go <number> {user.conquest_cardinal}: user.conquest_cardinal_move_1d(conquest_cardinal_1, number_1, "")
# for example: go north 1
go {user.conquest_cardinal} <number>: user.conquest_cardinal_move_1d(conquest_cardinal_1, number_1, "")
# for example: go 1 north 3 east
go <number> {user.conquest_cardinal} [also] <number> {user.conquest_cardinal}:
    user.conquest_cardinal_move_2d(conquest_cardinal_1, number_1, conquest_cardinal_2, number_2, "")
# for example: go north 1 east 3
go {user.conquest_cardinal} <number> [also] {user.conquest_cardinal} <number>:
    user.conquest_cardinal_move_2d(conquest_cardinal_1, number_1, conquest_cardinal_2, number_2, "")
go center:
    user.conquest_cardinal_move_1d("north", 0, "")

go <user.letter> <user.letter>: user.conquest_id_move(letter_1, letter_2)

# relative equivalents
also <number> {user.conquest_cardinal}: user.conquest_cardinal_move_1d(conquest_cardinal_1, number_1, "relative")
also {user.conquest_cardinal} <number>: user.conquest_cardinal_move_1d(conquest_cardinal_1, number_1, "relative")
also <number> {user.conquest_cardinal} <number> {user.conquest_cardinal}:
    user.conquest_cardinal_move_2d(conquest_cardinal_1, number_1, conquest_cardinal_2, number_2, "relative")
also {user.conquest_cardinal} <number> {user.conquest_cardinal} <number>:
    user.conquest_cardinal_move_2d(conquest_cardinal_1, number_1, conquest_cardinal_2, number_2, "relative")

