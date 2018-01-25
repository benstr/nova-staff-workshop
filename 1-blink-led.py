import RPi.GPIO as GPIO ## Import GPIO library
from time import sleep ## Allows us to use 'sleep'

GPIO.setmode(GPIO.BCM) ## Use broadcom pin numbering

LED_PIN = 17 ## GPIO pin the LED is attached to

## blink an LED
interval = 0
duration = 0.5

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
        interval += 1
        print "Blink #" + str(interval) ## Print current loop number
        blink(LED_PIN, duration) ## blink that light!

finally:
    GPIO.output(LED_PIN,False) ## Switch off LED
    GPIO.cleanup()  ## reset all pins