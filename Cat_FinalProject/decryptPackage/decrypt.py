#decrypt.py
#***************************************************************************************************************************************************************
# Names: Trevor Hunt, Nosagie Sherman, JaJuan Hill, Cian Roopnarine                                                                                            *
# emails: huntt3@mail.uc.edu, shermani@mail.uc.edu, hill4ju@mail.uc.edu, roopnacn@mail.uc.edu                                                                  *
# Assignment Number: Final Project                                                                                                                             *
# Due Date: 04/23/2024                                                                                                                                         *
# Course/Section: IS4010-001                                                                                                                                   *
# Semester/Year: Spring 2024                                                                                                                                   *
# Brief Description of the assignment: Collaborative assignment demonstrating working with encryption, JSON, Pillow, txt, lists and more                       *
#                                                                                                                                                              *
# Brief Description of what this module does: Defines functions to decrypt encrypted messages that use Fernet encryption and something similar to a book cipher*
# Citations:https://cryptography.io/en/latest/fernet/, https://www.geeksforgeeks.org/fernet-symmetric-encryption-using-cryptography-module-in-python/          *
# Anything else that's relevant:                                                                                                                               *
#***************************************************************************************************************************************************************
from cryptography.fernet import Fernet
def Decrypt_List(textList, jsonList):
    '''
    Uses given numbers to index into the file and build the decrypted string.
    @param: textList - List of words as the encryption key
    @param: jsonList - Given index numbers
    @return: decrypted string
    '''
    decoded_list = ""
    
    for num in jsonList:    #Loop through, building decrypted string
        newint = int(num)
        if(textList[newint] != "."):
            decoded_list = decoded_list + textList[newint] + " "
        else:   #Removes trailing space before "."
            decoded_list = decoded_list.strip(" ") + textList[newint] + " "
    
    return decoded_list



def Fernet_Decrypt(encrypted_message):
    '''
    Using a Fernet key, this decrypts given messages.
    @param: encrypted_message - given message to be decrypted
    @return: decrypted message
    '''

        # The given Fernet key
    key = b'2tWgZTHycJHttRAQkazCO-Qr66EBdm1mW1-QgCcSzVs='
    
        # Initialize a Fernet cipher instance with the key
    cipher = Fernet(key)
    
        # Decrypt the message
    decrypted_message = cipher.decrypt(encrypted_message)
    
    return decrypted_message