#!/usr/bin/env python3

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    list_of_text = []
    for i in range(len(text)):
        get_text = text[i]
        if get_text in alphabet:
            get_index = alphabet.index(get_text)
            put_to_list = list_of_text.append(get_index)
    print(list_of_text)

    list_of_alpha = []
    for i in range(shift, len(alphabet)):
        get_alpha = alphabet[i]
        get_letter = list_of_alpha.append(get_alpha)
    print(list_of_alpha)

    for i in range(0, shift):
        get_remainder = alphabet[i]
        append_to_end = list_of_alpha.append(get_remainder)
    print(list_of_alpha)

    for i in list_of_text:
        if i < len(list_of_alpha):
            print(list_of_alpha[i])
    print(shift)

encrypt(text, shift)