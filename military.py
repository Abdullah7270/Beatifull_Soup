import requests
from bs4 import BeautifulSoup 
import arabic_reshaper 
from bidi.algorithm import get_display

for page in range(0,5):
    url = f'https://www.gami.gov.sa/ar/news?page={page}'

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find_all('a', class_='all-link')
    for t in title:
        reshaped_text = arabic_reshaper.reshape(t.text)
        bidi_text = get_display(reshaped_text)
        print(bidi_text)
    print('-----------------')  # Print a line after each PAGE
