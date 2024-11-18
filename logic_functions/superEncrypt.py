from logic_functions.vigenere_c import vigenere_encrypt, vigenere_decrypt
from logic_functions.rsa_c import rsa_encrypt, rsa_decrypt, rsa_generate_keys
import connect as conn

def super_encrypt(plain_text, vigenere_key, public_key):
    # Langkah 1: Enkripsi menggunakan Vigenere
    vigenere_encrypted = vigenere_encrypt(plain_text, vigenere_key)
    
    # Langkah 2: Enkripsi menggunakan RSA
    rsa_encrypted = rsa_encrypt(vigenere_encrypted, public_key)
    rsa_encrypted_text = ' '.join(map(str, rsa_encrypted))
    
    query = "INSERT INTO pesan (plain_text, vigenere_key, rsa) VALUES (%s, %s, %s)"
    params = (plain_text, vigenere_key, rsa_encrypted_text)
    conn.run_query(query, params, fetch=False)
    return rsa_encrypted_text

def super_decrypt(encrypted_text, vigenere_key, private_key):
    # Langkah 1: Dekripsi menggunakan RSA
    rsa_decrypted = rsa_decrypt(encrypted_text, private_key)
    
    # Langkah 2: Dekripsi menggunakan Vigenere
    vigenere_decrypted = vigenere_decrypt(rsa_decrypted, vigenere_key)
    
    return vigenere_decrypted


# Contoh Penggunaan
if __name__ == "__main__":
    # Generate RSA keys
    public_key, private_key = rsa_generate_keys()
    
    # Input data
    text = "HELLO WORLD"
    vigenere_key = "KEY"
    
    # Enkripsi
    encrypted = super_encrypt(text, vigenere_key, public_key)
    print("Encrypted Text:", encrypted)
    
    # Dekripsi
    decrypted = super_decrypt(encrypted, vigenere_key, private_key)
    print("Decrypted Text:", decrypted)
