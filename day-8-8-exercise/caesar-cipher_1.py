#!/usr/bin/env python3

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
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
    print(f"The encoded text is {encrypted_to_string}")

def decrypt(text, shift):
    list_of_alpha = []
    for i in range(shift, len(alphabet)):
        get_alpha = alphabet[i]
        get_letter = list_of_alpha.append(get_alpha)

    for i in range(0, shift):
        get_remainder = alphabet[i]
        append_to_end = list_of_alpha.append(get_remainder)

    list_of_text = []
    for i in range(len(text)):
        get_text = text[i]
        if get_text in list_of_alpha:
            get_index = list_of_alpha.index(get_text)
            put_to_list = list_of_text.append(get_index)

    decrypted = []
    for i in list_of_text:
        if i < len(alphabet):
            get_the_encrypt = alphabet[i]
            append_encrypt = decrypted.append(get_the_encrypt)
    decrypted_to_string = "".join(decrypted)
    print(f"The decoded text is {decrypted_to_string}")

#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == 'encode':
    encrypt(text, shift)
elif direction == 'decode':
    decrypt(text, shift)
else:
    print("enter what you want me to do: ")