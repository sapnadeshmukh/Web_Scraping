from task5 import*
from task1 import*

from pprint import pprint
import json
import os

all_movie_dic=top_movies
i=0
all_movie_url=[]
all_movie_name=[]
while i <len(all_movie_dic):
    movie_name=all_movie_dic[i]["name"]
    all_movie_name.append(movie_name)
    url=all_movie_dic[i]["url"]
    all_movie_url.append(url)
    i=i+1
   
def analyse_co_actors():
    
        h=0
        full_actor_coactor=[]
        while h<250:
            def scrap_movie_details(movie_url):
                movie_detail_dic={}
                movie_detail_dic["name"]=movie_name
                movie_detail_dic["cast"]=all_cast_details_list[h-1]
                cast_details= movie_detail_dic["cast"]
                # pprint(movie_detail_dic["name"])
                index=0
                actor_imdb_id=cast_details[index]["imdb_id"]
                actor_name=(cast_details[index]["name"])
                main_dic={}
                inner_dic={}
                detail_list=[]
                second_inner_dic={}
                inner_dic["name"]=actor_name
                co_actor_imdb_id=cast_details[1]["imdb_id"]
                co_actor_name=cast_details[1]["name"]
                second_inner_dic["imdb_id"]=co_actor_imdb_id
                second_inner_dic["name"]=co_actor_name
                second_inner_dic["num_movies"]=0
                detail_list.append(second_inner_dic)
                inner_dic["frequent_co_actors"]=detail_list
                main_dic[actor_imdb_id]=inner_dic
                # pprint(main_dic)
                main1_dic={}
                main_list=[]
                main1_dic[actor_imdb_id]=actor_name
                main1_dic[co_actor_imdb_id]=co_actor_name
                # pprint(main1_dic)
                main_list.append(actor_name)
                main_list.append(co_actor_name)
                a=main_list
                # pprint(main_list)
                full_actor_coactor.append(a)
                
            url=all_movie_dic[h-1]["url"]
            scrap_movie_details(url)

            h=h+1
        pprint(full_actor_coactor)
       

analyse_co_actors()
