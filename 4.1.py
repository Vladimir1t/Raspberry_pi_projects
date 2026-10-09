import RPi.GPIO as GPIO

GPIO.setwarnings(False)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def dec2bin(num):
    return [int(bit) for bit in bin(num)[2:].zfill(8)]

#dac = [8, 11, 7, 1, 0, 5, 12, 6]

try:
    while True:
        num = int(input("type a a number: "))
        try:
            if 0 <= num <= 255:
                GPIO.output(dac, dec2bin(num))
                voltage = float(num) / 256.0 * 3.3
                print (f"output voltage {voltage:.4} vlot")
            else:
                if num < 0:
                    print ("try again. num < 0")
                elif num > 255:
                    print ("try again num > 255")
        except Exception as e:
            if num == "q": break
            print(e)
            print ("try again. not string")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()        
    print ("EOP")