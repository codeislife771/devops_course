import  random_substitution_cipher
import json

def intract_with_user():
    enc_and_dec_keys = create_enc_and_dec_keys()
    random_substitution_cipher.save_enc_dec__keys_to_json_file()
    print_create_enc_and_dec()
    print_description_to_user()
    
    while True:
        user_command = handle_command_from_user(enc_and_dec_keys)

        if user_command == 'q':
            print('Bye bye! See you next time!')
            break
              
def create_enc_and_dec_keys():
    encryped_keys = random_substitution_cipher.make_encryption_key()
    decrypted_keys = random_substitution_cipher.compute_dec_key(encryped_keys)
    encpyted_and_decypted_keys = {"dec_keys":decrypted_keys, "enc_keys": encryped_keys}
    return(encpyted_and_decypted_keys)

def print_create_enc_and_dec():
    enc_and_dec_keys = create_enc_and_dec_keys()
    print('---------------------')
    print('Create Encrypted Keys:\n',enc_and_dec_keys['enc_keys'])
    print('Create Decrypted Keys:\n',enc_and_dec_keys['dec_keys'])

def print_description_to_user():
    print('''
---------------------
"enc" For Encrypt Text
"dec" For Decrypt Text
"q"   For Exit''')
    
def encrypt_user_text(user_command_enc,encryped_keys):
    user_encrypted_text = random_substitution_cipher.encrypt_text(user_command_enc, encryped_keys)
    return user_encrypted_text

def decrypt_user_text(user_command_dec,decryped_keys):
    user_encrypted_text = random_substitution_cipher.encrypt_text(user_command_dec, decryped_keys)
    return user_encrypted_text

def save_encrypted_text_to_file(user_encrypted_text):
    encrypted_text_file = open("encrypted_text.json", 'w')
    json.dump(user_encrypted_text, encrypted_text_file)
    encrypted_text_file.close()
    
def handle_user_enc_choise(enc_and_dec_keys):
    
    user_command_enc = input('Enter text to encrypt> ') 
    user_encrypted_text = encrypt_user_text(user_command_enc,enc_and_dec_keys['enc_keys'])
    
    user_command_enc = input('Do you want to save the encrypted text to a file? (y/n)> ') 
    if user_command_enc == 'y':
        print('Saving encrypted text "encrypted_text.json" to a file...')
        save_encrypted_text_to_file(user_encrypted_text)
    
    return user_encrypted_text

def handle_user_dec_choise(enc_and_dec_keys):
        # do function decrypted text 
        user_command_dec = input('Enter text to decrypt> ') 
        user_decrypted_text = decrypt_user_text(user_command_dec,enc_and_dec_keys['dec_keys'])
        return user_decrypted_text

def return_enc_and_dec_by_user_choise(user_command, enc_and_dec_keys):
    if user_command == 'enc':
        user_encrypted_text = handle_user_enc_choise(enc_and_dec_keys)
        print(f'Encrypted Text: "{user_encrypted_text}"')
        return user_encrypted_text
    else:
        if user_command == 'dec':
            dec_choise = handle_user_dec_choise(enc_and_dec_keys)
            print(f'Deccrypted Text: "{dec_choise}"')
            return dec_choise 

def handle_command_from_user(enc_and_dec_keys):
    while True:
        user_command = input('> ')
        if user_command == "q":
            return user_command
        # quit_if_q_letter(user_command)  
        elif user_command not in ['enc', 'dec']:
            print_description_to_user()
            
        else:
            return_enc_and_dec_by_user_choise(user_command, enc_and_dec_keys)

if __name__ == "__main__":
    
    intract_with_user()
