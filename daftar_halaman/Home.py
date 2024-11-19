import streamlit as st
from logic_functions.superEncrypt import super_encrypt, super_decrypt
from logic_functions import rsa_c as rsa
from logic_functions import steganografi
from logic_functions import fileEncrypt as fileC
from Crypto.Random import get_random_bytes

def menu(page):
    if page == "Text":
        st.title("CatEyeProctor : Sistem Pengumpulan Laporan Kecurangan Ujian")
        st.header("Text Super Encryption dengan Vigenere dan RSA")
        option = st.radio("Pilih", ("Encrypt", "Decrypt"))
        
        if option == "Encrypt":
            text_to_encrypt = st.text_area("Masukkan teks untuk dienkripsi")
            vegenere_key = st.text_input("Masukkan Kunci Vigenere")
            if st.button("Encrypt"):
                public_key, private_key = rsa.rsa_generate_keys()
                encrypted_text = super_encrypt(text_to_encrypt, vegenere_key, public_key)
                st.markdown("<p style='color:red;'>Encrypted Text:</p>", unsafe_allow_html=True)
                st.write(encrypted_text)
        
        elif option == "Decrypt":
            text_to_decrypt = st.text_area("Masukkan teks untuk didekripsi")
            vigenere_key = st.text_input("Masukkan Kunci Vigenere")
            if st.button("Decrypt"):
                public_key, private_key = rsa.rsa_generate_keys()
                encrypted_list = list(map(int, text_to_decrypt.split()))
                decrypted_text = super_decrypt(encrypted_list, vigenere_key, private_key)
                st.write("Decrypted Text:", str(decrypted_text))
                
    elif page == "Steganography":
        st.title("CatEyeProctor : Sistem Pengumpulan Laporan Kecurangan Ujian")
        st.header("Steganoggraphy :  Sembunyikan pesan dalam gambar")
        option = st.radio("Pilih", ("Encrypt", "Decrypt"))
        
        if option == "Encrypt":
            image_file = st.file_uploader("Upload gambar", type=["jpg", "png", "jpeg"])
            text = st.text_area("Masukkan teks untuk disembunyikan")
            if st.button("Encrypt"):
                if not image_file or not text:
                    st.warning("Upload gambar dan masukkan teks")
                    return
                output_image_path = 'stenography.png'
                hidden_image = steganografi.embed_msg(image_file, output_image_path, text)
                st.write("Image saved to", hidden_image)
                with open(output_image_path, "rb") as file:
                    st.download_button(
                        label="Download gambar tersembunyi",
                        data=file,
                        file_name="stenography.png",
                        mime="image/png"
                    )
        elif option == "Decrypt":
            image = st.file_uploader("Upload gambar", type=["jpg", "png", "jpeg"])
            if st.button("Decrypt"):
                decoded_text = steganografi.extract_msg(image)
                st.write("Decrypt Text:", decoded_text)
        
    elif page == "File":
        st.title("CatEyeProctor : Sistem Pengumpulan Laporan Kecurangan Ujian")
        st.header("Enkripsi dan Dekripsi File dengan Blowfish")
        option = st.radio("Pilih", ("Encrypt", "Decrypt"))
        if option == "Encrypt":
                input_file = st.file_uploader("Upload file untuk di enkripsi", type=["txt", "pdf", "docx"])
                key = st.text_input("Masukkan kunci (4-56 bytes)")
                
                if input_file:
                    if st.button("Encrypt"):
                        if len(key) < 4 or len(key) > 56:
                            st.warning("Kunci harus 4 sampai 56 bytes")
                        else:
                            encrypted_file_path = fileC.encrypt_file(input_file, key)
                            st.success(f"File '{input_file.name}' successfully encrypted to '{encrypted_file_path}'")
                            with open(encrypted_file_path, "rb") as file:
                                st.download_button(
                                    label="Download encrypted file",
                                    data=file,
                                    file_name=encrypted_file_path.split("/")[-1],
                                    mime="application/octet-stream"
                                )

        elif option == "Decrypt":
            input_file = st.file_uploader("Upload file untuk di decrypt", type=["bin"])
            key = st.text_input("Masukkan kunci (4-56 bytes)")
            
            if input_file:
                if st.button("Decrypt"):
                    if len(key) < 4 or len(key) > 56:
                        st.warning("kunci harus 4 sampai 56 bytes")
                    else:
                        decrypted_file_path = fileC.decrypt_file(input_file, key)
                        st.success(f"File '{input_file.name}' successfully decrypted to '{decrypted_file_path}'")
                        with open(decrypted_file_path, "rb") as file:
                            st.download_button(
                                label="Download decrypted file",
                                data=file,
                                file_name=decrypted_file_path.split("/")[-1],
                                mime="application/octet-stream"
                            )

    else:
        st.write("404 Not Found")