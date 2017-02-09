import _thread
import sys
#import motorControl
#import servoControl
import time#
import mySocket

HOST = ' '
def runLidar(host):
    print('Run Lidar ')
    #setupLidar()
    processing = mySocket.mySocket(host, 6511)
    processing.connect()    #Host , port
    while True:
        distances = servoControl.sweepRight()    #distances is an array
        processing.sendData(distances)
        distances = servoControl.sweepLeft()
        processing.sendData(distances)
        #pause
    
def runMotors(host):
    print('Run Motors')
    app = mySocket.mySocket(host, 6510)
    app.connect() #Host , port
    while True:
        data = app.recData()
        thrust = app.getData(data, 0, 8)
        steeringThrust = app.getData(data, 8, 16)
        #motorControl.steeringThrust(thrust, steeringThrust)
        print(thrust , ' ', steeringThrust) #For debugging
        #time.sleep(0.01) #Try without the pause

_thread.start_new_thread(runLidar, (HOST,))

_thread.start_new_thread(runMotors, (HOST,))
