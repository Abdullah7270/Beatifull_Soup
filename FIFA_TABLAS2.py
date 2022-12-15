import requests
from bs4 import BeautifulSoup
import pandas as pd

# years = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974,
# 		 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014,
# 		 2018]

def get_matches(year):
	url = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')

	matches = soup.find_all('div', class_='footballbox')

	home = []
	score = []
	away = []

	for match in matches:
		home.append(match.find('th', class_='fhome').get_text())
		score.append(match.find('th', class_='fscore').get_text())
		away.append(match.find('th', class_='faway').get_text())

	dict_footable = {'Home': home, 'Score': score, 'Away': away}
	df_footable = pd.DataFrame(dict_footable)
	df_footable['year'] = year
	return (df_footable)

print(get_matches('1990'))