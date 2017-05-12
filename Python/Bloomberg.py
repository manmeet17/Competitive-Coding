import requests
from bs4 import BeautifulSoup
import json
url="https://www.bloomberg.com/markets/watchlist/recent-ticker/AAPL:US"
r=requests.get(url)
soup=BeautifulSoup(r.content,'html.parser')
js=json.loads(soup.text)
print (js["last_price"])