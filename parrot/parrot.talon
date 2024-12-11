not mode: sleep
-
parrot(alveolar_click):
	# app.notify("alveolar_click")
	user.do_mapped_parrot_action("alveolar_click")
parrot(dental_click):
	# app.notify("dental_click")
	# user.do_mapped_parrot_action("dental_click")
	mimic("model fix grammar block this")
	# tracking.control_zoom_toggle()
    # tracking.control_toggle()
parrot(shush):
	# app.notify("shush")
	user.do_mapped_parrot_action("shush")
parrot(hiss):
	# app.notify("hiss")
	user.do_mapped_parrot_action("hiss")


^assign {user.parrot_sound} <user.alphanumeric_or_action>$:
	user.assign_parrot_action(parrot_sound, alphanumeric_or_action)

^unassign {user.parrot_sound}$:
	user.unassign_parrot_action(parrot_sound)

^unassign all$:
	user.unassign_parrot_action("all")

# pro <user.text>: user.set_parrot_profile(text)
finished: user.set_parrot_profile("")
zoomer: user.set_parrot_profile("zoomer")
# scroller: user.set_parrot_profile("scroller")
gazer: user.set_parrot_profile("gazer")
# flip: user.parrot_special_action("flip")
