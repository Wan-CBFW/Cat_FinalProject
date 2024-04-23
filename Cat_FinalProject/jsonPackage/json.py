#json.py 
#****************************************************************************************************************************************
# Names: Trevor Hunt, Nosagie Sherman, JaJuan Hill, Cian Roopnarine                                                                     *
# emails: huntt3@mail.uc.edu, shermani@mail.uc.edu, hill4ju@mail.uc.edu, roopnacn@mail.uc.edu                                           *
# Assignment Number: Final Project                                                                                                      *
# Due Date: 04/23/2024                                                                                                                  *
# Course/Section: IS4010-001                                                                                                            *
# Semester/Year: Spring 2024                                                                                                            *
# Brief Description of the assignment: Collaborative assignment demonstrating working with encryption, JSON, Pillow, txt, lists and more*
# Brief Description of what this module does: Defines function to open and load json file                                               *
# Citations:                                                                                                                            *
# Anything else that's relevant:                                                                                                        *
#****************************************************************************************************************************************
import json

def jsonToList(path):
    '''
    Loads and returns list in json file dictionary under "Cat" key
    @param: json file path
    @return: contents of json file's dictionary under "Cat" key
    '''
    with open(path) as file:
        rawlist = json.load(file)
    jsonList = rawlist["Cat"]
    return jsonList