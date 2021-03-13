from task1 import *
from task4 import*
from task5 import*
from pprint import pprint




def analyse_movies_genre (movies_list):
    i=0
    list_of_genre=[]
    while i<len(movies_list):
        language=(movies_list[i]['gener'])
        list_of_genre.append(language)
        i=i+1
    all_genre= list_of_genre


    # pprint(all_genre)
    genre_list= all_genre
    each_genre_list = []
    for sublist in genre_list:
        for item in sublist:
            each_genre_list.append(item)
    # pprint (each_genre_list)


    main_genre_list=each_genre_list
    i=0
    new_list=[]
    while i<len(main_genre_list):
        j=0
        count=0
        while j<len(main_genre_list):
            if main_genre_list[i]==main_genre_list[j]:
                count=count+1
            j=j+1
        if [main_genre_list[i],count]not in new_list:
            new_list.append([main_genre_list[i],count])
        i=i+1
    main_genre_dic=dict(new_list)
    return(main_genre_dic)
genre_analysis = analyse_movies_genre (get_movie_details)
pprint(genre_analysis)



