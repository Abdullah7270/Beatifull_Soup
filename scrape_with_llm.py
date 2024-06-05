from bs4 import BeautifulSoup
import requests

def beautifulsoup_web_scraper(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return str(soup)

url = 'https://www.voanews.com/'

data = beautifulsoup_web_scraper(url)
print(data)