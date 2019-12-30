import key_gen
import encrypt
import decrypt


print("RSA Encrypter/ Decrypter")

public, private = key_gen.generate_key()
print('Public key: ',*public)
print('Private key: ',*private)

message = input("Enter a message to encrypt: ")

encrypted_msg = encrypt.encryption(public, message)
print("Encrypted message: ")
print([str(x) for x in encrypted_msg])
print("\n........\n")

decrypted_msg = decrypt.decryption(private, encrypted_msg)
print("Decrypted message: "+decrypted_msg)
