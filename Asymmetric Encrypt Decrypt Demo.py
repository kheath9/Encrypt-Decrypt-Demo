from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

# Generate private and public keys using RSA
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# User enters a message to encrypt
message = input("Enter a short message: ")

# Public key is used to encrypt user's message
encrypted = public_key.encrypt(message.encode(), padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                              algorithm=hashes.SHA256(), label=None))

# Prints the generated key (for demonstration purposes)
print("public key = ", public_key)
print("private key = ", private_key)

# Prints the encrypted message
print("Encrypted message:", encrypted)

# Decrypts the message with the private key
decrypted = private_key.decrypt(encrypted, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                        algorithm=hashes.SHA256(), label=None))

# Prints the decrypted message
print("Decrypted message:", decrypted.decode())
