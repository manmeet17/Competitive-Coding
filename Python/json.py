import requests
import json
url="http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1"
r=requests.get(url)

