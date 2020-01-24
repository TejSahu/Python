from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/70.0.3538.77 Safari/537.36'}
url = 'https://www.hdwallpapers.in/cars-desktop-wallpapers.html'
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, features="lxml")

html = soup.findAll('div', {'class': 'thumb'})
list1 = []  # list1 contains all the html files from the mentioned url
for num in range(0, 18):
    a = html[num].find('a')['href']
    list1.append(a)
