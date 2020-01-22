from typing import List, Any

import requests
from bs4 import BeautifulSoup
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/70.0.3538.77 Safari/537.36'}
url = 'https://www.amazon.in/dp/B081XP71GD?ref_=ams_ad_dp_asin_img'
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, features="lxml")
# print(soup)
Title = soup.find(id='productTitle').text.strip()
try:
    price = soup.find(id='priceblock_dealprice').text
except AttributeError:
    price = soup.find(id='priceblock_saleprice').text

# print(Title)
# print(price)

categories: List[Any] = []

for li in soup.select("#wayfinding-breadcrumbs_container ul.a-unordered-list")[0].findAll("li"):
    categories.append(li.get_text().strip())

del categories[1::2]

# print(categories)

features = []
for li in soup.select("#feature-bullets ul.a-unordered-list")[0].findAll('li'):
    features.append(li.get_text().strip())

jsonObject = {"Title": Title, 'categories': categories, 'features': features, 'price': price}

print(json.dumps(jsonObject, indent=2, ensure_ascii=False))
