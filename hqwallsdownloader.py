from bs4 import BeautifulSoup
import requests

c = 'https://www.hdqwalls.com'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                         'Chrome/70.0.3538.77 Safari/537.36'}

# Enter the page URL, main page url like the one here where you can see the thumbnails
for page in range(20, 26):
    print("The value of page is " + str(page))
    url = 'https://hdqwalls.com/category/superheroes-wallpapers/page/' + str(page)
    print(url)
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, features="lxml")

    html = soup.findAll('div', {'class': 'column_padding'})

    list1 = []  # list1 contains all the html files from the mentioned url
    for num in range(0, len(html)):
        a = html[num].find('a')['href']
        list1.append(a)

    print(list1)
    with open('downloads_hdq.txt', 'w') as download_file:
        for tab in range(len(html)):
            print(c + list1[tab], file=download_file)

    print("Saved file, on to downloading now")

    download_urls = []
    with open('downloads_hdq.txt', 'r') as read_file:
        for i in read_file:
            download_urls.append(i)

    # print(len(download_urls))
    # Downloading part code

    for i in range(len(download_urls)):
        url2 = download_urls[i][25: len(download_urls[i]) - 1] + ".jpeg"
        # print(url2)

        d = ""
        response = requests.get(download_urls[i], headers=headers)
        soup = BeautifulSoup(response.content, features='lxml')
        for a in soup.find_all('div', {'class': 'wallpaper_container'}):
            for b in a.findAll('div', {'class': 'text-center'}):
                for e in b.findAll('a'):
                    d = e.get('href')
                    print('Downloading ' + d)

            request2 = requests.get(d)
            # Change the path "C:\\Users\\Tej-Laptop\\Desktop\\Game\\" to your desired location below
            with open("C:\\Users\\Tej-Local\\Downloads\\" + url2, 'wb') as image:
                image.write(request2.content)

    del a
    del tab
    del b
    del html
    del list1
    del d
    del soup
    del response
    del request2
print("Finished Downloading")
