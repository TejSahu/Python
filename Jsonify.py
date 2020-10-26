import requests
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                         'AppleWebKit/537.36 (KHTML, like Gecko)'
                         'Chrome/70.0.3538.77 Safari/537.36'}

yts = 'https://yts.mx/api/v2/list_movies.json'
data = requests.get(yts, headers=headers).json()
with open("C:\\Users\\Tej-Laptop\\PycharmProjects\\Writing\\YTS.json", 'w') as jsonout:
    json.dump(data, jsonout, indent=3)
