import requests as r
import json as j
import SimpleCV as scv
import time as t
import os as o
#----
import talkey
from gtts import gTTS
from pygame import mixer
import subprocess


open_file=open('../keys','r')
file_lines=open_file.readlines()
key =file_lines[1].strip()

#set up cam
cam = scv.Camera()

while(1):
    print("Enter:")

    #user input
    raw_input()

    #take photo
    cam.getImage().save("img.jpg")

    #url, headers, file location
    url = "https://api.projectoxford.ai/vision/v1.0/analyze?visualFeatures=Description&language=en"
    headers = {'Ocp-Apim-Subscription-Key': key}
    files = {'file': open('img.jpg', 'rb')}

    #sends photo to microsoft and gets info
    response = r.post(url, headers=headers, files=files)

    #parse response
    data = j.loads(response.text)
    caption = data['description']['captions'][0]['text']

    print("Reading")
    print(caption)
    tts = gTTS(text=caption, lang='en')
    tts.save("speech.mp3")

    #subprocess.call(["/bin/mv","/tmp/a","/tmp/b"])
    subprocess.Popen(['mpg123', '-q', "speech.mp3"]).wait()

    print("Done")

    #o.rename('img.jpg', data['requestId'] + '.jpg')

