import RPi.GPIO as GPIO
import time

# Associo variabile colori a pin Raspberry
blue = 17
green = 27
red = 22

class RGBClass:
    def __init__(self):
        #GPIO.setmode(GPIO.BCM)  # convenzione nomeclatura dei pin

        GPIO.setwarnings(False)  # no GPIO warnings da Python in console

        # choosing a frequency for pwm
        Freq = 100

        GPIO.setup(blue, GPIO.OUT)  # blue
        GPIO.setup(green, GPIO.OUT)  # verde
        GPIO.setup(red, GPIO.OUT)  # rosso
        '''
        #self.RED = GPIO.PWM(red, Freq)
        self.RED_on = GPIO.output(red,True)## Accendo il led
        self.RED_off = GPIO.output(red,False)## Accendo il led
        self.GREEN = GPIO.PWM(green, Freq)
        self.BLUE = GPIO.PWM(blue, Freq)
        '''

    @staticmethod
    def green_on():
        GPIO.output(green, 1)

    @staticmethod
    def green_off():
        GPIO.output(green, 0)

    @staticmethod
    def blue_on():
        GPIO.output(blue, 1)

    @staticmethod
    def blue_off():
        GPIO.output(blue, 0)
        
    @staticmethod
    def red_off():
        GPIO.output(red, 0)

    @staticmethod
    def red_pulse():
        for x in range(1, 5):
            GPIO.output(red, 1)
            time.sleep(0.1)
            GPIO.output(red, 0)
            time.sleep(0.1)