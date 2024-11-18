import streamlit as st
from logic_functions.superEncrypt import super_encrypt, super_decrypt
from logic_functions import rsa_c as rsa
from logic_functions import steganografi


def menu(page):
    if page == "Text":
        st.title("Text Encryption and Decryption")
        st.header("Super Encryption dengan Vigenere dan RSA")
        option = st.radio("Choose an option", ("Encrypt", "Decrypt"))
        
        if option == "Encrypt":
            text_to_encrypt = st.text_area("Enter text to encrypt")
            vegenere_key = st.text_input("Enter Vigenere Key")
            if st.button("Encrypt"):
                public_key, private_key = rsa.rsa_generate_keys()
                encrypted_text = super_encrypt(text_to_encrypt, vegenere_key, public_key)
                st.write(":green[Encrypted Text:]")
                st.write(encrypted_text)
        
        elif option == "Decrypt":
            text_to_decrypt = st.text_area("Enter text to decrypt")
            vigenere_key = st.text_input("Enter Vigenere Key")
            if st.button("Decrypt"):
                public_key, private_key = rsa.rsa_generate_keys()
                encrypted_list = list(map(int, text_to_decrypt.split()))
                decrypted_text = super_decrypt(encrypted_list, vigenere_key, private_key)
                st.write("Decrypted Text:", str(decrypted_text))
                
    elif page == "Steganography":
        st.title("Steganography")
        st.header("Hide text in an image")
        option = st.radio("Choose an option", ("Encode", "Decode"))
        
        if option == "Encode":
            image_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
            text = st.text_area("Enter text to hide")
            if st.button("Encode"):
                if not image_file or not text:
                    st.warning("Please upload an image and enter text to hide")
                    return
                output_image_path = 'stenography.png'
                hidden_image = steganografi.embed_msg(image_file, output_image_path, text)
                st.write("Image saved to", hidden_image)
                with open(output_image_path, "rb") as file:
                    st.download_button(
                        label="Download encoded image",
                        data=file,
                        file_name="stenography.png",
                        mime="image/png"
                    )
        elif option == "Decode":
            image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
            if st.button("Decode"):
                decoded_text = steganografi.extract_msg(image)
                st.write("Decoded Text:", decoded_text)
        
    elif page == "File":
        st.write("File")    
    else:
        st.write("404 Not Found")