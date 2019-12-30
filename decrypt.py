def decryption(private_key, ciphertext):
    key, n = private_key
    plain = [chr(pow(char, key)%n) for char in ciphertext]
    plain = ''.join(plain)
    return plain
