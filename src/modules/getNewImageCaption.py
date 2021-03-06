import requests as r
import json as j
import SimpleCV as scv


def capture(cam):
    caption=""
    print("getting picture/caption...")
    open_file=open('../keys','r')
    file_lines=open_file.readlines()
    key =file_lines[1].strip()

    #get photo
    cam.getImage().save("img.jpg")


    #url, headers, file location
    url = "https://api.projectoxford.ai/vision/v1.0/analyze?visualFeatures=Description&language=en"
    headers = {'Ocp-Apim-Subscription-Key': key}
    files = {'file': open('img.jpg', 'rb')}

    #sends photo to microsoft and gets info
    response = r.post(url, headers=headers, files=files)

    #parse response
    data = j.loads(response.text)
    caption += data['description']['captions'][0]['text']


    print(caption)
    print("...done")

    return caption