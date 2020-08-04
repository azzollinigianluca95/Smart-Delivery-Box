import RPi.GPIO as GPIO
import time

def ServoOpen():
    servoPIN = 26
    #GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(servoPIN, GPIO.OUT)
    p = GPIO.PWM(servoPIN, 50)

    print("start opening")
    p.start(2.5)
    time.sleep(0.5)
    p.stop()

def ServoClose():
    servoPIN = 26
    #GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(servoPIN, GPIO.OUT)
    p = GPIO.PWM(servoPIN, 50)

    print ("start closing")
    p.start(2.5)
    p.ChangeDutyCycle(12.5)
    time.sleep(0.5)
    p.stop()