🔐 Password Manager

A lightweight desktop application built with Python and Tkinter for managing and generating secure passwords — with auto-copy functionality and instant save confirmation.

💡 Simple. Secure. Built for learning modular Python & clean UI design.

🧭 Overview

This Password Manager helps users generate, copy, and store strong passwords securely on their local machine.
It combines Tkinter GUI, randomized password logic, and clipboard integration for a smooth, efficient experience.

✨ Key Features

🔑 Generate strong passwords (letters, digits & symbols)

📋 Auto-copy generated password using pyperclip

💾 Save credentials (Website | Email | Password) to data.txt

⚠️ Popup alerts for empty fields and confirmation before saving

🧠 Smart UX — email pre-filled, website auto-focused

🧩 Project Structure
password_manager/
├─ assets/
│  └─ logo.png
│
├─ password_generator.py     # Password creation logic
├─ main.py                   # Tkinter UI + Save workflow
├─ data.txt                  # Auto-generated credentials file
└─ README.md

🧠 How It Works
1️⃣ Generate Password

Uses random and string modules

Randomly selects a mix of letters, digits, and symbols

Automatically copies the password to clipboard (pyperclip.copy())

pwd = generate_password()
pyperclip.copy(pwd)
password_entry.insert(0, pwd)

2️⃣ Save Data

When the user clicks Add:

Checks if any fields are empty → shows a warning popup

Displays a confirmation dialog with all info

On confirmation → appends credentials to data.txt:

website | email | password


Clears textboxes & refocuses the cursor on Website entry

⚙️ Setup & Usage
📦 Requirements

Python 3.8+

Install the required dependency:

pip install pyperclip

▶️ Run the App
python password_manager/main.py

🖥️ UI Overview
Component	Description
🧱 Canvas Logo	Displays app logo (assets/logo.png)
🧾 Entries	Website, Email/Username, Password
⚙️ Buttons	Generate Password → creates + copies password
Add → saves credentials
💚 Styling	Highlighted entries, soft colors, modern fonts
🧰 Tech Stack
Purpose	Library
GUI	Tkinter
Clipboard	Pyperclip
Password Generation	Random, String
File Handling	Python built-ins
🧩 Example Saved Data
google.com | user@gmail.com | @Pa$$w0rd12
github.com | khaled@dev.com | A8!tg9#Kp

⚡ Code Highlights

🧩 Modular password generation file (password_generator.py)

🧠 Smart UX with dynamic focus and popups

🧾 Messagebox confirmation before saving

📋 Clipboard copy for quick paste

🚀 Future Enhancements

🔒 Encrypt data.txt (AES or Fernet)

🔍 Search & filter by website

💡 Add password strength meter

🌐 Export/Import to JSON or CSV

👨‍💻 Author

Khaled Elsayed
Built with ❤️ using Python, Tkinter, and clean modular structure to practice GUI and UX principles.

📜 License

MIT License — free to use and modify.

“Where simplicity meets security — one password at a time.”