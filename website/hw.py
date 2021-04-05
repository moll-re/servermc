import time
import datetime
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
        self.last_called = datetime.datetime.fromtimestamp(0)
    
    def turn_on(self):
        if self.is_on():
            return
        self.last_called = datetime.datetime.now()
        print("Now starting the PC...")

    def is_on(self):
        response = os.system("nc -w 1 -vz " + self.host_ip + " 2556")
        print(response)
        on_status = (response == 0) # response 0 means ping was successful
        on_expected = datetime.datetime.now() - self.last_called <= datetime.timedelta(minutes=2)
        return on_status or on_expected


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