import smtplib
import datetime as dt
import random

my_email = "aliyuahmaad60@gmail.com"
password = ""
now = dt.datetime.now()
day_of_the_week = now.day
if day_of_the_week:
    with open("quotes.txt") as data_quotes:
        content = data_quotes.readlines()
    ran_quote = random.choice(content)
    print(ran_quote)
    connection = smtplib.SMTP(host="smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="tasnimdantanko@gmail.com",
                        msg=f"Subject:HEY BABY\n\n{ran_quote} last try hahaha!".encode("utf-8"))
    connection.close()




