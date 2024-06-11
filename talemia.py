import requests
from bs4 import BeautifulSoup
import arabic_reshaper
from bidi.algorithm import get_display

def clean_text(text):
    # Remove or replace unwanted characters
    # Example: Replace FSI and other control characters if they are known
    return text.replace('\u2068', '').replace('\u2069', '')  # FSI and PDI

page_number = 1

for page in range(0, 20):
    url = f'https://www.talemia.sa/ar/news/listall/{page}'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    titles = soup.find_all('h4', class_='media-heading news-titleall')

    for title in titles:
        try:
            cleaned_text = clean_text(title.text.strip())
            reshaped_text = arabic_reshaper.reshape(cleaned_text)
            bidi_text = get_display(reshaped_text)
            print(bidi_text)
        except Exception as e:
            print(f"Error processing text: {title.text.strip()} with error {e}")

    print(f'Page {page_number} scrapped')
    page_number += 1
