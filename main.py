import _thread
import sys
import motorControl
#import servoControl
import time#
import mySocket

HOST = ''
def runLidar(host):
    print('Run Lidar ')
    #setupLidar()
    processing = mySocket.serverSocket(host, 6511)
    processing.connect()    #Host , port
    while True:
        distances = servoControl.sweepRight()    #distances is an array
        processing.sendData(distances)
        distances = servoControl.sweepLeft()
        processing.sendData(distances)
        #pause
    
def runMotors(host):
    print('Run Motors')
    motorControl.setup()
    while True:
        app = mySocket.serverSocket(host, 6510)
        app.connect() #Host , port
        app.setTimeOut()
        while True:
            try:
                data = app.recData()
                steeringThrust = app.getData(data, 0, 8)
                thrust = app.getData(data, 8, 16)
                motorControl.steeringThrust(thrust, steeringThrust)
                print(thrust , ' ', steeringThrust) #For debugging
                #time.sleep(0.01) #Try without the pause
            except app.timeOut:
                print(app.timeOut)
                break;

_thread.start_new_thread(runLidar, (HOST,))

_thread.start_new_thread(runMotors, (HOST,))
