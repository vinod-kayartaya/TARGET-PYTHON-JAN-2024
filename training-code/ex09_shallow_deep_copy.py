from pprint import pprint
import json

if __name__ == '__main__':
    p1 = dict(fname='Vinod', phones=['9731424784'], emails={'official': 'vinod@vinod.co'})
    p2 = p1.copy()
    p3 = json.loads(json.dumps(p1))
    p1['phones'].append('9844083934')
    p2['emails']['personal'] = 'kayartaya.vinod@gmail.com'

    pprint(p1)
    pprint(p2)
    pprint(p3)

    movie_info_str = '{"Title":"Along Came a Spider","Year":2001,"Rated":"R","Released":"06 Apr 2001","Runtime":"104 min","Genre":"Drama, Thriller","Director":"Lee Tamahori","Writer": null,"Actors":"Morgan Freeman, Michael Wincott, Monica Potter","Plot":"When a senator\'s daughter under Secret Service protection is kidnapped from a private school, detective Alex Cross investigates the case even though he\'s recovering from the loss of his partner.","Language":"English, Russian","Country":"United States, Germany, Canada","Awards":"1 win & 1 nomination","Poster":"https://m.media-amazon.com/images/M/MV5BOTVlY2VhMWEtYmRlOC00YWVhLWEzMDktZWJlYzNiMWJmZTIwXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"6.4/10"},{"Source":"Rotten Tomatoes","Value":"32%"},{"Source":"Metacritic","Value":"42/100"}],"Metascore":"42","imdbRating":"6.4","imdbVotes":"94,762","imdbID":"tt0164334","Type":"movie","DVD":"21 Jan 2010","BoxOffice":"$74,078,174","Production":null,"Website":null,"Response":true}'
    movie_info = json.loads(movie_info_str)
    pprint(movie_info)
