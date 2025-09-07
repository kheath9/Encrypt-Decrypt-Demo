from cryptography.fernet import Fernet

# Fernet module generates a symmetric key
key = Fernet.generate_key()
f = Fernet(key)

# User enters a message to encrypt
message = input("Enter a short message: ")
encrypted = f.encrypt(message.encode())

# Prints the generated key (for demonstration purposes)
print("key =", key)
# Prints the encrypted message
print("Encrypted message:", encrypted)


# Decrypts and prints the message
decrypted = f.decrypt(encrypted)
print("Decrypted message:", decrypted.decode())
