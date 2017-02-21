import _thread
import sys
import motorControl
#import servoControl
import time#
import mySocket
import myCamera

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
    app = mySocket.serverSocket(host, 6510)
    while True:
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

def cameraStream(host):
    print('Run cameraStream')
    camera = myCamera.cameraClass(800, 600)
    cameraSocket = mySocket.serverSocket(host, 6515)
    while True:
        cameraSocket.connect() #Host , port
        cameraSocket.setTimeOut()
        while True:
            try:
                camera.capture('tempFrame')
                data = camera.convertToBinary('tempFrame')
                cameraSocket.sendData(data)
                #print(data) #For debugging
                #time.sleep(0.01) #Try without the pause
            except cameraSocket.timeOut:
                print(cameraSocket.timeOut)
                break;
                
_thread.start_new_thread(runLidar, (HOST,))

_thread.start_new_thread(runMotors, (HOST,))

_thread.start_new_thread(cameraStream, (HOST,))
