import RPi.GPIO as GPIO
import time

leds = [21, 20, 16, 12, 7, 8, 25, 24]

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)

for j in range(2):
    for i in range (7):
        GPIO.output(leds[i], 1)
        time.sleep(1)
        GPIO.output(leds[i], 0)

GPIO.cleanup()