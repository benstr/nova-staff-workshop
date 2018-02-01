import RPi.GPIO as GPIO ## Import GPIO library
from time import sleep ## Allows us to use 'sleep'
from Hologram.HologramCloud import HologramCloud ## Import Hologram cloud library

GPIO.setmode(GPIO.BCM) ## Use broadcom pin numbering

LED_PIN = 17 ## GPIO pin the LED is attached to
BTN_PIN = 4 ## GPIO pin the button is attached to

##setup button pin
GPIO.setup(BTN_PIN,GPIO.IN,pull_up_down=GPIO.PUD_UP) ## Setup GPIO pin as an input

GPIO.setup(LED_PIN, GPIO.OUT)

## setup Hologram
hologram = HologramCloud(dict(), network='cellular', authentication_type='sim-otp')
TOPIC = 'benstrs-light'

## LED state
LED_STATE = False

## Function to turn an LED on
def lightOn(PIN):
    GPIO.setup(LED_PIN, GPIO.OUT) ## Setup GPIO Pin to OUT
    GPIO.output(LED_PIN,True) ## Switch on LED

## Function to turn an LED off
def lightOff(PIN):
    GPIO.setup(LED_PIN, GPIO.OUT) ## Setup GPIO Pin to OUT
    GPIO.output(LED_PIN,False) ## Switch on LED

## Function to blink an LED once
def blink(PIN, hold = 0.5):
    lightOn(LED_PIN)
    sleep(hold)
    lightOff(LED_PIN)
    sleep(hold)

## Function to toggle LED
def toggleLed(PIN):
    global LED_STATE
    if LED_STATE is True:
        lightOff(PIN)
        LED_STATE = False
        return False
    else:
        lightOn(PIN)
        LED_STATE = True
        return True


try:
    while True:

        ## Button pressed
        if GPIO.input(BTN_PIN) == False:

            ## toggle LED
            result = toggleLed(LED_PIN)
            
            ## send event message to the cloud
            hologram.sendMessage("light turned "  + str(result), [TOPIC])

finally:
    GPIO.output(LED_PIN,False) ## Switch off LED
    GPIO.cleanup()  ## reset all pins
