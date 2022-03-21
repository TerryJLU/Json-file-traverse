import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)

def readSimpleJsonFile():
    simple_fname=input("Please input simple json file name:")
    with open(os.path.join(BASE_DIR, simple_fname),'r',encoding='utf8') as simple_content:
        try:
            simple_json =  json.load(simple_content)
        except ValueError:
             return False
    return simple_json
          


def readCheckJsonFile():
    check_fname=input("Please input json file name , the file that you want to check:")
    with open(os.path.join(BASE_DIR, check_fname),'r',encoding='utf8') as check_content:
        # Check if the json file data is json format
        try:
            check_json =  json.load(check_content)
        except ValueError:
            return False
    return check_json

aa = readSimpleJsonFile()
bb = readCheckJsonFile()


for key,value in bb.items():
    if (key not in aa):
        print('The json The %s is not exist key' %(key))
    if  (value == '') :
        print('Has null value')
