import _thread
import sys
import motorControl
import mySocket
import myCamera

HOST = ''
    
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
        camera.capture(stream)
        try:
            while True:
                camera.wait() #Exit to finally if something goes wrong
        finally:
            camera.end()
            cameraSocket.end()

_thread.start_new_thread(runMotors, (HOST,))

_thread.start_new_thread(cameraStream, (HOST,))
