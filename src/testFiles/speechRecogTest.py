import speech_recognition as sr
import pyaudio

p = pyaudio.PyAudio()
print(p.get_default_input_device_info())
r = sr.Recognizer()
with open('../keys','r') as f:
    BING_KEY=f.readline().strip()

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
            print("CaptureTask")
    except sr.UnknownValueError:
        print("Microsoft Bing Voice Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))
