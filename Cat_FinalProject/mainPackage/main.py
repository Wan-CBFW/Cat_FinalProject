#main.py
#*****************************************************************************************************************************************
# Names: Trevor Hunt, Nosagie Sherman, JaJuan Hill, Cian Roopnarine                                                                      *
# emails: huntt3@mail.uc.edu, shermani@mail.uc.edu, hill4ju@mail.uc.edu, roopnacn@mail.uc.edu                                            *
# Assignment Number: Final Project                                                                                                       *
# Due Date: 04/23/2024                                                                                                                   *
# Course/Section: IS4010-001                                                                                                             *
# Semester/Year: Spring 2024                                                                                                             *
# Brief Description of the assignment: Collaborative assignment demonstrating working with encryption, JSON, Pillow, txt, lists and more *
#                                                                                                                                        *
# Brief Description of what this module does: Invokes functions in order to display a photo, and print two decrypted messages            *
# Citations:                                                                                                                             *
# Anything else that's relevant:                                                                                                         *
#*****************************************************************************************************************************************
import json
from jsonPackage.json import *
from txtPackage.txt import txtToList
from imagePackage.image import *
from decryptPackage import *
from decryptPackage.decrypt import Decrypt_List, Fernet, Fernet_Decrypt
from cryptography.fernet import Fernet

if __name__ == "__main__":
    text_list = txtToList("UCEnglish.txt")
    hint_list = jsonToList("EncryptedGroupHints Spring 2024 Section 001-1.json")
    decrypted_list = Decrypt_List(text_list, hint_list)
    print(decrypted_list)
    
    Encrypted_Movie_Title = jsonToList("TeamsAndEncryptedMessagesForDistribution - 001.json")
    Str_Movie_Title = Encrypted_Movie_Title[0]                  #Get first and only element in list (turning into string)
    Decrypted_Movie_Title = Fernet_Decrypt(Str_Movie_Title)
    print(Decrypted_Movie_Title.decode())                       #.decode() removes b'
    
    loadImage("Cat_FinalProject.jpg").show()