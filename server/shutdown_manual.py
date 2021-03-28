import shutdown_helper as h


if h.spigot_running() or h.other_users():
    h.logout()
else:
    h.poweroff()
