from time import sleep
import RPi.GPIO as GPIO
import requests

# setup variables
delay=.5
inPin=40
outPin=38
api_url = "https://api.restful-api.dev/objects/ff8081818eeb2234018f03c9a27f3d1f"

# configure GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(outPin,GPIO.OUT)
GPIO.setup(inPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

try:
    while True:
        readVal = GPIO.input(inPin)
        print(readVal)
        if readVal == 1:   # door is open
            GPIO.output(outPin,0)
            thing = {"name": "Open"}
            response = requests.put(api_url, json=thing)
        if readVal == 0:   # door is closed
            GPIO.output(outPin,1)
            thing = {"name": "Closed"}
            response = requests.put(api_url, json=thing)
        sleep(delay)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("GPIO Cleaned Up")


