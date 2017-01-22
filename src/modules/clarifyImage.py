from clarifai.rest import ClarifaiApp
import readCaptionAloud as readL
import subprocess as p

def analyse(imageURL):
    print("sending to clarifai...")
    app = ClarifaiApp()
    response = app.tag_urls([imageURL])
   # print(response)
    conceptArray = response['outputs'][0]['data']['concepts']

    outputArray=[]
    for x in range(0,len(conceptArray)):
        outputArray.insert(len(outputArray),conceptArray[x]['name'])


    things=""
    for x in range(0,4):
       # print(outputArray[x])
        things+=(","+outputArray[x])
        if (x==2):
            things+=" and "

    #readL.readText("I also see...... "+things)
    print("...done")
    return("I also see... "+things)


