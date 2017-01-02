import RPi.GPIO as GPIO
from RPIO import PWM

servo = PWM.Servo()
GPIO.setmode(GPIO.BCM)

motors = [[17,27,18],[22,23,24]]
m1 = motors[0]
m2 = motors[1]

global speed
speed = 0

def forward(true):
    for m in motors:
        GPIO.output(m[0], true)##Gpio print
        GPIO.output(m[1], not true)##It seems as it would not print out a two dimensional for loop

def thrust(speed1, speed2):
    speed1 = int(speed1)##Only let integers pass
    speed2 = int(speed2)
    
    servo.set_servo(m1[3], speed1) ##max speed 20000
    servo.set_servo(m2[3], speed2) ##max speed 20000

def steeringThrust(turnPercent):
    speed1 = speed
    speed2 = speed
    
    if turnPercent < 0:
        speed1 = speed * turnPercent / (-100)
    if turnPercent > 0:
        speed2 = speed * turnPercent / 100

    thrust(speed1, speed2)
        
def rotate(left):
     for m in motors:
        GPIO.output(m[0], left)##Gpio print
        GPIO.output(m[1], not left)
        left != left ##
        
def setup():    ##setup motor pins as outputs
    PWM.cleanup()
    for i in range(1):
        GPIO.setup(m1[i], GPIO.OUT)
        GPIO.setup(m2[i], GPIO.OUT) 
