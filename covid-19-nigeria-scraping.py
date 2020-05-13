import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://covid19.ncdc.gov.ng/')

soup = BeautifulSoup(response.text, 'html.parser')

cases = soup.find_all(class_='content')

for case in cases:
    print(case)