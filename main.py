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
                thrust = app.getData(data, 0, 8)
                steeringThrust = app.getData(data, 8, 16)
                motorControl.steeringThrust(thrust, steeringThrust)
                #print(thrust , ' ', steeringThrust) #For debugging
                #time.sleep(0.01) #Try without the pause
            except app.timeOut:
                print(app.timeOut)
                break;

def cameraStream(host):
    while True:
        print('Run cameraStream')
        camera = myCamera.cameraClass(800, 600)
        cameraSocket = mySocket.serverSocket(host, 6515) 
        cameraSocket.connect() #Host , port
        stream = cameraSocket.makefile()
        camera.startCapture(stream)
        try:
            while True:
                camera.capture() #Exit to finally if something goes wrong
        finally:
            camera.end()
            cameraSocket.end()
                
_thread.start_new_thread(runLidar, (HOST,))

_thread.start_new_thread(runMotors, (HOST,))

_thread.start_new_thread(cameraStream, (HOST,))
