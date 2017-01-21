import talkey
from gtts import gTTS
from pygame import mixer
import subprocess

def readText(textToRead):
    print("reading...")
    tts = gTTS(text=textToRead, lang='en')
    tts.save("speech.mp3")
    print("...done")

    #subprocess.call(["/bin/mv","/tmp/a","/tmp/b"])
    subprocess.Popen(['mpg123', '-q', "speech.mp3"]).wait()