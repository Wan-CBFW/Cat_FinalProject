#decrypt.py

from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"my deep dark secret")
token
b'...'
f.decrypt(token)
b'my deep dark secret'

from cryptography.fernet import Fernet


# Your Fernet key (you should store this securely)
key = b'2tWgZTHycJHttRAQkazCO-Qr66EBdm1mW1-QgCcSzVs='

# Your Fernet-encrypted message
encrypted_message = b'gAAAAABlTNM6E_sG85Z7exRFRBnvBhpDhL4rzknNKiPZGnjR_Zem2ZxvlzxwyyoyS3ixtb6Hz_REgEGhTKMWJzJkDy3Slqj49g=='

# Initialize a Fernet cipher instance with the key
cipher = Fernet(key)

# Decrypt the message
decrypted_message = cipher.decrypt(encrypted_message)

print("Decrypted message:", decrypted_message.decode())
