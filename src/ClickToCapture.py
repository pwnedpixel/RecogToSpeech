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
    clarifaiOut =cl.analyse("https://recog.file.core.windows.net/recogimages/image" + str(
        currentIndex) + ".jpg?sv=2015-12-11&ss=bqtf&srt=sco&sp=rwdlacup&se=2017-01-22T04:13:20Z&sig=0FcOC1Ge0r9Ms047P7el57ci1OOzU9%2B%2Fb1BzOU9TWn0%3D")
    while (p.poll() is None):
        time.sleep(0.5)
    readC.readText(clarifaiOut,'clar')