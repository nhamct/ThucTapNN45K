from asyncore import write
from turtle import pd
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import csv

url='https://www.imdb.com/search/title/?title_type=video_game&sort=user_rating,desc&start=151&ref_=adv_nxt'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, "html.parser",exclude_encodings='utf-8')
source=soup.find_all('div',class_='lister-item mode-advanced')
name_game=[]
year_release=[]
genra_game=[]
rate_game=[]
view_game=[]
for link in source:
    name=link.h3.a.text
    name_game.append(name)
    year=link.h3.find('span',class_='lister-item-year text-muted unbold').text.replace("Video Game",'').replace('(','').replace(')','')
    year_release.append(year)
    genre=link.find('p',class_='text-muted').text.replace('\n','')
    genra_game.append(genre)
    rate=link.find('div',class_='inline-block ratings-imdb-rating').text.replace('\n','')
    rate_game.append(rate)
    view=link.find('span',attrs={'name':'nv'}).text
    view_game.append(view)
data={'Name of game':name_game,'Year release':year_release,'genre':genra_game,'rate':rate_game,'view':view_game}
df_game=pd.DataFrame(data)
with open ('data_game2.csv','w',encoding='utf-8') as data_game:
    writer=csv.writer(data_game)
    df_game.to_csv(data_game)




