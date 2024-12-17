from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
response.raise_for_status()
html_text = response.text

soup = BeautifulSoup(html_text, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
article_text = []
article_link = []
for article in articles:
    text = article.get_text()
    article_text.append(text)
    link = article.find(name="a").get("href")
    article_link.append(link)

article_upvote = [int(score.get_text().split()[0]) for score in soup.find_all("span", "score")]

# basecase
highest = article_upvote[0]
for high in article_upvote:
    if high > highest:
        highest = high
# print(article_upvote.index(highest))
get_index = article_upvote.index(highest)
get_text = article_text[get_index]
get_link = article_link[get_index]
print(get_text)
print(get_link)




























# with open("./website.html", mode="r") as web_text:
#     html_text = web_text.read()
#
# soup = BeautifulSoup(html_text, "html.parser")
# print(soup.title)
#
# print(soup.prettify())
#
# all_anchor = soup.find_all(name="a")
# for anchor in all_anchor:
#     print(anchor.get("href"))
#     print(anchor.getText())
