import time
import os

real_deal = True
try:
   import RPi.GPIO as GPIO
except:
    real_deal = False

class PiOut:
    def __init__(self):
        self.trigger = 18
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.trigger, GPIO.OUT)

    def turn_on(self):
        if not self.already_on():
            return
        GPIO.output(18, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(18, GPIO.LOW)
    
    def already_on(self):
        hostname = "192.168.178.29"
        response = os.system("ping -c 1 " + hostname)

        return (response == 0)

class SimOut:
    def __init__(self):
        print("Using the sim")
    
    def turn_on(self):
        print("Now the computer would start!")




if real_deal:
    handler = PiOut()
else:
    handler = SimOut()