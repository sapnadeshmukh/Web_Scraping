from task5 import*
from pprint import pprint

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
    while h<1:
        def scrap_movie_details(movie_url):
            page=requests.get(movie_url)
            soup=BeautifulSoup(page.text,"html.parser")  
            title_div=soup.find('div',class_="title_wrapper").h1.get_text()
            movie_name=" "
            for i in title_div:
                if "(" not in i:
                    movie_name=(movie_name+i).strip()
                else:
                    break
            sub_div=soup.find('div',class_="subtext")
            runtime=sub_div.find('time').get_text().strip()
            runtime_hours=int(runtime[0])*60
            movie_runtime=0
            if "min " in runtime:

                runtime_minutes =int(movie_runtime[3:].strip('min'))
                movie_runtime=runtime_hours+runtime_minutes
            else:
                movie_runtime=runtime_hours
            gener=sub_div.find_all('a')
            gener.pop()
            movie_gener=[i.get_text() for i in gener]
            summary=soup.find('div',class_="plot_summary")

            movie_bio=summary.find('div',class_="summary_text").get_text().strip()
            director=summary.find('div',class_="credit_summary_item")
            director_list=director.find_all('a')
            movie_directors=[i.get_text( ).strip() for i in director_list]

            extra_details=soup.find('div',attrs={"class":"article","id":"titleDetails"})
            list_of_divs=extra_details.find_all('div')
            for div in list_of_divs:
                tag_h4=div.find_all('h4')
                for text in tag_h4:
                    if 'Language:' in text:
                        tag_anchor=div.find_all('a')
                        movie_language=[language.get_text() for language in tag_anchor]
                    elif 'Country:' in text:
                        tag_anchor=div.find_all('a')
                        movie_country=''.join([country.get_text() for country in tag_anchor])
            movie_poster_link=soup.find('div',class_="poster") .a['href'] 
            movie_poster="https://www.imdb.com" +movie_poster_link 
            movie_detail_dic={}
            movie_detail_dic["name"]=movie_name
           
            movie_detail_dic["cast"]=all_cast_details_list[h-1]
            cast_details= movie_detail_dic["cast"]
            pprint(movie_detail_dic["name"])

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
            pprint(main_dic)
        url=all_movie_dic[h-1]["url"]
        scrap_movie_details(url)
        h=h+1
analyse_co_actors()
