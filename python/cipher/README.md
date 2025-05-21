# 🔐 Python Random Substitution Cipher

A small command-line tool for encrypting and decrypting text using a randomly generated substitution cipher.

---

## 📖 Overview

This project demonstrates:

- Generating a **random substitution key** that never maps a character to itself.  
- Encrypting and decrypting arbitrary text via that key.  
- A simple interactive terminal interface.

Everything is written in pure Python, with no external dependencies beyond the standard library.

---

## 🚀 Features

- **Key Generation**  
  Creates a bijective mapping of characters (letters, digits, punctuation, space), ensuring no character maps to itself.
- **Encryption & Decryption**  
  - `encrypt_text(text, key)`  
  - `decrypt_text(text, inv_key)`
- **Built-In Tests**  
  - `test_key(key)` verifies your cipher key is valid.  
  - `test_all()` runs a full encrypt/decrypt cycle and confirms the result matches the original.
- **Interactive Shell**  
  A user-friendly loop to choose between encrypt, decrypt, or quit.

---

## 📂 File Structure

<pre> 
├── random_substitution_cipher.py   # Core functions
│   ├── make_encryption_key()
│   ├── compute_dec_key()
│   ├── encrypt_text()
│   ├── decrypt_text()
│   ├── test_key()
│   └── test_all()
│
├── encryption_decryption_cli.py    # Interactive CLI
│   ├── intract_with_user()
│   ├── create_enc_and_dec_keys()
│   ├── print_description_to_user()
│   ├── encrypt_user_text()
│   ├── decrypt_user_text()
│   └── handle_command_from_user()
│
└── README.md # Project overview & instructions </pre>

## 🔧 Installation

1. Clone this repository:  
   ```bash
   git clone https://github.com/your-username/devops_course.git
   cd devops_course

    # (Optional) Create and activate a virtual environment:
        python3 -m venv venv
        source venv/bin/activate




## ▶️ Usage
1. **How To Run The Script**
    ```bash
    #Run the interactive CLI with:
    python encryption_decryption_cli.py

    #You’ll see your generated keys printed at startup, then:
    #Type enc to encrypt a line of text.
    #Type dec to decrypt a line of text.
    #Type q to quit.



2. **Launch the CLI**  
   ```bash
   python encryption_decryption_cli.py
   ---------------------
    "enc"  Encrypt Text
    "dec"  Decrypt Text
    "q"    Quit

    > enc
    Enter text to encrypt> Hello, World!
    Encrypted Text: "Xy9$z..."

    > dec
    Enter text to decrypt> Xy9$z...
    Decrypted Text: "Hello, World!"

    > q
    Bye bye! See you next time!