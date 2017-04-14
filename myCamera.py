from picamera import PiCamera

class cameraClass:
        def __init__(self, resolutionX, resolutionY):#setup camera
                self.resolutionX = resolutionX
                self.resolutionY = resolutionY
                self.camera = PiCamera()
                self.camera.resolution = (resolutionX, resolutionY)

        def capture(self, name):#capture to stream
                self.camera.start_recording(name, format='h264')
                
        def wait(self):
                self.camera.wait_recording(5)

        def end(self):
                self.camera.stop_recording()


