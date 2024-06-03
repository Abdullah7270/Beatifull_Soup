from bs4 import BeautifulSoup
import requests 

url = 'https://openlibrary.org/'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

# book_titles = soup.find_all('img', alt=True)
# for index, book in enumerate (book_titles,start=1):
#     print(f"{index}: {book['alt']}")

# book_images = soup.find_all('img', class_='bookcover')
# for index, image in enumerate (book_images,start=1):
#     print(f"{index}: {image['src']}")

book_images = soup.find_all('img', class_='bookcover')
for index, image in enumerate(book_images, start=1):
    src = image['src']
    if not src.startswith('data:image'):
        print(f"{index}: {src}")