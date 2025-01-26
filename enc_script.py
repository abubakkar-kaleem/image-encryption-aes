from Crypto.Cipher import AES

# Function to encrypt image data
def enc_image(input_data, key, iv, filepath):
    """
    Encrypts the provided image data using AES encryption in CFB mode.

    Args:
        input_data (bytes): The raw data of the image to be encrypted.
        key (bytes): The AES encryption key.
        iv (bytes): The AES initialization vector.
        filepath (str): The directory where the encrypted file will be saved.
    """
    # Create AES cipher object using the key and IV, with CFB mode
    cfb_cipher = AES.new(key, AES.MODE_CFB, iv)
    
    # Encrypt the input image data
    enc_data = cfb_cipher.encrypt(input_data)

    # Write the encrypted data to a new file
    with open(filepath + "/encrypted.enc", "wb") as enc_file:
        enc_file.write(enc_data)  # Save the encrypted data as 'encrypted.enc'

# Function to decrypt image data
def dec_image(input_data, key, iv, filepath):
    """
    Decrypts the provided encrypted image data using AES decryption in CFB mode.

    Args:
        input_data (bytes): The encrypted data to be decrypted.
        key (bytes): The AES decryption key.
        iv (bytes): The AES initialization vector.
        filepath (str): The directory where the decrypted file will be saved.
    """
    # Create AES cipher object for decryption using the same key and IV, with CFB mode
    cfb_decipher = AES.new(key, AES.MODE_CFB, iv)
    
    # Decrypt the encrypted data
    plain_data = cfb_decipher.decrypt(input_data)

    # Write the decrypted data to a new file
    with open(filepath + "/output.png", "wb") as output_file:
        output_file.write(plain_data)  # Save the decrypted image as 'output.png'
