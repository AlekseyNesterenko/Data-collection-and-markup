import requests
from lxml import html

all_movies = []


resp = requests.get(url='https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm', 
                    headers = {'User_Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'})

tree = html.fromstring(html=resp.content)

movies = tree.xpath("//table[@data-caller-name='chart-moviemeter']/tbody/tr")

def get_titlemeter(list_element):
    try:
        return(list_element[0].split()[-1])
    except:
        return "no change"

def get_position_change(list_element):
    try:
        return(int(list_element[0].strip()[:-1]))
    except:
        return 0



for movie in movies:
    m = {
        'name' : movie.xpath(".//td[contains(@class, 'titleColumn')]/a/text()")[0],
        'release_year' : movie.xpath(".//td[contains(@class, 'titleColumn')]/span/text()")[0][1:-1],
        'position' : movie.xpath(".//td[contains(@class, 'titleColumn')]/div/text()")[0].split()[0],
        'titlemeter' : (movie.xpath(".//td[contains(@class, 'titleColumn')]/div/span/span/@class")),
        'position_change' : movie.xpath(".//td[contains(@class, 'titleColumn')]/div/span/text()[2]")
    }
    all_movies.append(m)

print(movies)