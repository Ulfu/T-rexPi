import RPi.GPIO as GPIO
import GPIO.PWM as PWM

GPIO.setmode(GPIO.BCM)

motors = [[17,27,18],[22,23,24]]
#m1 = motors[0[3]]
#m2 = motors[1[3]]


def forward(true):
    for m in motors:
        GPIO.output(m[0], true)#Gpio print
        GPIO.output(m[1], not true)

def thrust(speed1, speed2):
    speed1 = int(speed1)#Only let integers pass
    speed2 = int(speed2)
    nonlocal m1
    nonlocal m2
    m1.ChangeDutyCycle(speed1) #max speed 100
    m2.ChangeDutyCycle(speed2) #max speed 100

def steeringThrust(thrust, turnPercent):
    thrust = clamp(thrust,-100, 100)
    turnPercent = clamp(turnPercent,-100, 100)

    if (thrust < 0):
        direction = false
        thrust = abs(thrust)
    else:
        direction = false
    
    speed1 = thrust
    speed2 = thrust
    
    if (turnPercent < 0):
        speed1 = speed * (1 + turnPercent / 100)
    elif (turnPercent > 0):
        speed2 = speed * (1 - turnPercent / 100)

    forward(direction)
    thrust(speed1, speed2)
        
def rotate(left):
     for m in motors:
        GPIO.output(m[0], left)#Gpio print
        GPIO.output(m[1], not left)
        left != left #
        
def clamp(n, minVal, maxVal):   #constain a value
    return max(min(maxVal, n), minVal)
        
def setup():    #setup motor pins as outputs
    #PWM.cleanup()
    for i in range(2):
        GPIO.setup(motors[0[i]], GPIO.OUT)
        GPIO.setup(motors[1[i]], GPIO.OUT)
    nonlocal m1 = PWM(motors[0[3]], 50)
    nonlocal m1 = PWM(motors[1[3]], 50)
    m1.start(0)
    m2.start(0)
