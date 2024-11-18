from Cryptodome.Cipher import Twofish
from Crypto.Random import get_random_bytes
import os

# Fungsi untuk menambahkan padding agar data kelipatan 16 byte
def pad(data):
    padding_length = 16 - len(data) % 16
    return data + bytes([padding_length] * padding_length)

# Fungsi untuk menghapus padding setelah dekripsi
def unpad(data):
    padding_length = data[-1]
    return data[:-padding_length]

# Fungsi untuk enkripsi file menggunakan Twofish
def encrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        plaintext = f.read()
    
    cipher = Twofish.new(key, Twofish.MODE_CBC)
    iv = cipher.iv
    padded_text = pad(plaintext)
    ciphertext = cipher.encrypt(padded_text)
    
    with open(output_file, 'wb') as f:
        f.write(iv + ciphertext)
    
    print(f"File '{input_file}' berhasil dienkripsi menjadi '{output_file}'")

# Fungsi untuk dekripsi file menggunakan Twofish
def decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        iv = f.read(16)  # Membaca IV (16 byte pertama)
        ciphertext = f.read()
    
    cipher = Twofish.new(key, Twofish.MODE_CBC, iv=iv)
    decrypted_data = cipher.decrypt(ciphertext)
    plaintext = unpad(decrypted_data)
    
    with open(output_file, 'wb') as f:
        f.write(plaintext)
    
    print(f"File '{input_file}' berhasil didekripsi menjadi '{output_file}'")

# Program utama
if __name__ == "__main__":
    # Membuat kunci Twofish sepanjang 16 byte (128-bit)
    key = get_random_bytes(16)
    print(f"Kunci yang digunakan (hex): {key.hex()}")

    # Masukkan nama file yang ingin dienkripsi
    input_file = input("Masukkan nama file yang akan dienkripsi: ")
    encrypted_file = "encrypted_file.bin"
    decrypted_file = "decrypted_file.txt"

    # Enkripsi file
    encrypt_file(input_file, encrypted_file, key)

    # Dekripsi file
    decrypt_file(encrypted_file, decrypted_file, key)
