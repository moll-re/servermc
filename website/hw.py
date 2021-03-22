import time
import os

real_deal = True
try:
   import RPi.GPIO as GPIO
except:
    real_deal = False

class SimOut:
    def __init__(self, host_ip, host_url):
        print("Starting HW-handler")
        self.host_ip = host_ip
        self.host_url = host_url
    
    def turn_on(self):
        print("Now starting the PC...")
        if self.is_on():
            return

    def is_on(self):
        response = os.system("ping -c 1 " + self.host_ip)
        return (response == 0) # response 0 means ping was successful


class PiOut(SimOut):
    def __init__(self, host_ip, host_url):
        super().__init__(host_ip, host_url)
        self.trigger = 18
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.trigger, GPIO.OUT)

    def turn_on(self):
        super().turn_on()
        print("and on HW level too")
        GPIO.output(18, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(18, GPIO.LOW)



if real_deal:
    handler = PiOut
else:
    handler = SimOut