from azure.storage.file import ContentSettings
from azure.storage.file import FileService
from time import gmtime, strftime
import json as j

def uploadImg():
    print("uploading...")

    #get api key from file
    open_file = open('../keys', 'r')
    file_lines = open_file.readlines()
    key = file_lines[2].strip()
    file_service = FileService(account_name='recog', account_key=key)

    #fetch the index file from server
    file_service.get_file_to_path('recogimages', None, 'current.txt', '../current.txt')

    #open the index file and get the index value
    open_file = open('../current.txt', 'r')
    file_lines = open_file.readlines()
    data = j.loads(file_lines[0])
    currentIndex = data['index']
    open_file.close()

    #increase the index
    currentIndex+=1

    #upload picture to server
    file_service.create_file_from_path(
        'recogimages',
        None, # We want to create this blob in the root directory, so we specify None for the directory_name
        strftime("image"+str(currentIndex), gmtime())+'.jpg',
        'img.jpg',
        content_settings=ContentSettings(content_type='image/jpg'))

    #open index file in write mode, and write new index
    open_file = open('../current.txt', 'w')
    open_file.writelines("{\"index\":"+str(currentIndex)+"}")
    open_file.close()

    #upload index file back to server
    file_service.create_file_from_path(
        'recogimages',
        None,  # We want to create this blob in the root directory, so we specify None for the directory_name
        'current.txt',
        '../current.txt',
        content_settings=ContentSettings(content_type='text/plain'))


    print("...done")