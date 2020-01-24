# Getting the list from page part
from bs4 import BeautifulSoup
import requests

c = "https://www.hdwallpapers.in/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/70.0.3538.77 Safari/537.36'}
#Enter the page URL, main page url like the one here where you can see the thumbnails
url = 'https://www.hdwallpapers.in/creative__graphics-desktop-wallpapers/page/2'
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, features="lxml")
prefix = 'https://www.hdwallpapers.in'
html = soup.findAll('div', {'class': 'thumb'})
list1 = []  # list1 contains all the html files from the mentioned url
for num in range(0, 18):
    a = html[num].find('a')['href']
    list1.append(a)

with open('downloads.txt', 'w') as download_file:
    for tab in range(18):
        print((prefix + list1[tab]), file=download_file)

# Downloading part
download_urls = []
with open('downloads.txt', 'r') as read_file:
    for i in read_file:
        download_urls.append(i)

#  getting them into a list and getting a second variable for proper file name
for i in range(18):
    # print(download_urls[i])
    url2 = download_urls[i][28:len(download_urls[i]) - 16] + ".jpeg"
    print(url2)
    d = ""
    response = requests.get(download_urls[i], headers=headers)
    soup = BeautifulSoup(response.content, features='lxml')
    for a in soup.findAll('div', {'class': 'wallpaper-resolutions'}):
        for b in a.findAll('a', title='HD 1920 x 1080 Wallpaper'):
            d = c + b.get('href')
            print(d)
            # print(b.get('href'))
            # print(c + b.get('href'))
    request2 = requests.get(d)

#Change the path "C:\\Users\\Tej-Laptop\\Desktop\\Game\\" to your desired location below
    with open("C:\\Users\\Tej-Laptop\\Desktop\\Game\\" + url2, 'wb') as image:
        image.write(request2.content)

print("Finished Downloading")
