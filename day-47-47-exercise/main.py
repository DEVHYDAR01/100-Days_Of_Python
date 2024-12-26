from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()
testing_endpoint = "https://appbrewery.github.io/instant_pot/"

response = requests.get(url=testing_endpoint)
response.raise_for_status()
sample_page = response.text
# print(sample_page)

soup = BeautifulSoup(sample_page, "html.parser")
price = float(soup.find(name="span", class_="aok-offscreen").get_text().split("$")[1])
get_product_title = soup.find(name="span", id="productTitle").get_text()
split_text = get_product_title.split()
product_title = "".join(split_text).replace(",", " ")
# print(product_title)
# print(price)
target_price = 100.00
if price < target_price:
    with smtplib.SMTP(os.getenv("SMTP_ADDRESS"), port=587) as connection:
        connection.starttls()
        connection.login(user=os.getenv("EMAIL_ADDRESS"), password=os.getenv("EMAIL_PASSWORD"))
        connection.sendmail(
            from_addr=os.getenv("EMAIL_ADDRESS"),
            to_addrs="autobirthdaywisherinfo@gmail.com",
            msg=f"Subject: AMAZON PRICE ALERT\n\n{product_title} is now ${price}\n\n{testing_endpoint}".encode()
        )
