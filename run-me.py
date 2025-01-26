import os
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import hashlib
import enc_script

# Alert when password is missing
def pass_alert():
    tkinter.messagebox.showinfo("Password Alert", "Please enter a password.")

# Function to handle image encryption
def encrypt():
    global file_path_e
    enc_pass = passg.get()  # Get the entered password

    # Check if password is entered
    if enc_pass == "":
        pass_alert()  # Show alert if no password is entered
    else:
        # Open file dialog for image selection
        filename = askopenfilename()
        file_path_e = os.path.dirname(filename)  # Get the file path of selected image

        # Generate encryption key and IV using SHA-256 hash of password
        hash = hashlib.sha256(enc_pass.encode())
        p = hash.digest()
        key = p  # Use the hash as the encryption key
        iv = p.ljust(16)[:16]  # Use first 16 bytes for IV
        print("Encoding key is: ", key)

        # Read image data
        with open(filename, 'rb') as input_file:
            input_data = input_file.read()

        # Encrypt image data using enc_script
        enc_script.enc_image(input_data, key, iv, file_path_e)

        # Show success message
        tkinter.messagebox.showinfo("Encryption Alert", "Encryption ended successfully. File stored as: encrypted.enc")

# Function to handle image decryption
def decrypt():
    global file_path_e
    enc_pass = passg.get()  # Get the entered password

    # Check if password is entered
    if enc_pass == "":
        pass_alert()  # Show alert if no password is entered
    else:
        # Open file dialog for encrypted file selection
        filename = askopenfilename()
        file_path_e = os.path.dirname(filename)  # Get the file path of selected encrypted file

        # Generate decryption key and IV using SHA-256 hash of password
        hash = hashlib.sha256(enc_pass.encode())
        p = hash.digest()
        key = p  # Use the hash as the decryption key
        iv = p.ljust(16)[:16]  # Use first 16 bytes for IV

        # Read encrypted file data
        with open(filename, 'rb') as input_file:
            input_data = input_file.read()

        # Decrypt image data using enc_script
        enc_script.dec_image(input_data, key, iv, file_path_e)

        # Show success message
        tkinter.messagebox.showinfo("Decryption Alert", "Decryption ended successfully. File stored as: output.png")

# GUI setup
top = Tk()
top.geometry("500x150")
top.resizable(0, 0)
top.title("ImageEncryption")

# Title message
title = "Image Encryption Using AES"
msgtitle = Message(top, text=title)
msgtitle.config(font=('helvetica', 17, 'bold'), width=300)
msgtitle.pack()

# Separator line
sp = "---------------------------------------------------------------------"
sp_title = Message(top, text=sp)
sp_title.config(font=('arial', 12), width=650)
sp_title.pack()

# Password input label and entry
passlabel = Label(top, text="Enter Encryption/Decryption Key:")
passlabel.pack()
passg = Entry(top, show="*", width=20)
passg.config(highlightthickness=1, highlightbackground="blue")
passg.pack()

# Encrypt and Decrypt buttons
encrypt = Button(top, text="Encrypt", width=28, height=3, command=encrypt)
encrypt.pack(side=LEFT)
decrypt = Button(top, text="Decrypt", width=28, height=3, command=decrypt)
decrypt.pack(side=RIGHT)

top.mainloop()
