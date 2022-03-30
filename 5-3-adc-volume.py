import RPi.GPIO as GPIO
import time 

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3
troykaModule = 17
comp = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(troykaModule, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(leds, GPIO.OUT, initial=GPIO.HIGH)

def decimal2binary(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(bits)]

def num2dac(value):
    signal = decimal2binary(value)
    GPIO.output(dac, signal)

    return signal

def adc():
    value = 0

    for i  in range(8):
        value = value + 2**(7-i)
        GPIO.output(dac, decimal2binary(int(value)))
        time.sleep(0.01)
        if int( GPIO.input(comp)) == 0:
            value = value - 2**(7-i)

    return value

try:
    while True:

        comparatorValue = adc()
        time.sleep(0.1)
        voltage = comparatorValue / 255 * maxVoltage

        if comparatorValue <= 0:
            GPIO.output(leds, decimal2binary(int(0)))
        elif comparatorValue <= 32:
            GPIO.output(leds, decimal2binary(int(1)))
        elif comparatorValue <= 64:
            GPIO.output(leds, decimal2binary(int(3)))
        elif comparatorValue <= 96:
            GPIO.output(leds, decimal2binary(int(7)))
        elif comparatorValue <= 128:
            GPIO.output(leds, decimal2binary(int(15)))
        elif comparatorValue <= 160:
            GPIO.output(leds, decimal2binary(int(31)))
        elif comparatorValue <= 192:
            GPIO.output(leds, decimal2binary(int(63)))
        elif comparatorValue <= 224:
            GPIO.output(leds, decimal2binary(int(127)))
        else:
            GPIO.output(leds, decimal2binary(int(255)))


finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    GPIO.output(leds, GPIO.LOW)
    GPIO.cleanup(leds)
    
    print('GPIO cleanup completed')