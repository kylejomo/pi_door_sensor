from time import sleep
import RPi.GPIO as GPIO
import requests

# setup variables
delay=.1
inPin=40
outPin=38
LEDstate=0        # starts as off
buttonState=1     # starts as on
buttonStateOld=1  # starts as on

# configure GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(outPin,GPIO.OUT)
GPIO.setup(inPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

try:
    while True:
        buttonState=GPIO.input(inPin) # when pressed it goes to 0
        #print(buttonState)
        if buttonState==0 and buttonStateOld==1:  # button has just been pushed
            LEDstate= not LEDstate   # toggle the LED 
            GPIO.output(outPin,LEDstate)
        buttonStateOld=buttonState
        sleep(delay)
except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO Cleaned Up')


# Post - Write a new todo
#api_url = "https://api.restful-api.dev/objects"
#thing = {"name": "Closed"}
#response = requests.post(api_url, json=thing)
#print("Response from Post")
#print(response.json())
#print("ID and Status Code")
#print(response.json().get("id"))
#print(response.status_code)


# Get - Get the todo just written
api_url = "https://api.restful-api.dev/objects/ff8081818eeb2234018f03c9a27f3d1f"
response = requests.get(api_url)
print("\n\n Get of the thing object just written")
print(response.json())


# PUT - Change the todo
api_url = "https://api.restful-api.dev/objects/ff8081818eeb2234018f03c9a27f3d1f"
thing = {"name": "Opened"}
response = requests.put(api_url, json=thing)
print("\n\n Response from Put")
print(response.json())
print(response.status_code)


# Get - Get the todo just changed 
api_url = "https://api.restful-api.dev/objects/ff8081818eeb2234018f03c9a27f3d1f"
response = requests.get(api_url)
print("\n\n Get of the thing object just written")
print(response.json())
