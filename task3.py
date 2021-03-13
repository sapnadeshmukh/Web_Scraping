from task1 import *
from task2 import *
from pprint import pprint

def group_by_decade(movies):
    dic_of_movies={}
    list1=[]
    for movie in movies:
        movie_year=movie%10
        decade=movie-movie_year
        if decade not in list1:
            list1.append(decade)
    list1.sort()
    for year in list1:

        
        dic_of_movies[year]=[]
    for year in dic_of_movies:
        decaderange=year+9
        for x in movies:
            if x<=decaderange and x>=year:
                for v in movies[x]:
                    dic_of_movies[year].append(v)
    return(dic_of_movies)
Dic_of_movies=group_by_decade(Group_by_year)
# pprint(Dic_of_movies)