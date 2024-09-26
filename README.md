This project is part of my internship with Prodigy InfoTech, and I’m excited to share it with the community.

Project Overview

This Python-based tool allows users to protect their images by encrypting them, hiding messages within images, and sharing encryption keys through QR codes. It is designed with a simple but feature-packed GUI using *Tkinter* and integrates modern technologies such as *Google Drive uploads*, *Facial Recognition* for decryption, and *Image Steganography*.

  Features

The *Image Encryption Tool By EricIyke* includes the following features:

1. *Multi-Language Support*: Supports multiple languages for wider accessibility.
2. *Select Encryption Algorithm*: Choose between different encryption algorithms (e.g., Fernet, AES, RSA).
3. *Generate Encryption Key*: Create a secure encryption key that can be used to encrypt and decrypt images.
4. *Select File to Encrypt*: Choose an image file for encryption.
5. *Select File to Decrypt*: Choose an encrypted file for decryption.
6. *Compress File Before Encryption*: Option to compress files before encrypting to save storage space.
7. *Upload Encrypted File to Google Drive*: Upload encrypted images directly to your Google Drive for safekeeping.
8. *Verify Face for Decryption*: Use your camera to verify the user’s face before allowing decryption of an image.
9. *Encrypt Image from Camera*: Capture an image from your camera and encrypt it in one go.
10. *Hide Message in Image*: Use steganography to hide secret messages within an image.
11. *Reveal Message from Image*: Extract hidden messages from encrypted images.
12. *Generate QR Code for Key Sharing*: Generate and share QR codes for encryption keys, allowing easy key sharing.
13. *Toggle Dark Mode*: Switch between dark and light mode for a better visual experience.

https://github.com/user-attachments/assets/990156db-99da-45ae-ae4c-dc36d26111ac



Installation

To use this tool, follow these steps:

1. Clone the repository:

`git clone https://github.com/UzoukwuEricIyke/PRODIGY_CS_02`

2. Navigate to the project directory:

`cd PRODIGY_CS_02`

3. Install the required dependencies:

`pip install -r requirements.txt`

4. Run the program:

`python ImageEncryptor.py`

  Dependencies

The tool uses several Python libraries to implement the various features:

- *Tkinter*: For building the graphical user interface (GUI).
- *Cryptography*: For handling encryption algorithms like Fernet, AES, and RSA.
- *OpenCV*: For capturing images from the camera.
- *Face Recognition*: For facial verification to ensure authorized access.
- *Stegano*: For hiding and revealing messages in images.
- *Google API*: For uploading files to Google Drive.
- *PyQRCode*: For generating QR codes for key sharing.
- *Zipfile*: For compressing files before encryption.

  How to Use

1. *Launch the Tool*: Run `ImageEncryptor.py` to open the GUI.
2. *Select Encryption Algorithm*: Choose from a variety of encryption algorithms depending on your security needs.
3. *Generate a Key*: If required, generate an encryption key to use for encrypting and decrypting your images.
4. *Encrypt/Decrypt Files*: Upload or capture an image to encrypt or decrypt.
5. *Additional Features*: Explore options like hiding messages, uploading to Google Drive, verifying with face recognition, etc.

  Contributions

Contributions are welcome. If you have suggestions for improving the tool or find bugs, feel free to fork the repo, make your changes, and submit a pull request.

  Contact

For further information or inquiries, please contact:

  *Uzoukwu Eric Ikenna*  
  Email: [uzoukwuericiyke@yahoo.com](mailto:uzoukwuericiyke@yahoo.com)
  LinkedIn - https://www.linkedin.com/in/uzoukwu-eric-ikenna/

Thank you for using the Image Encryption Tool By EricIyke. I hope it meets your encryption and security needs.
