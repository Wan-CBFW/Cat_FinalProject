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
if __name__ == "__main__":
    
    #pass
    list_one = jsonToList("EncryptedGroupHints Spring 2024 Section 001-1.json")
    cat_list = list_one["Cat"]
    print(cat_list)
    list_two = jsonToList("TeamsAndEncryptedMessagesForDistribution - 001.json")
    cat_list_two = list_two["Cat"]
    print(cat_list_two)
    
    