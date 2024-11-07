import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}

is_on = True
while is_on:
    try:
        users_input = input("Enter a word: ").upper()
        convert_to_list = list(users_input)
        phonetic_words_list = [nato_dict[letter] for letter in convert_to_list]
        print(phonetic_words_list)
        is_on = False
    except KeyError:
        print("Sorry only letters in the alphabets")
        