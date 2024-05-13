import requests
from bs4 import BeautifulSoup


class User:
    def __init__(self, name, surname, posts, location):
        self.name = name
        self.surname = surname
        self.posts = posts
        self.location = location
        self.wspolrzedne = User.wspolrzedne(self)


    def wspolrzedne(self)-> list:
        url: str = f'https://pl.wikipedia.org/wiki/{self.location}'
        response = requests.get(url)
        response_html = BeautifulSoup(response.text, 'html.parser')
        latitude = response_html.select('.latitude')[1].text.replace(",", ".")
        longitude = response_html.select('.longitude')[1].text.replace(",", ".")
        return [latitude, longitude]



#https: // pl.wikipedia.org / wiki / Zambrów

lucja=User("Lucja", "Tarnowska", posts="10", location="Zambrów")
print(type(lucja.wspolrzedne[0]))


