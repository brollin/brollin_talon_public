drain: edit.word_left()
step: edit.word_right()

tug: edit.left()
push: edit.right()
north: edit.up()
sout: edit.down()


# Delete
clear all: user.delete_all()
clear line: edit.delete_line()
clear line start: user.delete_line_start()
clear line end: user.delete_line_end()
clear left: edit.delete()
clear right: user.delete_right()

<user.delete> up:
    edit.extend_line_up()
    edit.delete()

<user.delete> down:
    edit.extend_line_down()
    edit.delete()

<user.delete> word:
    edit.delete_word()

scratcher:
    user.delete_word_left_n(1)

# scratcher <number_small> times:
#     user.delete_word_left_n(number_small)

swallow:
    user.delete_word_right_n(1)

swallow <number_small> times:
    user.delete_word_right_n(number_small)

<user.delete> head:
    edit.extend_line_start()
    edit.delete()

<user.delete> tail:
    edit.extend_line_end()
    edit.delete()

<user.delete> way up:
    edit.extend_file_start()
    edit.delete()

<user.delete> way down:
    edit.extend_file_end()
    edit.delete()
