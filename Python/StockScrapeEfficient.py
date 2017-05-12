import requests
from bs4 import BeautifulSoup
f=open("C:\\Users\\manmeet_tarun\\Documents\\file.txt","r")
file=f.read().split("\n")
for i in file:
	url="https://www.google.com/finance/getprices?q="+i+"&x=NASD&i=120&p=25m&f=c&df=cpct&auto=1&ts=1486478402858&ei=BtyZWIjuEtDLuATdir_wBA"
	r=requests.get(url)
	soup=BeautifulSoup(r.content,'html.parser')
	print (i,end=":")
	print (soup.text.split()[-1])