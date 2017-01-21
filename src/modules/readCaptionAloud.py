import subprocess
import requests as r
import json

def readText(textToRead):
    open_file = open('../keys', 'r')
    file_lines = open_file.readlines()
    nmaid = file_lines[3].strip()
    nmaidKey = file_lines[4].strip()


    print("reading...")
    url = "https://nim-rd.nuance.mobi:9443/nina-webapi/TTS/"
    headers = {'nmaid': nmaid, 'nmaidkey':nmaidKey, 'Content-Type':'application/json'}
    body = {
        'text': textToRead,
        'tts-type': 'text',
        'user': 'http_sample'
        }
    print("send post")
    response = r.post(url, headers=headers, data=json.dumps(body))
    print("got response")
    print(response)

    print("...done")

    #subprocess.call(["/bin/mv","/tmp/a","/tmp/b"])
    subprocess.Popen(['mpg123', '-q', "speech.mp3"]).wait()