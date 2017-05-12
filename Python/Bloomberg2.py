import requests
from bs4 import BeautifulSoup
import json
import time
import csv
with open("C:\\Users\\manmeet_tarun\\Documents\\companylist.csv", newline='') as f:
    reader = list(csv.reader(f))
    for i in range(1,len(reader)):
    	url="https://www.bloomberg.com/markets/watchlist/recent-ticker/"+reader[i][0]+":US"
    	r=requests.get(url)
    	js=r.json()
    	print (js["disp_name"],end=":")
    	print (js['last_price'])