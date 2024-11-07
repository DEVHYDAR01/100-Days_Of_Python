import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}

def re_run():
    users_input = input("Enter a word: ").upper()
    convert_to_list = list(users_input)
    try:
        phonetic_words_list = [nato_dict[letter] for letter in convert_to_list]

    except KeyError:
        print("Sorry only letters in the alphabets")
        re_run()
    else:
        print(phonetic_words_list)


re_run()