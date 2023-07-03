from unittest import result
import requests

class theMovieDb:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3"
        self.api_key = "a643f0d974d802d377b159c5fe5fb898"

    def getPopulers(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()

    def getSearchResults(self, keyword):
        response = requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keyword}&page=1")
        return response.json()


movieApi = theMovieDb()

while True:
    secim = input("1- Populer Movies\n2- Search Movies\n3- Exit\nSeçim: ")

    if secim == "3":
        break
    else:
        if secim == "1":
            movies = movieApi.getPopulers()
            for movie in movies["results"]:
                print(movie["title"])

        if secim == "2":
            keyword = input("keyword: ")
            movies = movieApi.getSearchResults(keyword)
            for movie in movies["results"]:
                print(movie["name"])

