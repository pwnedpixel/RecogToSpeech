import talkey
from gtts import gTTS
from pygame import mixer
import subprocess
import time

p=subprocess

def readText(textToRead, fileName):
    print("reading...")
    tts = gTTS(text=textToRead, lang='en')
    tts.save(fileName+".mp3")
    print("...done talking")

    #subprocess.call(["/bin/mv","/tmp/a","/tmp/b"])
    p = subprocess.Popen(['mpg123', '-q', fileName+".mp3"])

    return p