os: mac
and app.bundle: subset.Into-the-Breach
and not mode: sleep
-
^go <user.any_alphanumeric_key>+$:
    user.breach_go_to_tile(any_alphanumeric_key_list, "")

^click <user.any_alphanumeric_key>+$:
    user.breach_go_to_tile(any_alphanumeric_key_list, "click")

# parrot(tongue_click):
# 	# mouse_click(0)

parrot(caveman):
	mouse_click(0)

