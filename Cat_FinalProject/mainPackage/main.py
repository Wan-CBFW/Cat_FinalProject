#main.py
#*********************************************************************************************************
# Names: Trevor Hunt, [], [], []                                                    *
# emails: huntt3@mail.uc.edu, [], [], []                                 *
# Assignment Number: Final Project                                                                       *
# Due Date: 04/23/2024                                                                                   *
# Course/Section: IS4010-001                                                                             *
# Semester/Year: Spring 2024                                                                             *
# Brief Description of the assignment: []                      *
#                                                                                                        *
# Brief Description of what this module does: [] *
# Citations:                                                       *
# Anything else that's relevant:                                                                         *
#*********************************************************************************************************
import json
from jsonPackage.json import *
from txtPackage.txt import txtToList
if __name__ == "__main__":
    #pass
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
    

    
    