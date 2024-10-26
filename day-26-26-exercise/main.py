import pandas

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

users_input = input("Enter a word: ").upper()
convert_to_list = list(users_input)
phonetic_words_list = [nato_dict[letter] for letter in convert_to_list if letter in nato_dict]
print(phonetic_words_list)


