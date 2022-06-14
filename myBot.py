import requests
import json
import base64
import os

#creates path for images
def specifyPath():
    dir_name = input("Type a directory name: ")
    os.mkdir(dir_name)
#gets raw text image files
def receive_image(prompt, count=0):
    url = 'https://bf.dallemini.ai/generate'

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    data = json.dumps({'prompt':"{}".format(prompt)})
    response = requests.post(url, headers=headers, data=data).text
    parsedResponse = json.loads(response)
    key = "images"
    if(key in parsedResponse):
        print("It worked.")
        return parsedResponse
    else:
        if(count<=5):
            count = count + 1
            print("It didn't work", count)
            receive_image(prompt, count)
#converts text to images and saves them in the generated directory
def image_decoding(dictOfImages):
    for x in range(len(dictOfImages["images"])):
        with open("imageToSave{}.jfif".format(x), "wb") as fh:
            fh.write(dictOfImages["images"][x].decode('base64'))
    print("Check yo' files")

def test():
    with open("test.txt", "wb") as fh:
        fh.write("this is text in a file")  

specifyPath()

#image_prompt = input("Dall-e, draw me: ")
#a = receive_image(image_prompt)
#b = image_decoding(a)