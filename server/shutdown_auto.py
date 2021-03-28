import shutdown_helper as h


if h.spigot_running() or h.users():
    # do nothing:
    print("PROCESSES STILL RUNNING -> doing nothing")
else:
    h.poweroff()
