from picamera import PiCamera

class cameraClass:
	def __init__(self, resolutionX, resolutionY):#setup camera
                self.resolutionX = resolutionX
                self.resolutionY = resolutionY
                self.camera = PiCamera()
                self.camera.resolution = (resolutionX, resolutionY)
        
	def capture(self, name):#capture image
                name = name + '.png'
                #camera.start_preview()
                camera.capture(name)
                #camera.close()

        def convertToBinary(self, name):
                name = name + '.png'
                with open(name, 'rb') as imageFile:
                file = imageFile.read()
                b = bytearray(file)
                return b
                #print b[0]

