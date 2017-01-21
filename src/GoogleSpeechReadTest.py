import talkey
from gtts import gTTS
from pygame import mixer
import subprocess


print("STart")
tts = gTTS(text='This is a Test. Do not panic.', lang='en')
tts.save("speech.mp3")
print("End")

#subprocess.call(["/bin/mv","/tmp/a","/tmp/b"])
subprocess.Popen(['mpg123', '-q', "speech.mp3"]).wait()
