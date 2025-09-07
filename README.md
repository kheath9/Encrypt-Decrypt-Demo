# Encrypt-Decrypt-Demo

The symmetric demo uses the Fernet module from the Python cryptography library to generate a symmetric key. The key is then used to encrypt a short message entered by the user. The program then prints the ecrypted message and then uses the generated key to decrypt, and finally prints the decrypted message. 

The asymmetric demo uses cryptography's hazmat module to generate a public and private key using RSA. A private key is generated using the recommended public exponent size and a standard 2048 bit key size. The public key is then generated from the private key. The SHA256 hash function protects the integrity of the message and OAEP padding ensures the randomness of the cyphertext. The private key is then used to decrypt the user's message, and the decrypted message is finally printed.  
