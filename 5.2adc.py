import RPi.GPIO as GPIO
from time import sleep
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
bits = len(dac)
levels = 2**bits

def dec2bin(num):
    return [int(bit) for bit in bin(num)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

GPIO.setup (troyka, GPIO.OUT, initial = GPIO.HIGH)

def adc():
    vr = 0
    tv = 0
    for i in range (bits):
        pow2 = 2**(bits - i - 1)
        tv = vr + pow2
        signal = dec2bin(tv)
        GPIO.output (dac, signal)
        sleep (0.01)
        compv = GPIO.input (comp)
        if compv == 0:
            vr = tv
    return vr
try:
    while True:
        value = adc ()
        voltage = value/levels* 3.3
        print ("digit = ", value, "voltage = ", voltage)

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()