# 🔐 Secure Password Generator (Python)

This is a command-line **secure password generator** built with Python. It uses the `secrets` module for cryptographically secure randomization—ideal for generating strong, unpredictable passwords for personal or professional use.

## 🚀 Features

- Customizable password length (minimum: 8 characters)
- Option to include:
  - Uppercase letters
  - Lowercase letters
  - Digits
  - Symbols
- Auto-copies the generated password to your clipboard
- Option to generate multiple passwords in a loop
- Clears the terminal for a cleaner UI

## 🛠️ Technologies Used

- Python 3.x
- `secrets` — secure random number generation
- `string` — character sets
- `pyperclip` — clipboard support
- `os` and `time` — terminal and delay management

## 🧠 Why `secrets`?

Unlike the `random` module, `secrets` is designed for **cryptographic security**. This means passwords generated using `secrets` are much harder to predict, keeping you safe from brute-force attacks or seed-guessing exploits.

## 📦 Requirements

Install the required Python library:
```bash
pip install pyperclip
