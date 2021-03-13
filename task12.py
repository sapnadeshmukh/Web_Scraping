import requests
import json
from bs4 import BeautifulSoup
from pprint import pprint
from task1 import*
import os

all_movie_dic=top_movies
def movie_list(movie):
    details={}
    listUrl=[]
    movieList= movie
    return movieList
movies_detail_list = movie_list(all_movie_dic)
# pprint(movies_detail_list)
listOfUrl=[]
for i in movies_detail_list:
    url=i["url"]
    listOfUrl.append(url)

def all_movies_cast():
    i=0
    castOfmovie=[]
    while i<len(listOfUrl):

        def scrape_movie_cast(movie_caste_url):
            movie_id=''
            for _id in movie_caste_url[27:]:
                if '/' not in _id:
                    movie_id=movie_id + _id
                else:
                    break
            file_name=movie_id+"_cast.json"
            # print(file_name)
            text=None
            if os.path.exists(file_name):
                # print("From cashing data:---")
                f=open( file_name)
                text=f.read()
                text=json.loads(text)
                return text
            if text is None:
                print("Non cashing data:---")
                row=requests.get(movie_caste_url)
                soup=BeautifulSoup(row.text,'html.parser')
                table_data=soup.find('table',class_='cast_list')
                actors=table_data.findAll('td',class_='')
                cast_list=[]
                for actor in actors:
                    actor_dict={}
                    imdb_id=actor.find('a').get('href')[6:15]
                    name=actor.getText().strip()
                    actor_dict['imdb_id']=imdb_id
                    actor_dict['name']=name
                    cast_list.append(actor_dict.copy())
                all_director= cast_list
                with open(file_name, "w") as outfile: 
                    json.dump(all_director, outfile,indent=4) 
                return all_director
        # user_scrap_cast=int(input("enter any movie index:--"))
        user_for_scrap_cast=(listOfUrl[i])
        user_url=(str(user_for_scrap_cast))
        # pprint(user_url)
        # print("Movie Name:-",movies_detail_list[i]["name"])
        main_url=user_url+"fullcredits?ref_=tt_cl_sm#cast"
        result=scrape_movie_cast(main_url)
        castOfmovie.append(result)
        i=i+1
    return (castOfmovie)
all_cast_details_list=all_movies_cast()
# pprint(all_cast_details_list)










