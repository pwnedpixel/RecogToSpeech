import modules.getNewImageCaption as getC
import modules.readCaptionAloud as readC
import modules.azureUpload as azureU

cam=getC.scv.Camera()

while(1):
    print("Press \"Enter\" to capture")

    #user input
    raw_input()

    #take photo
    readC.readText(getC.capture(cam))
    azureU.uploadImg()
