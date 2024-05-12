#!/usr/bin/env python3
from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if shift > len(alphabet):
    shift = shift % 25

def caesar(text, shift, direction):
    if direction == 'encode':
        list_of_text = []
        for i in range(len(text)):
            get_text = text[i]
            if get_text in alphabet:
                get_index = alphabet.index(get_text)
                put_to_list = list_of_text.append(get_index)

        list_of_alpha = []
        for i in range(shift, len(alphabet)):
            get_alpha = alphabet[i]
            get_letter = list_of_alpha.append(get_alpha)
            
        for i in range(0, shift):
            get_remainder = alphabet[i]
            append_to_end = list_of_alpha.append(get_remainder)

        encrypted = []
        for i in list_of_text:
            if i < len(list_of_alpha):
                get_the_encrypt = list_of_alpha[i]
                append_encrypt = encrypted.append(get_the_encrypt)
                encrypted_to_string = "".join(encrypted)
        print(f"The {direction}d text is {encrypted_to_string}")
    elif direction == 'decode':
        list_of_alpha = []
        for i in range(shift, len(alphabet)):
            get_alpha = alphabet[i]
            get_letter = list_of_alpha.append(get_alpha)
            
        list_of_text = []
        for i in range(len(text)):
            get_text = text[i]
            if get_text in alphabet:
                get_index = list_of_alpha.index(get_text)
                put_to_list = list_of_text.append(get_index)
        
        for i in range(0, shift):
            get_remainder = alphabet[i]
            append_to_end = list_of_alpha.append(get_remainder)
        decrypted = []
        for i in list_of_text:
            if i < len(alphabet):
                get_the_encrypt = alphabet[i]
                append_encrypt = decrypted.append(get_the_encrypt)
                decrypted_to_string = "".join(decrypted)
        print(f"The {direction}d text is {decrypted_to_string}")

caesar(text, shift, direction)
