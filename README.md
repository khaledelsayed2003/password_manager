# 🔐 Password Manager  
### A Lightweight Tkinter-Based Desktop App for Secure Password Creation & Storage  
### A simple, modular, and secure tool to generate, copy, and save credentials efficiently.  

---

## 🧭 Overview  
This project is a **Password Manager** built using **Python** and **Tkinter** that allows users to **generate**, **copy**, and **store** secure passwords locally.  
It integrates **clipboard functionality**, **user-friendly GUI**, and **data saving** features in one clean design.  

- The **Password Generator** creates strong, randomized passwords using letters, digits, and symbols.  
- The **Main Application (UI)** handles user interaction, clipboard copy, and saving credentials to a text file.  

Together, these components create a smooth, fast, and secure password management experience.  

---

## 🧩 Project Structure  
```bash
password_manager/
├─ assets/
│   └─ logo.png
│
├─ password_generator.py      # Password creation logic
├─ main.py                    # Tkinter UI + Save workflow
├─ data.txt                   # Auto-generated credentials file
└─ README.md

##✨ Features
🔑 Generate strong passwords with random letters, numbers, and symbols

📋 Auto-copy generated password using pyperclip

💾 Save credentials (Website | Email | Password) to data.txt

⚠️ Pop-up alerts for empty fields and confirmation before saving

🧠 Smart UX with pre-filled email and auto-focus on website input

##⚙️ Setup & Usage
📦 Requirements
Python 3.8+
Install the required library:
pip install pyperclip


##🧰 Technologies Used
Purpose	Library
GUI	Tkinter
Clipboard	Pyperclip
Password Generation	Random, String
File Handling	Python Built-ins


##👨‍💻 Author
Khaled Elsayed
Built with ❤️ using Python, Tkinter, and modular GUI design principles for a clean, secure, and efficient experience.

##📄 License
This project is for educational and personal use.
© 2025 – Khaled Elsayed.

##“Where simplicity meets security — one password at a time.”