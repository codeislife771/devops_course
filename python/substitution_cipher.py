"""
substitution_cipher.py

A Python implementation of a substitution cipher.

This script allows encryption and decryption of text using a randomly-generated substitution cipher key. 
In substitution ciphers, each character of the plaintext is replaced with another character according to a secret key.

Functions:
- make_encryption_key(): Generates a random substitution cipher key.
- compute_dec_key(enc_key): Computes the decryption key (reverse mapping) from the encryption key.
- encrypt_text(text, enc_key): Encrypts plaintext using the provided encryption key.
- decrypt_text(encrypted_text, dec_key): Decrypts ciphertext back to plaintext using the decryption key.
- test_all(): Demonstrates the entire encryption-decryption workflow with an example.

Usage:
Run this script directly to see an example encryption-decryption process:
    python substitution_cipher.py
"""

import random

def make_encryption_key():
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    shuffled_alphabet = alphabet.copy()
    random.shuffle(shuffled_alphabet)

    cipher_key = {}

    for id_letter in range(len(alphabet)):
        alphabet_letter = alphabet[id_letter]

        while alphabet_letter == shuffled_alphabet[id_letter]:
            random.shuffle(shuffled_alphabet)
        else:
            cipher_key[alphabet[id_letter]] = shuffled_alphabet[id_letter]

    cipher_key[" "] = " "

    return cipher_key

def compute_dec_key(enc_key):
    dec_key = {value: key for key, value in enc_key.items()}
    return dec_key

# Encrypt text using the encryption key
def encrypt_text(text, enc_key):
    result_encrypt_text = []
    text = text.strip().lower()
    for letter in text:
        result_encrypt_text.append(enc_key.get(letter, letter))
    return result_encrypt_text

# Decrypt text using the decryption key
def decrypt_text(encrypted_text, dec_key):
    decrypted_text = ""
    for letter in encrypted_text:
        decrypted_text += dec_key.get(letter, letter)
    return decrypted_text

# Demonstration of the complete encryption-decryption process
def test_all():
    print('--------------------------------')
    text = "hello world."
    enc_key = make_encryption_key()
    dec_key = compute_dec_key(enc_key)

    encrypted_text = encrypt_text(text, enc_key)
    decrypted_text = decrypt_text(encrypted_text, dec_key)
    print("Original Text:", text)
    print("Encryption Key:", enc_key)
    print("Decryption Key:", dec_key)
    print("Encrypted Text:", encrypted_text)
    print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
    test_all()
