import requests 
from bs4 import BeautifulSoup 
import pandas as pd
import warnings
from urllib3.exceptions import InsecureRequestWarning

# Suppress only the InsecureRequestWarning
warnings.simplefilter('ignore', InsecureRequestWarning)

cuurent_page = 1

data = []

################################# Looping through all the pages ###############

while True:
    print('Cuurently scraping page: '+str(cuurent_page))

################################# Fetching the page ############################
    url = 'https://scrapeme.live/shop/page/'+str(cuurent_page)+'/'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
    }

    response = requests.get(url, headers=headers, verify=False)
################################# Parsing the page #############################
    soup = BeautifulSoup(response.text,'html.parser')

    all_items = soup.find_all('li', class_='product')

    if "Page not found" in soup.title.string:
        break

############################### Looping through every element on the page ####### 
    for item in all_items:
        row = {}
################################# Fetchin data points of the elements ############
        row['Name'] = item.find('h2', class_='woocommerce-loop-product__title').text
        row['Price'] = item.find('span', class_='woocommerce-Price-amount amount').text.replace('£',"").replace('00',"")
        row['URL'] = item.find('a').get('href')

        data.append(row)
    cuurent_page +=1
################################# Writing to CSV #################################
df = pd.DataFrame(data)
df.to_csv('toys.csv', index=False)

