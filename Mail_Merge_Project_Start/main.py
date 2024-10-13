guests = []
with open("./Input/Names/invited_names.txt") as get_invite_names:
    for name in range(8):
        name_invites = get_invite_names.readline().strip()
        guests.append(name_invites)

for invites in guests:
    file = open("./Input/Letters/starting_letter.txt")
    content = file.read()
    replaced = content.replace('[name]', f'{invites}')
    with open(f"./Output/ReadyToSend/letter_for_{invites}.docx", mode="w") as to_write:
        to_write.write(replaced)


#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp