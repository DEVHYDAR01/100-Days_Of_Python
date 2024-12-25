from bs4 import BeautifulSoup
import requests
import smtplib

testing_endpoint = "https://appbrewery.github.io/instant_pot/"

response = requests.get(url=testing_endpoint)
response.raise_for_status()
sample_page = response.text
# print(sample_page)

soup = BeautifulSoup(sample_page, "html.parser")
price = float(soup.find(name="span", class_="aok-offscreen").get_text().split("$")[1])
print(price)


