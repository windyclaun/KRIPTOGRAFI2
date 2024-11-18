import binascii

def encrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        plaintext = f.read()
    
    # Pad agar panjangnya kelipatan 16 byte
    padded_plaintext = plaintext + b' ' * (16 - len(plaintext) % 16)

    T = Twofish(key)
    ciphertext = b''

    # Enkripsi blok-blok 16 byte
    for i in range(0, len(padded_plaintext), 16):
        block = padded_plaintext[i:i+16]
        ciphertext += T.encrypt(block)

    with open(output_file, 'wb') as f:
        f.write(ciphertext)
    print(f"File terenkripsi disimpan sebagai: {output_file}")

def decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        ciphertext = f.read()
    
    T = Twofish(key)
    plaintext = b''

    # Dekripsi blok-blok 16 byte
    for i in range(0, len(ciphertext), 16):
        block = ciphertext[i:i+16]
        plaintext += T.decrypt(block)
    
    # Hapus padding yang ditambahkan saat enkripsi
    plaintext = plaintext.rstrip(b' ')

    with open(output_file, 'wb') as f:
        f.write(plaintext)
    print(f"File didekripsi disimpan sebagai: {output_file}")


if __name__ == "__main__":
    # Kunci harus sepanjang 16, 24, atau 32 byte
    key = b'IniKunciRahasia1234'  # Panjang kunci = 16 byte (128-bit)

    # Nama file input dan output
    input_file = 'file_input.txt'
    encrypted_file = 'file_terenkripsi.bin'
    decrypted_file = 'file_didekripsi.txt'

    # Enkripsi file
    encrypt_file(input_file, encrypted_file, key)

    # Dekripsi file
    decrypt_file(encrypted_file, decrypted_file, key)
