from bs4 import BeautifulSoup
import requests
import pandas as pd

# Lists to hold the data
titles = []
prices = []
stars = []
urlss = []

pages_to_scrape = 10

# Get the raw data
for i in range(1, pages_to_scrape + 1):
    url = f'https://books.toscrape.com/catalogue/page-{i}.html'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    # Extract data for each book
    for book in soup.find_all('article', class_='product_pod'):
        # Title
        title = book.find('h3').find('a')['title']
        titles.append(title)
        
        # Price
        price = book.find('p', class_='price_color').text
        prices.append(price)
        
        # Star rating
        star = book.find('p', class_='star-rating')['class'][1]
        stars.append(star)
        
        # Image URL
        image_url = book.find('div', class_='image_container').find('img')['src']
        full_image_url = 'https://books.toscrape.com/' + image_url.replace('../', '')
        urlss.append(full_image_url)

# Build a dictionary
data = {'Title': titles, 'Price': prices, 'Stars': stars, 'Links': urlss}

# Create DataFrame
df = pd.DataFrame(data)
df.index += 1

# Save to Excel
df.to_excel('book.xlsx', index=False)

print('Books Data Saved Successfully!')
