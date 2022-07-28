
from bs4 import BeautifulSoup
import urllib.request
import csv
count_getdata=1
def getdata():
    try:
        title=soupnew.find('div',class_='sc-94726ce4-2 khmuXj').h1.text
    except:
        title=None
    try:
        year=soupnew.find('a',class_='ipc-link ipc-link--baseAlt ipc-link--inherit-color sc-8c396aa2-1 WIUyh').text
    except:
        year=None
        # year_release=soupnew.find('li',attrs={'data-testid':"title-details-releasedate"}).div.ul.li.a.text
            # Ở đây lấy date, month, year có dính cả country
    try:
        esrp=soupnew.find('div',class_='sc-94726ce4-3 eSKKHi').ul.text.replace('Video Game','')
    except:
        esrp=None
            # Xóa năm lặp trong esrp
    try:      
        genre=soupnew.find('div',class_='ipc-chip-list__scroller').text
    except:
        genre=None
    try:  
        rate=soupnew.find('div',class_='sc-7ab21ed2-2 kYEdvH').span.text
    except:
        rate=None
    try:
        vote=soupnew.find('div',class_='sc-7ab21ed2-3 dPVcnq').text
    except:
        vote=None
    try:
        country=soupnew.find('li',attrs={'data-testid':"title-details-origin"}).div.ul.li.a.text
    except:
        country=None
    try:
        production_company=soupnew.find('li',attrs={'data-testid':"title-details-companies"}).div.ul.li.a.text
    except:
        production_company=None
    a=[title,year,esrp,genre,rate,vote,country,production_company]
    csv_writer.writerow(a)
    return title,year,esrp,genre,rate,vote,country,production_company

with open("video_game.csv", "w",newline='', encoding='utf-8') as data_game:
    csv_writer = csv.writer(data_game)
    csv_writer.writerow(["Name", "year", "esrp", "genre", "rate", "vote",'country','company'])
    for x in range(1,1000,50):
        link='https://www.imdb.com/search/title/?title_type=video_game&sort=user_rating,desc&start=' + str(x) +'&ref_=adv_nxt'
        page=urllib.request.urlopen(link)
        soup=BeautifulSoup(page,'html.parser',exclude_encodings='utf-8')
        link=soup.find_all('h3',class_='lister-item-header')

        for i in link:
            href=i.a.get('href')
            urlnew='https://www.imdb.com'+str(href)+'?ref_=adv_li_tt'
            pagenew=urllib.request.urlopen(urlnew)
            soupnew=BeautifulSoup(pagenew,'html.parser',exclude_encodings='utf-8') 
            getdata()
            print(count_getdata)
            count_getdata+=1
            
data_game.close()
        
      






    
