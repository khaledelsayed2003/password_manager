🔐 Password Manager (Python + Tkinter)

A lightweight desktop Password Manager built with Python and Tkinter.
Generates strong passwords, auto-copies them to the clipboard, confirms before saving, and stores entries locally.

“Fast to use, simple to read, easy to extend.”

✨ Features

🔑 Strong password generator (letters + digits + symbols)

📋 Auto-copy to clipboard (via pyperclip) on generate

💾 Save credentials (Website | Email | Password) to data.txt

⚠️ Popups for empty fields + Confirm dialog before saving

🧭 Keyboard-friendly: website field focuses on launch

📁 Project Structure
```bash
password_manager/
├─ assets/
│  └─ logo.png
├─ main.py                 # Tkinter UI + save workflow
├─ password_generator.py   # password creation logic (pure Python)
└─ data.txt                # (auto-created) saved entries

▶️ Getting Started
Prerequisites

Python 3.8+

Install dependency
pip install pyperclip

Run
python password_manager/main.py

🧠 How It Works

Generate Password

password_generator.generate_password() returns a random strong string.

fill_generated_password() inserts it into the password field and copies it using pyperclip.copy().

Save Flow (Add button)

Validate fields → warn if any are empty (messagebox.showwarning).

Show confirmation with the details (messagebox.askokcancel).

On OK → append a line to password_manager/data.txt in the format:

<website> | <email> | <password>


Clear inputs and return focus to the website field.

⚙️ Customization

Default email (in main.py):

email_entry.insert(0, "your_email@example.com")


Password recipe (in password_generator.py): tweak counts/symbol set

[random.choice(letters) for _ in range(6)]
[random.choice(numbers) for _ in range(3)]
[random.choice(symbols) for _ in range(2)]
symbols = "!#$%&*()+"


Entry styling (border/color/font) is centralized in entry_style in main.py.

🔒 Important Notes

This app stores credentials in plain text (data.txt) for learning/demo purposes.
For real use, consider:

Encrypting at rest (e.g., cryptography/fernet)

Protecting the file with OS permissions

Avoiding printing passwords in popups/logs

Clipboard contents can be read by other apps—clear it if needed.

🧰 Tech Stack

Python (Tkinter GUI)

pyperclip (clipboard copy)

random / string (secure-ish generation for demo)

✅ To-Do / Ideas

⏸️ Show/Hide password toggle

🔊 Toast/snackbar instead of modal info dialog

🔐 Encrypt data.txt

🔍 Search by website + copy to clipboard

🧪 Unit tests for generator and validators

📜 License

MIT — use, modify, and learn freely.

👤 Author

Khaled Elsayed
Built with ❤️ to practice Tkinter, modular Python, and UX basics.