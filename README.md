# Image Encryption & Decryption Using AES

This project implements a secure image encryption and decryption system using the **AES (Advanced Encryption Standard)** algorithm. The system is designed to ensure the confidentiality of images sent over potentially insecure transmission channels. By leveraging AES encryption, the image data is rendered unreadable to unauthorized users, ensuring that only those with the correct decryption key can restore the image to its original form. This project aims to demonstrate the power of AES encryption in protecting sensitive information like medical, military, and other confidential images.

## Features:
- **Image Encryption:** Encrypt any image using a password-protected AES algorithm, making it unreadable to unauthorized parties.
- **Image Decryption:** Decrypt encrypted images back to their original format using the same password used during encryption.
- **Password Protection:** A password is required to encrypt and decrypt the image, ensuring that only authorized users can access the data.
- **Graphical User Interface (GUI):** Built with Python’s Tkinter library, the GUI is user-friendly and allows users to easily select images, enter passwords, and encrypt/decrypt images with a click of a button.
- **Easy File Management:** Select files directly from the system’s file explorer, making it simple to choose images for encryption or decryption.

## How It Works:
1. **Image Selection:** The user selects an image file using a file dialog.
2. **Password Input:** The user enters a password that will be used as the encryption/decryption key.
3. **Encryption/Decryption Process:** Based on the user’s choice, the program either encrypts or decrypts the selected image using AES encryption with a 256-bit key generated from the password.
4. **Output:** After the encryption or decryption is completed, the processed image is saved in the same directory as the input file.

## System Requirements:
- Python 3.x
- Required Libraries:
  - Tkinter
  - PIL (Python Imaging Library)
  - hashlib
  - custom script for encryption (`enc_script.py`)

## Usage:
- To **encrypt** an image, click the **Encrypt** button, select the image, and provide a password.
- To **decrypt** an encrypted image, click the **Decrypt** button, select the encrypted image, and enter the password used during encryption.

This project is ideal for users who need a simple yet secure way to protect image data for sensitive applications such as medical imaging, government documents, or military communication.

## Code Structure:
- **Main Python File (`image_encryption.py`)**: Contains the logic for image encryption, decryption, and the Tkinter GUI setup.
- **Encryption Script (`enc_script.py`)**: A custom script for handling AES encryption and decryption of image files.
- **Image Processing**: Utilizes AES-256 encryption to ensure high-level security for images.

## Project Report Highlights:
The project leverages the **AES algorithm** for encryption and decryption to secure image data during transmission. The core objective is to provide an encryption system that ensures the confidentiality of image files, particularly in fields that handle sensitive information. Through this system, users can securely send and receive images over a network without the risk of unauthorized access or modification.

## Future Improvements:
- Implement support for different encryption keys for each encryption cycle.
- Enhance the system to support multiple file formats beyond images.
- Add more advanced encryption algorithms for added security options.

---

## Author
Muhammad Abubakkar Kaleem  
BSCS, FAST-NUCES (2018–2022)  
This project was created as part of the **Information Security System** course project.
