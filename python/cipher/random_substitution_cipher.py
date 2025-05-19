"""
random_substitution_cipher.py

A Python implementation of a random substitution cipher.

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
    python random_substitution_cipher.py
"""

import random
import string

def make_encryption_key():
    # Step 1: Build character list to encrypt
    char = " " + string.ascii_lowercase + string.digits + string.punctuation
    char = list(char)

    # Step 2: Shuffle until valid (no character maps to itself)
    while True:
        shuffled_char = char.copy()
        random.shuffle(shuffled_char)

        # long way
        # is_valid = True
        # for original, shuffled in zip(char, shuffled_char):
        #     if original == shuffled:
        #         is_valid = False
        #         break

        # if is_valid:
        #     break

        # short way
        if all(original != shuffled for original, shuffled in zip(char, shuffled_char)): break
        

    # Step 3: Build final encryption key
    cipher_key = {}
    for original, shuffled in zip(char, shuffled_char):
        cipher_key[original] = shuffled

    return cipher_key

def compute_dec_key(enc_key):
    dec_key = {value: key for key, value in enc_key.items()}
    return dec_key

def encrypt_text(text, enc_key):
    result_encrypt_text = []
    for letter in text:
        result_encrypt_text.append(enc_key.get(letter, letter)) 
        
    return ''.join(result_encrypt_text)

def decrypt_text(encrypted_text, dec_key):
    decrypted_text = ""
    for letter in encrypted_text:
        decrypted_text += dec_key.get(letter, letter)
    return decrypted_text

def test_key(cipher_key):
    values = list(cipher_key.values())
    if len(values) != len(set(values)):
        print("❌ Test failed: Duplicate values in cipher_key!")
    elif any(k == v for k, v in cipher_key.items()):
        print("❌ Test failed: Some characters map to themselves!")
    else:
        print("✅ Test passed: Valid cipher key.")

def test_all():
    print('--------------------------------')
    text = "hello world. test123!"
    enc_key = make_encryption_key()
    dec_key = compute_dec_key(enc_key)

    encrypted_text = encrypt_text(text, enc_key)
    decrypted_text = decrypt_text(encrypted_text, dec_key)

    print("Original Text:     ", repr(text))
    print("Encrypted Text:    ", encrypted_text)
    print("Decrypted Text:    ", repr(decrypted_text))
    print("Match?             ", text == decrypted_text)

    test_key(enc_key)

if __name__ == "__main__":
    test_all()
