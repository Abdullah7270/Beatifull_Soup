import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://www.countries-ofthe-world.com/flags-of-the-world.html'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


for country in soup.find_all('td'):
    print(country.text.strip())


for flag in soup.find_all('img'):
    print('https://www.countries-ofthe-world.com/' + flag.get('src'))

