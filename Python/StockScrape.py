import requests
from bs4 import BeautifulSoup
k=0
f=open("C:\\Users\\manmeet_tarun\\Documents\\airlines.txt","r")
file=f.read().split("\n")
for i in file:
	k+=1
	url="https://in.finance.yahoo.com/q?s="+i
	r=requests.get(url)
	soup=BeautifulSoup(r.content,"html.parser")
	price=soup.find_all("span",{"id":"yfs_l84_"+i.lower()})
	name=soup.find_all("div",{"class":"title"})
	print (name[0].text,end=":")
	print (price[0].text)
print ("Number of companies:%d"%(k))
