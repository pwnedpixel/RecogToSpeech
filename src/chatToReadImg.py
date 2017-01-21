import speech_recognition as sr
import pyaudio
#----
import requests as req
import json as j
import SimpleCV as scv
import time as t
import os as o
#----
import talkey
from gtts import gTTS
from pygame import mixer
import subprocess

#setup audio
p = pyaudio.PyAudio()
print(p.get_default_input_device_info())
r = sr.Recognizer()

#set up cam
cam = scv.Camera()

#retrieve keys
with open('../keys','r') as f:
    file_lines=f.readlines()
    BING_KEY=file_lines[0].strip()
    VISION_KEY=file_lines[1].strip()

print(BING_KEY)

while(1):
    
    with sr.Microphone() as source:
        #.adjust_for_ambient_noise(source)
        r.energy_threshold=16500
        print(r.energy_threshold)
        
        print("Say something!")
        audio = r.listen(source)
        
        print("end listen")
    try:
        output=r.recognize_bing(audio, key=BING_KEY)
        print("Microsoft Bing Voice Recognition thinks you said " + output)
        if "take picture" in output:
            #--important code
            #take photo
            cam.getImage().save("img.jpg")

            #url, headers, file location
            url = "https://api.projectoxford.ai/vision/v1.0/analyze?visualFeatures=Description&language=en"
            headers = {'Ocp-Apim-Subscription-Key': VISION_KEY}
            files = {'file': open('img.jpg', 'rb')}

            #sends photo to microsoft and gets info
            response = req.post(url, headers=headers, files=files)

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

    except sr.UnknownValueError:
        print("Microsoft Bing Voice Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))
