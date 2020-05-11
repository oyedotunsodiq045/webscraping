import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('http://127.0.0.1:5501/index.html')

soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find_all(class_='content')

for post in posts:
    print(post)