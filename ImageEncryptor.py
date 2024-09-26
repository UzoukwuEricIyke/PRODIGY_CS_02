import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from cryptography.fernet import Fernet
import os
import zipfile
import cv2
import face_recognition
from stegano import lsb
import pyqrcode
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# Encryption Variables
cipher_suite = Fernet(Fernet.generate_key())

# Function: Google Drive Upload
def upload_to_google_drive(file_path):
    creds = Credentials.from_authorized_user_file('credentials.json', ['https://www.googleapis.com/auth/drive.file'])
    service = build('drive', 'v3', credentials=creds)
    file_metadata = {'name': os.path.basename(file_path)}
    media = MediaFileUpload(file_path, mimetype='application/octet-stream')
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    messagebox.showinfo("Upload Success", f"File uploaded to Google Drive with ID: {file.get('id')}")

# Function: Face recognition for decryption
def verify_face_for_decryption():
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    cam.release()

    if not ret:
        messagebox.showerror("Error", "Failed to capture image from camera.")
        return False

    known_image = face_recognition.load_image_file("authorized_face.png")
    unknown_image = frame

    known_encoding = face_recognition.face_encodings(known_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)

    if len(unknown_encoding) > 0:
        result = face_recognition.compare_faces([known_encoding], unknown_encoding[0])
        if result[0]:
            return True
    return False

# Function: Generate Encryption Key
def generate_key():
    global cipher_suite
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)
    messagebox.showinfo("Key Generated", "New encryption key generated and saved.")

# Function: Encrypt File
def encrypt_file(file_path, compress=False):
    try:
        if compress:
            file_path = compress_file(file_path)
        with open(file_path, "rb") as file:
            file_data = file.read()
            encrypted_data = cipher_suite.encrypt(file_data)

        encrypted_file = file_path + ".enc"
        with open(encrypted_file, "wb") as file:
            file.write(encrypted_data)
        messagebox.showinfo("Success", f"File encrypted and saved as {encrypted_file}")
    except Exception as e:
        messagebox.showerror("Error", f"Encryption failed: {str(e)}")

# Function: Decrypt File
def decrypt_file(file_path):
    try:
        with open(file_path, "rb") as file:
            encrypted_data = file.read()
            decrypted_data = cipher_suite.decrypt(encrypted_data)

        decrypted_file = file_path.replace(".enc", "")
        with open(decrypted_file, "wb") as file:
            file.write(decrypted_data)
        messagebox.showinfo("Success", f"File decrypted and saved as {decrypted_file}")
    except Exception as e:
        messagebox.showerror("Error", f"Decryption failed: {str(e)}")

# Function: Encrypt Camera Image
def encrypt_camera_image():
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    cam.release()

    if ret:
        cv2.imwrite("camera_image.png", frame)
        encrypt_file("camera_image.png")

# Function: Hide Message in Image (Steganography)
def hide_message_in_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        message = tk.simpledialog.askstring("Input", "Enter the message to hide:")
        encrypted_image = lsb.hide(file_path, message)
        encrypted_image.save(file_path + "_stego.png")
        messagebox.showinfo("Success", "Message hidden in the image.")

# Function: Reveal Message from Image (Steganography)
def reveal_message_from_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        hidden_message = lsb.reveal(file_path)
        messagebox.showinfo("Hidden Message", hidden_message if hidden_message else "No message found.")

# Function: Generate QR Code for Key Sharing
def generate_qr_code():
    qr_data = cipher_suite._signing_key.decode('utf-8')
    qr = pyqrcode.create(qr_data)
    qr.show()

# Function: Compress File Before Encryption
def compress_file(file_path):
    zip_file = file_path + ".zip"
    with zipfile.ZipFile(zip_file, 'w') as zipf:
        zipf.write(file_path, os.path.basename(file_path))
    messagebox.showinfo("File Compressed", f"File compressed to {zip_file}")
    return zip_file

# Function: Dark Mode Toggle
def toggle_dark_mode():
    current_bg = root.cget('bg')
    if current_bg == "#f5f5f5":
        root.config(bg="#333333")
        for widget in root.winfo_children():
            widget.config(bg="#333333", fg="#FFFFFF")
    else:
        root.config(bg="#f5f5f5")
        for widget in root.winfo_children():
            widget.config(bg="#f5f5f5", fg="#000000")

# Function: Multi-Language Support (Stub for simplicity)
def change_language(lang):
    messagebox.showinfo("Language Changed", f"Language set to {lang}")

# GUI Setup
root = tk.Tk()
root.title("Image Encryption Tool By EricIyke")
root.geometry("1000x800")
root.config(bg="#f5f5f5")

# Adding title label
title_label = tk.Label(root, text="Image Encryption Tool By EricIyke", font=("Helvetica", 24), bg="#f5f5f5", fg="#FF5733")
title_label.pack(pady=20)

# Adding horizontal layout for features
feature_frame = tk.Frame(root, bg="#f5f5f5")
feature_frame.pack(pady=10)

# Create scrollable frame for options
canvas = tk.Canvas(feature_frame, bg="#f5f5f5")
scrollbar = tk.Scrollbar(feature_frame, orient="horizontal", command=canvas.xview)
scrollable_frame = tk.Frame(canvas, bg="#f5f5f5")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(xscrollcommand=scrollbar.set)

# Add options to the scrollable frame
def add_buttons_to_gui():
    # Multi-Language Dropdown
    language_menu = ttk.Combobox(scrollable_frame, values=["English", "French", "Spanish"], state='readonly')
    language_menu.set("Select Language")
    language_menu.pack(side="left", padx=10)
    language_menu.bind("<<ComboboxSelected>>", lambda event: change_language(language_menu.get()))

    # Select Encryption Algorithm
    encryption_menu = ttk.Combobox(scrollable_frame, values=["Fernet", "AES", "RSA"], state='readonly')
    encryption_menu.set("Select Encryption Algorithm")
    encryption_menu.pack(side="left", padx=10)

    # Toggle Dark Mode Button
    dark_mode_button = tk.Button(scrollable_frame, text="Toggle Dark Mode", command=toggle_dark_mode)
    dark_mode_button.pack(side="left", padx=10)

    # Key generation button
    generate_key_button = tk.Button(scrollable_frame, text="Generate Encryption Key", command=generate_key)
    generate_key_button.pack(side="left", padx=10)

    # Encrypt file button
    encrypt_file_button = tk.Button(scrollable_frame, text="Select File to Encrypt", command=lambda: encrypt_file(filedialog.askopenfilename()))
    encrypt_file_button.pack(side="left", padx=10)

    # Decrypt file button
    decrypt_file_button = tk.Button(scrollable_frame, text="Select File to Decrypt", command=lambda: decrypt_file(filedialog.askopenfilename()))
    decrypt_file_button.pack(side="left", padx=10)

    # Compress File Before Encryption Checkbox
    compress_var = tk.IntVar()
    compress_checkbox = tk.Checkbutton(scrollable_frame, text="Compress File Before Encryption", variable=compress_var)
    compress_checkbox.pack(side="left", padx=10)

    # Upload to Google Drive Button
    upload_drive_button = tk.Button(scrollable_frame, text="Upload Encrypted File to Google Drive", command=lambda: upload_to_google_drive(filedialog.askopenfilename()))
    upload_drive_button.pack(side="left", padx=10)

    # Verify Face for Decryption Button
    verify_face_button = tk.Button(scrollable_frame, text="Verify Face for Decryption", command=verify_face_for_decryption)
    verify_face_button.pack(side="left", padx=10)

    # Encrypt Image from Camera Button
    encrypt_camera_button = tk.Button(scrollable_frame, text="Encrypt Image from Camera", command=encrypt_camera_image)
    encrypt_camera_button.pack(side="left", padx=10)

    # Hide Message in Image Button
    hide_message_button = tk.Button(scrollable_frame, text="Hide Message in Image", command=hide_message_in_image)
    hide_message_button.pack(side="left", padx=10)

    # Reveal Message from Image Button
    reveal_message_button = tk.Button(scrollable_frame, text="Reveal Message from Image", command=reveal_message_from_image)
    reveal_message_button.pack(side="left", padx=10)

    # Generate QR Code Button
    qr_button = tk.Button(scrollable_frame, text="Generate QR Code for Key Sharing", command=generate_qr_code)
    qr_button.pack(side="left", padx=10)

# Add buttons to GUI
add_buttons_to_gui()

# Configure the scrollable canvas
canvas.pack(side="top", fill="both", expand=True)
scrollbar.pack(side="bottom", fill="x")

# Run the GUI main loop
root.mainloop()
