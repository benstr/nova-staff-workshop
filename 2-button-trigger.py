import RPi.GPIO as GPIO ## Import GPIO library
from time import sleep ## Allows us to use 'sleep'

GPIO.setmode(GPIO.BCM) ## Use broadcom pin numbering

LED_PIN = 17 ## GPIO pin the LED is attached to
BTN_PIN = 4 ## GPIO pin the button is attached to

##setup button pin
GPIO.setup(BTN_PIN,GPIO.IN,pull_up_down=GPIO.PUD_UP) ## Setup GPIO pin as an input

## LED state
ledState = False

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


try:
    while True:

        ## Real-time light state
        if GPIO.input(BTN_PIN) == False:
            lightOn(LED_PIN)
            ledState = True
        else:
            lightOff(LED_PIN)
            ledState = False

finally:
    GPIO.output(LED_PIN,False) ## Switch off LED
    GPIO.cleanup()  ## reset all pins