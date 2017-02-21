from picamera import PiCamera

class cameraClass:
	def __init__(self, resolutionX, resolutionY):
		self.resolutionX = resolutionX
        self.resolutionY = resolutionY
        self.camera = PiCamera()
        self.camera.resolution = (resolutionX, resolutionY)
        
	def capture(self, name):
        camera.start_preview()
        camera.capture(name,'.png')
		camera.close()
