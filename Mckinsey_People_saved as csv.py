from bs4 import BeautifulSoup
import pandas as pd
import requests
from csv import writer

url = 'https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-people'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

with open('makanzy_people1.csv', 'w', newline='', encoding='utf-8') as file:
	the_writer = writer(file)
	header = ['Name', 'Title', 'Profile', 'Photo_Link']
	the_writer.writerow(header)


	for box in soup.find_all('div', class_='profile-card-inner has-image'):
	# print(box.prettify())

		name = box.find('h6', class_='headline profile-card--title').text
		title = box.find('h6', class_='eyebrow profile-card--value').text.strip().replace(' ', '')
		profile = box.find('div', class_='profile-card--value profile-card--job-description').text.strip()
		photo = f'https://www.mckinsey.com' + box.find('img', class_='profile-card__profile-pic')['data-src']
		print(name, title, profile, photo)

		print()
		data = [name, title, profile, photo]
		the_writer.writerow(data)












# title = soup.find('h6', class_='eyebrow profile-card--value').text.strip().replace(' ', '')
# profile = soup.find('div', class_='profile-card--value profile-card--job-description').text.strip()
#
# print(name, title,profile)