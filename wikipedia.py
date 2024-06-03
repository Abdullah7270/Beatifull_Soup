from bs4 import BeautifulSoup 
import requests 
import re 

url = 'https://en.wikipedia.org/wiki/Artificial_intelligence'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

# Extract all the links from the webpage
links = []
text = []

for link in soup.find_all('a', attrs={'href':re.compile('^/wiki/')}):
    text.append(link.text)
    links.append(link.get('href'))

# print(len(links))
# print(len(text))

# Print the Links
for i in range(len(links)):
    print(text[i]+ '--->' +'https://en.wikipedia.org/'+links[i])