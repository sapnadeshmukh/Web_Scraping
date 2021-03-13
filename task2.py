from task1 import *
from pprint import pprint

def group_by_year(movies):
    years=[]
    for movie in movies:
        year=movie["year"]
        if year not in years:
            years.append(year)
    movie_dict_by_year={index:[] for index in years}
    for index in movies:
        year=index["year"]
        for movieInlist in movie_dict_by_year:
            
            if str(movieInlist)==str(year):
                movie_dict_by_year[movieInlist].append(index)
    return(movie_dict_by_year)
Group_by_year=group_by_year(top_movies)
# pprint(Group_by_year)