import RPi.GPIO as GPIO

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

try:
    print("Please enter a number from 0 to 255")
    n = input()
    if (n == 'q'):
        quit()

    if (n.isdigit() or (n == 'q')):
        n = int(n)
        if (n < 0):
            print("Please enter number > 0")

        if (n > 255):
            print("It is more than DAC can manage")
            quit()

        for i in range(8):
            GPIO.output(dac[i], decimal2binary(n)[i])
        print("DAC voltage should be:", n * (3.3/2**8))
        
    else:
        print("Not an int number")

finally:

    GPIO.output(dac, 0)
    GPIO.cleanup()