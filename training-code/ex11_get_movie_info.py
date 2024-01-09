import requests
from pprint import pprint

apikey = 'aa9e49f'
url = 'https://www.omdbapi.com/'


def get_movies(search_text: str) -> list:
    payload = dict(s=search_text, apikey=apikey)
    r = requests.get(url, params=payload)
    # print(f'r.status_code is {r.status_code}')
    return r.json()['Search']


def get_movie_details(imdbID: str) -> dict:
    payload = dict(i=imdbID, apikey=apikey)
    r = requests.get(url, params=payload)
    return r.json()


if __name__ == '__main__':
    search_term = input('Enter search term: ')
    filename = search_term.replace(' ', '_') + '.txt'

    movies = get_movies(search_term)
    try:
        with open(filename, mode='w') as file:
            for m in movies:
                file.write(f'Title: {m["Title"]}\n')
                movie_details = get_movie_details(m['imdbID'])
                file.write(f'Plot: {movie_details["Plot"]}\n')
                file.write(f'Poster: {m["Poster"]}\n')
                file.write('-'*50)
                file.write('\n')
        print(f'Details saved in file {filename}')
    except OSError as err:
        print(f'something went wrong - {err}')


