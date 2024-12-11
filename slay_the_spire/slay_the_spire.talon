os: mac
and app.bundle: net.java.openjdk.cmd
-

# voice commands to ignore
each: skip()
sun: skip()
drum: skip()
air: skip()
made: skip()

(head | tug) <user.number_string>: skip()
use ten: skip()
use: skip()
word <user.text>: skip()

# Turn off repeater ordinals (optional; prevents accidental repeats)
<user.ordinals>: skip()

# long right click
info:
    user.mouse_drag(1)
    sleep(0.1)
    user.mouse_drag_end()

# long left click
touchy:
    user.mouse_drag(0)
    sleep(0.1)
    user.mouse_drag_end()

turn turn: key(e)
