import requests
import pandas as pd
from bs4 import BeautifulSoup

article_list = []
url = 'https://blog.mozilla.org/en/latest/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, features='lxml')

articles = soup.find_all('section', class_='mzp-c-card mzp-has-aspect-1-1')

for item in articles:
	title = item.find('h2', class_='mzp-c-card-title').text
	link = item.find('a', class_='mzp-c-card-block-link')

	article = {
		'Title': title,
		'Link': link['href']
	}
	article_list.append(article)

df = pd.DataFrame(article_list)
df.to_csv('articlelist.csv', index=False)
print(df)





















