from task1 import *
from task4 import*
from task5 import*
from pprint import pprint

def analyse_movies_language(movies_list):
    i=0
    list_of_language=[]
    while i<len(movies_list):
        language=(movies_list[i]["language"])
        list_of_language.append(language)
        i=i+1
    all=list_of_language


    pprint(all)
    l=all 
    flat_list = []
    for sublist in l:
        for item in sublist:
            flat_list.append(item)
    pprint (flat_list)


    char_list=flat_list
    i=0
    new_list=[]
    while i<len(char_list):
        j=0
        count=0
        while j<len(char_list):
            if char_list[i]==char_list[j]:
                count=count+1
            j=j+1
        if [char_list[i],count]not in new_list:
            new_list.append([char_list[i],count])
        i=i+1
    main_dict=dict(new_list)
    return(main_dict)
language_analysis = analyse_movies_language(get_movie_details)
# pprint(language_analysis)



