tag: user.clipboard_manager
-

clip man stay:
    user.clipboard_manager_toggle_sticky()

clip man clear:
    user.clipboard_manager_remove()

clip man chuck <number_small> [and <number_small>]*:
    user.clipboard_manager_remove(number_small_list)

clip man split <number_small> [and <number_small>]*:
    user.clipboard_manager_split(number_small_list)

clip man copy <number_small> [and <number_small>]*:
    user.clipboard_manager_copy(number_small_list)
