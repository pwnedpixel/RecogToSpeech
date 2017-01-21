from azure.storage.file import ContentSettings
from azure.storage.file import FileService
from time import gmtime, strftime

def uploadImg():
    print("uploading...")
    #get key from file
    open_file = open('../keys', 'r')
    file_lines = open_file.readlines()
    key = file_lines[2].strip()

    #upload to server
    file_service = FileService (account_name='recog', account_key=key)
    file_service.create_file_from_path(
        'recogimages',
        None, # We want to create this blob in the root directory, so we specify None for the directory_name
        strftime("%Y-%m-%d-%H-%M-%S", gmtime())+'.jpg',
        'img.jpg',
        content_settings=ContentSettings(content_type='image/jpg'))
    print("...done")