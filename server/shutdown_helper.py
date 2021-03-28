import psutil
import os


def spigot_running():
    """returns True iff spigot is running"""
    for proc in psutil.process_iter():
        if "java" in proc.name():
            return True
    return False


def users():
    """Return true if any user is logged in."""
    # check own user:
    try:
        users_logged = psutil.users()
    except:
        users_logged = []
    unames = [u.name for u in users_logged]

    for user in unames: # if there are any more instances of remy, then return True in order to not shutdown
        if "remy" in user or "Remy" in user:
            return True

    # if either remy was never logged in, or remy issued the command to shutown himself (AND has no other instances), then we shutdown
    return False

def other_users():
    """Returns true if and only if other instances than the one that called the command are logged in"""
    # check own user:
    try:
        logged_in = os.getlogin()
    except:
        logged_in = "NO USER"
    try:
        users_logged = psutil.users()
    except:
        users_logged = []
    
    unames = [u.name for u in users_logged]
    
    for i,u in enumerate(unames): # clear the list of the logged_in user:
        if logged_in in u:
            unames.pop(i)
            break
    
    for user in unames: # if there are any more instances of remy, then return True in order to not shutdown
        if "remy" in user or "Remy" in user:
            return True

    # if either remy was never logged in, or remy issued the command to shutown himself (AND has no other instances), then we shutdown
    return False

def logout():
    """logs out the current user"""
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
    """Powers off the computer"""
    print("POWER OFF")
    if os.name != "nt": # not running on windows
        os.system("sudo shutdown now") # sudo does not require a password on manjaro-tower
