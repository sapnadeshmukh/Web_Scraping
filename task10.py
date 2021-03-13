from pprint import pprint
# from task9 import *
from task5 import*

def   analyse_language_and_directors(movie_list):
    directors_dic={}
    for movie in movie_list:
        for director in movie['director']:
         directors_dic[director]={}
    # return directors_dic
    for i in range(len(movie_list)):
        for director in directors_dic:

            if director in movie_list[i]['director']:
                for language in movie_list[i]['language']:
                    directors_dic[director][language]=0
    for i in range(len(movie_list)):
        for director in directors_dic:
            if director in movie_list[i]['director']:
                for language in movie_list[i]['language']:
                    directors_dic[director][language]=+1
    return directors_dic
director_by_language=analyse_language_and_directors(get_movie_details)
pprint(director_by_language)
