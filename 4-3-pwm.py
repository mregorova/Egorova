import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.OUT)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]

p = GPIO.PWM(22, 0.5)
p.start(1)
p.ChangeDutyCycle(0)
input('Press return to stop:')
p.stop()
GPIO.output(dac, 0)
GPIO.cleanup()

try:
    while True:
        print("Enter duty cycle")
        dc = int(input())
        p.ChangeDutyCycle(dc)

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()