#ceaser cipher 

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text_def, shift_def, direction_def):
    if direction_def == 'encode':
        new_alph1 = alphabet[:shift_def]
        changed_alph = alphabet + new_alph1

    #encrypt message
        encrypt_msg = ""
        for letter in text_def:
            letter_idx = alphabet.index(letter)
            letter_idx_moved = letter_idx + shift_def
            # 'if letter_idx_moved > 25: # endrer ikke på lista. men restarter idx nummeret.
            #     letter_idx_moved -= 25 '
            encrypt_msg += changed_alph[letter_idx_moved]
        print(f'{encrypt_msg} encrypted')

    else:

#decrypt message 
        new_alph2 = alphabet[-shift_def:]
        changed_alph1 = new_alph2 + alphabet   

        
        decrypt_msg = ""
        for letter in text_def:
            letter_idx = changed_alph1.index(letter)
            # print(letter_idx)
            letter_idx_moved = letter_idx - shift_def
            decrypt_msg += changed_alph1[letter_idx_moved]

        print(f'{decrypt_msg} decrypted')
    

encrypt(text_def=text, shift_def= shift, direction_def=direction)










# def decrypt(text, shift):
#     new_alph1 = alphabet[-shift:]
#     changed_alph = new_alph1 + alphabet   
#     print(changed_alph)
    
#     decrypt_msg = ""
#     for letter in text:
#         letter_idx = changed_alph.index(letter)
#         print(letter_idx)
#         letter_idx_moved = letter_idx - shift
#         # print(letter_idx_moved)
#         decrypt_msg += changed_alph[letter_idx_moved]

#     print(f'{decrypt_msg} decrypted')

# decrypt('djwjmjabujpo', 1)
# #civilization




