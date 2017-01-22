import modules.getNewImageCaption as getC
import modules.readCaptionAloud as readC
import modules.azureUpload as azureU
import modules.clarifyImage as cl
import threading
import subprocess
import time

cam=getC.scv.Camera()
sem = threading._Semaphore

while(1):
    print("Press \"Enter\" to capture")

    #user input
    raw_input()

    #take photo
    p = readC.readText(getC.capture(cam), 'caption')
    currentIndex = azureU.uploadImg()
    clarifaiOut =cl.analyse("https://recog.file.core.windows.net/recogimages/image" + str(currentIndex) + ".jpg?sv=2015-12-11&ss=bfqt&srt=sco&sp=rwdlacup&se=2017-01-25T06:11:11Z&st=2017-01-21T22:11:11Z&spr=https,http&sig=ln6d8cXBF4OiQvdVPj1XhZjcfTF3W7aYFGU623t7nac%3D")
    while (p.poll() is None):
        time.sleep(0.5)
    readC.readText(clarifaiOut,'clar')