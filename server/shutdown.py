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
    # check own user:
    try:
        logged_in = os.getlogin()
    except:
        logged_in = "NO USER"
    users = psutil.users()
    
    unames = [u.name for u in users]
    
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
    print("LOGOUT")
    if os.name == "nt": # running on windows
        os.system("shutdown -l")
    else: # linux
        try: # for users like remy
            uname = os.getlogin()
            os.system("sudo pkill -u" + uname)
        except: # for users like craftbukkit, without homedir
            print("Doing nothing")

def poweroff():
    if os.name == "nt": # running on windows
        print("POWER OFF")
    else:
        print("POWER OFF")
        os.system("sudo shutdown now")



if spigot_running() or other_users():
    logout()
else:
    poweroff()
