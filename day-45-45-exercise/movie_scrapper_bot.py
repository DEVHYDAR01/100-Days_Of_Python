from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
response.raise_for_status()
html_content = response.text
# print(html_content)

soup = BeautifulSoup(html_content, "html.parser")

all_movie_tags = soup.find_all(name="h3", class_="title")
all_movies = [movie.get_text() for movie in all_movie_tags]
# print(all_movies)
reversed_movies = [movie for movie in all_movies[::-1]]

with open("./movies.txt", mode="w") as movie_file:
    for movie in reversed_movies:
        movie_file.write(movie + "\n")



