#json.py 

import json

def jsonToList(path):
    with open(path) as file:
        jsonlist = json.load(file)
    return jsonlist
    