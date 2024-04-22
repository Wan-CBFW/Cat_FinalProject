#main.py
#*****************************************************************************************************************************
# Names: Trevor Hunt, Nosagie Sherman, JaJuan Hill, Cian Roopnarine                                                          *
# emails: huntt3@mail.uc.edu, shermani@mail.uc.edu, hill4ju@mail.uc.edu, roopnacn@mail.uc.edu                                *
# Assignment Number: Final Project                                                                                           *
# Due Date: 04/23/2024                                                                                                       *
# Course/Section: IS4010-001                                                                                                 *
# Semester/Year: Spring 2024                                                                                                 *
# Brief Description of the assignment: Collaborative assignment demonstrating working with JSON, Pillow, txt, lists and more *
#                                                                                                                            *
# Brief Description of what this module does: Invokes functions in order to display a photo, and print two decrypted messages*
# Citations:                                                                                                                 *
# Anything else that's relevant:                                                                                             *
#*****************************************************************************************************************************
import json
from jsonPackage.json import *
from txtPackage.txt import txtToList
from imagePackage.image import *
if __name__ == "__main__":
    text_list = txtToList("UCEnglish.txt")
    list_one = jsonToList("EncryptedGroupHints Spring 2024 Section 001-1.json")
    cat_list = list_one["Cat"]
    decoded_list_one = []
    
    for num in cat_list:
        newint = int(num)
        decoded_list_one.append(text_list[newint])
    print(decoded_list_one)
    
    list_two = jsonToList("TeamsAndEncryptedMessagesForDistribution - 001.json")
    key = list_two["Cat"]
    print(key)
    
    loadImage("Cat_FinalProject.jpg").show()