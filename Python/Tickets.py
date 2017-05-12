from bs4 import BeautifulSoup
import requests
from pygame import mixer
from time import sleep
import winsound
c=0
while(True):
    url="https://in.bookmyshow.com/buytickets/john-wick-2-vellore/movie-vell-ET00046519-MT/20170223"
    r=requests.get(url,allow_redirects=True)
    l=[]
    soup=BeautifulSoup(r.content,'html.parser')
    dates=soup.find_all("ul",{"id":"showDates"})
    f=dates[0].find_all("div")
    for i in f:
            l.append(i.text.split())
    print (l)
    for i in l:
            if(i[0]=="26"):
                    winsound.Beep(2500,60000)
    c+=1
    print (c)
    sleep(300)
