from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movie_website = response.text
soup = BeautifulSoup(movie_website, "html.parser")

all_movie = []
sam_mov = soup.findAll('h3', class_='title')
print(sam_mov)
for movie_text in sam_mov:
    text = movie_text.getText()
    all_movie.append(text)
movies = all_movie[:: -1]

with open(file="newMovies.txt", mode="w", encoding='utf8') as file:
    for movie in movies:
        file.write(f"{movie}\n")
