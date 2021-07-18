import requests
from bs4 import BeautifulSoup
import random
import webbrowser
''' .ir = imdb verir
class = titleColumn secondaryInfo çekersen yılını veriyor
class="ratingColumn imdbRating" title çekersen imdb puanını veriyor
href linki verir
.secondary info yılı veriyor.
.title adını veriyor
class="inline canwrap" storyline  veriyor
'''
def string_cleaner(title_changed):
    if "." in title_changed:
        index = title_changed.index(".")
        title_changed = title_changed.replace(' ', '', index + 3)
    return title_changed

def rating_value(link):
    res = requests.get(link)
    soup = BeautifulSoup(res.text, 'html.parser')
    ratingValue = soup.find("span", {"itemprop" : "ratingValue"})
    return str(rating_value)

def gueser_movies(movies):
    guess = random.randint(0, 249)
    link = 'https://www.imdb.com' + movies[guess][1]
    ('Title: ' + movies[guess][0] + ' \nIMDb: ' + rating_value(link))
    speech = movies[guess][0]
    """ while True:
        answer = input('Do you want to open the page? :')
        if answer == 'y':
            webbrowser.open(link)
            break
        else:
            answer = input('Do you want to reroll? ')
            if answer == 'y':
                gueser_movies(movies)
                break
            else :
                break """
    film_link = []
    film_link.append(movies[guess][0])
    film_link.append('https://www.imdb.com' + movies[guess][1])
    return film_link

def get_title(title):
    titles = []
    for idx, item in enumerate(title):
        title1 = item.getText()
        title_changed = title1.replace('\n', '')
        title_changed = string_cleaner(title_changed)
        titles.append(title_changed)
    return titles

def get_link(accessed_links):
    links = []
    for link in accessed_links:
        link_updated = link.get('href')
        if link_updated != None:
            if link_updated.startswith('/title/'):
                links.append(link_updated)
    return  [item for idx,item in enumerate(links) if idx % 2 == 0]

def get_rankings(ratings):
    for idx, item in enumerate(ratings):
        rating_value = item.getText()
        print(rating_value)

def main():
    res = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')
    soup = BeautifulSoup(res.text, 'html.parser')
    title = soup.select('.titleColumn')
    accessed_links = soup.find_all('a')
    movies = list(zip(get_title(title), get_link(accessed_links)))
    return gueser_movies(movies)


if __name__ == '__main__':
    main()

