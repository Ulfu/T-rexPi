import RPi.GPIO as GPIO
#import RPi.GPIO.PWM as PWM

GPIO.setmode(GPIO.BCM)

motors = [[17,27,18],[22,23,24]]
#m1 = motors[0[3]]
#m2 = motors[1[3]]


def forward(true):
    for m in motors:
        GPIO.output(m[0], true)#Gpio print
        GPIO.output(m[1], not true)

def setThrust(speed1, speed2):
    speed1 = int(speed1)#Only let integers pass
    speed2 = int(speed2)
    m1.ChangeDutyCycle(speed1) #max speed 100
    m2.ChangeDutyCycle(speed2) #max speed 100

def steeringThrust(thrust, turnPercent):
    thrust = clamp(thrust,-100, 100)
    turnPercent = clamp(turnPercent,-100, 100)
    thrust = clampIf(thrust,-10, 10)
    turnPercent = clampIf(turnPercent,-10, 10)

    if (thrust < 0):
        direction = false
        thrust = abs(thrust)
    else:
        direction = False
    
    speed1 = thrust
    speed2 = thrust
    
    if (turnPercent < 0):
        speed1 = speed * (1 + turnPercent / 100)
    elif (turnPercent > 0):
        speed2 = speed * (1 - turnPercent / 100)

    forward(direction)
    setThrust(speed1, speed2)
        
def rotate(left):
     for m in motors:
        GPIO.output(m[0], left)#Gpio print
        GPIO.output(m[1], not left)
        left != left #
        
def clamp(n, minVal, maxVal):   #constain a value
    return max(min(maxVal, n), minVal)
        
def setup():    #setup motor pins as outputs
    #PWM.cleanup()
    #for i in range(2):
        #GPIO.setup(motors[0][i], GPIO.OUT)
        #GPIO.setup(motors[1][i], GPIO.OUT)
    GPIO.setup(motors[0][0], GPIO.OUT)
    GPIO.setup(motors[1][0], GPIO.OUT)
    GPIO.setup(motors[0][1], GPIO.OUT)
    GPIO.setup(motors[1][1], GPIO.OUT)
    GPIO.setup(motors[0][2], GPIO.OUT)
    GPIO.setup(motors[1][2], GPIO.OUT)
    global m1
    m1 = GPIO.PWM(motors[0][2], 50)
    global m2
    m2 = GPIO.PWM(motors[1][2], 50)
    m1.start(0)
    m2.start(0)
    
def clampIf(n, minVal, maxVal):
    if (n > minVal and n <maxVal):
        n = 0
    return n
