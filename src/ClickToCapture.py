import modules.getNewImageCaption as getC
import modules.readCaptionAloud as readC

def run():
    while(1):
        print("Enter:")

        #user input
        raw_input()

        #take photo
        readC.readText(getC.capture())