def encryption(public_key, plaintext):
    key, n = public_key
    cipher = [pow(ord(char),key)%n for char in plaintext]
    return cipher
