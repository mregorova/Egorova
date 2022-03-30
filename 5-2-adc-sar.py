import RPi.GPIO as GPIO
import time 

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3
troykaModule = 17
comp = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(troykaModule, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.OUT, initial=GPIO.HIGH)

def decimal2binary(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(bits)]

def num2dac(value):
    signal = decimal2binary(value)
    GPIO.output(dac, signal)

    return signal

def adc(value):
    comparatorValue = GPIO.input(comp)
            
    return comparatorValue

try:
    while True:


        number = 0
        for value in range(8):
            number += 2**(8 - value - 1)

            signal = decimal2binary(number)
            GPIO.output(dac, signal)
            time.sleep(0.001)
            voltage = number / 255 * maxVoltage

            comparatorValue = adc(value)

            if comparatorValue == 0:
                number -= 2**(8 - value - 1)
        
            print("ADC value = {:^3} -> {}, input voltage = {:.2f}".format(value, signal, voltage))



except KeyboardInterrupt:
    print('\nThe program was stopped by the keyboard')
else:
    print("No exceptions")
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    
    print('GPIO cleanup completed')