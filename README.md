# 🔐 Password Manager (Tkinter + JSON)

A simple Python GUI app that helps you **generate, save, and search passwords** safely using **Tkinter** and **JSON**.

---

## 🌿 Features

- Generate strong random passwords  
- Save website, email, and password info in a JSON file  
- Search for stored passwords easily  
- Copy generated passwords automatically  
- Handle missing files and empty fields safely  

---

## 🧩 Project Structure  
```bash
password_manager/
├─ assets/
│  ├─ logo.png
│  ├─ app_preview.png
│  ├─ password_generation.png
│  ├─ details_found.png
│  ├─ details_not_found.png
│  ├─ warning_popup.png
│  ├─ confirmation_popup.png
│  ├─ file_not_found.png
│  └─ saved_data(json).png
│
├─ main.py                # Main Tkinter app (save & search logic)
├─ password_generator.py  # Password generator function
└─ README.md              # Project documentation

--- 

##⚙️ Setup & Usage
####📦 Requirements
-Python 3.8+
-Install the required library: pip install pyperclip

---

##🧰 Technologies Used
Purpose	                |                Library
GUI	                    |               Tkinter
Clipboard	            |                Pyperclip
Password_Generation	    |             Random, String
File_Handling	        |            Python Built-ins

---

##🧩 How to Use
###➕ Add a Password

-Fill in Website, Email, and Password fields

-Click Add → info is saved to data.json


###🎲 Generate a Password

-Click Generate Password → a random password is created and copied to clipboard



###🔍 Find a Password

-Enter the website name and click Search → the app shows stored credentials

---

##👨‍💻 Author
Khaled Elsayed
-Built with ❤️ using Python, Tkinter, and modular GUI design principles for a clean, secure, and efficient experience.

##📄 License
This project is for educational and personal use.
© 2025 – Khaled Elsayed.

---
##“Where simplicity meets security — one password at a time.”