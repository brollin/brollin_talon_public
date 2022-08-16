not mode: sleep
-
parrot(tongue_click): user.do_mapped_parrot_action("tongue_click")
parrot(caveman): user.do_mapped_parrot_action("caveman")

^assign {user.parrot_sound} <user.alphanumeric_or_action>$:
	user.assign_parrot_action(parrot_sound, alphanumeric_or_action)

^unassign {user.parrot_sound}$:
	user.unassign_parrot_action(parrot_sound)

^unassign all$:
	user.unassign_parrot_action("all")

profile <user.text>: user.set_parrot_profile(text)
profile none: user.unassign_parrot_action("all")
zoomer: user.set_parrot_profile("second")
