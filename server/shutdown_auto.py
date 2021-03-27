import psutil
import os

def spigot_running():
    """returns True iff spigot is running"""
    for proc in psutil.process_iter():
        if "java" in proc.name():
            return True
    return False

def users():
    """returns True iff user remy (or other) is logged in (through ssh, vnc or other)"""
    # check own user:
    users_logged = psutil.users()
    
    unames = [u.name for u in users_logged]

    for user in unames: # if there are any more instances of remy, then return True in order to not shutdown
        if "remy" in user or "Remy" in user:
            return True

    # if either remy was never logged in, or remy issued the command to shutown himself (AND has no other instances), then we shutdown
    return False

def logout():
    print("LOGOUT")
    if os.name == "nt": # running on windows
        os.system("shutdown -l")
    else: # linux
        try: # for users like remy
            uname = os.getlogin()
            os.system("pkill -u " + uname)
        except: # for users like craftbukkit, without homedir
            print("Doing nothing")

def poweroff():
    if os.name == "nt": # running on windows
        print("POWER OFF")
    else:
        print("POWER OFF")
        os.system("sudo shutdown now") # sudo does not require a password on manjaro-tower



if spigot_running() or users():
    # do nothing:
    print("PROCESSES STILL RUNNING -> doing nothing")
else:
    poweroff()
