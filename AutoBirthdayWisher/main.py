##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import smtplib
import pandas
import random
import datetime as dt

my_email = "aliyuahmaad60@gmail.com"
password = ""

list_of_letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

now = dt.datetime.now()
present_day = now.day
present_month = now.month

df = pandas.read_csv("birthdays.csv")
for (index, row) in df.iterrows():
    if (present_day and present_month) == (row["day"] and row["month"]):
        get_ran_letter = random.choice(list_of_letters)
        with open(f"./letter_templates/{get_ran_letter}") as ran_file:
            content = ran_file.readlines()
            replaced = content[0].replace("[NAME]", f"{row["name"]}")
            content[0] = replaced
            stringed_content = ''.join(content)
        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=f"{row["email"]}",
            msg=f"SUBJECT: HAPPY BIRTHDAY\n\n{stringed_content} sorry if you got this mail i am just testing something")
        connection.close()







