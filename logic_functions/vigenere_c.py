def vigenere_encrypt(plaintext, key):
    ciphertext = ''
    key = key.upper()
    key_length = len(key)
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            char = chr((ord(char) - offset + ord(key[key_index]) - ord('A')) % 26 + offset)
            key_index = (key_index + 1) % key_length
        ciphertext += char
    return ciphertext


def vigenere_decrypt(ciphertext, key):
    plaintext = ''
    key = key.upper()
    key_length = len(key)
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            char = chr((ord(char) - offset - (ord(key[key_index]) - ord('A')) + 26) % 26 + offset)
            key_index = (key_index + 1) % key_length
        plaintext += char
    return plaintext


# Contoh Penggunaan
# if __name__ == "__main__":
#     text = "HelloWorld"
#     key = "KEY"
    
#     encrypted = vigenere_encrypt(text, key)
#     print("Encrypted:", encrypted)
    
#     decrypted = vigenere_decrypt(encrypted, key)
#     print("Decrypted:", decrypted)
