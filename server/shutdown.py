import psutil
import os

def spigot_running():
    """returns True iff spigot is running"""
    for proc in psutil.process_iter():
        if "spigot" in proc.name():
            return True
    return False

def other_users():
    """returns True iff user remy (or other) is logged in (through ssh, vnc or other)"""
    users = psutil.users()
    for user in users:
        if "remy" in user.name or "Remy" in user.name:
            return True
    return False

def logout():
    if os.name == "nt": # running on windows
        os.system("shutdown -l")
    else: # linux
        try: # for users like remy
            uname = os.path.expanduser("~").replace("/home/","")
            os.system("sudo pkill -u" + uname)
        except: # for users like craftbukkit, without homedir
            print("Doing nothing")

def poweroff():
    if os.name == "nt": # running on windows
        print("POWER OFF")
    else:
        os.system("sudo shutdown now")


if spigot_running() or other_users():
    logout()
else:
    poweroff()
