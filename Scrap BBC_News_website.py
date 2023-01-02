import requests
import pandas as pd
from bs4 import BeautifulSoup


url = 'https://www.bbc.com/news'

#Great a header
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

# Request the web page
r = requests.get(url, headers=headers)
html = r.content

# Great soup objectt
soup = BeautifulSoup(html, 'html.parser')
#print(soup.prettify())

# Great scraper
def bbc_news_scraper(keyword):
	news_list = []
	# Find all the headers in BBC
	for h in soup.find_all('h3', class_='gs-c-promo-heading__title'):
		news_title = h.contents[0].lower()
		if news_title not in news_list:
			if 'bbc' not in news_title:
				news_list.append(news_title)
	no_of_news =0
	keyword_list = []
#  Goes through the list and search for the keyword
	for i, title in enumerate(news_list):
		text = ''
		if keyword.lower() in title:
			text = '<-------------------------KEYWORD'
			no_of_news += 1
			keyword_list.append(title)
		print(i + 1, ':', title, text)
	# Print the Title of the articles that contain the keyword
	print(f'\n----------------Total mentions of "{keyword}" = {no_of_news} ----------------')
	for i, title in enumerate(keyword_list):
		print(i + 1, ':', title)

bbc_news_scraper('putin')






























