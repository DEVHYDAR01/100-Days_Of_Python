file = open("my_file.txt", mode="a")
content = file.write("\n How are you!")
print(content)
file.close()