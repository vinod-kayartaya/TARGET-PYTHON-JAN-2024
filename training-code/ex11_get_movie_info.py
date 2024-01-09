import requests
from pprint import pprint


def get_movies(search_text: str) -> list:
    apikey = 'aa9e49f'
    url = f'https://www.omdbapi.com/'
    payload = dict(s=search_text, apikey=apikey)
    r = requests.get(url, params=payload)
    # print(f'r.status_code is {r.status_code}')
    return r.json()['Search']


if __name__ == '__main__':
    movies = get_movies('spider')
    pprint(movies)
