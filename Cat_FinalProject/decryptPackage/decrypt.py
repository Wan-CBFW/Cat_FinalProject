#decrypt.py
from cryptography.fernet import Fernet
def Decrypt_List(textlist, jsonlist):
    decoded_list = ""
    for num in jsonlist:
        newint = int(num)
        decoded_list = decoded_list+ textlist[newint] + " "
    return decoded_list



def Fernet_Decrypt(encrypted_message):
    

    # Your Fernet key (you should store this securely)
    key = b'2tWgZTHycJHttRAQkazCO-Qr66EBdm1mW1-QgCcSzVs='
    
    # Your Fernet-encrypted message
    
    
    # Initialize a Fernet cipher instance with the key
    cipher = Fernet(key)
    
    # Decrypt the message
    decrypted_message = cipher.decrypt(encrypted_message)
    
    return decrypted_message
