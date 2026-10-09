import RPi.GPIO as GPIO
from time import sleep

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def dec2bin(num):
    return [int(bit) for bit in bin(num)[2:].zfill(8)]

inc_flag = 1
t = 0
x = 0

try:
    period = float(input("type a period for signal: "))

    while True:
        GPIO.output (dac, dec2bin(x))

        if x == 0: 
            inc_flag = 1
        elif x == 255: 
            inc_flag = 0
        x = x + 1 if inc_flag == 1 else x - 1

        sleep(period/512)
        t += 1
except ValueError:
    print ("wrong period")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("EOP")