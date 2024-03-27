import pandas as pd
from bs4 import BeautifulSoup
import requests

url = 'https://www.scrapethissite.com/pages/simple/'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')  # 'html.parser' can be used if 'lxml' is not installed

all_data = []

# Assuming each 'div' with class 'row' contains multiple 'div' with class 'country', 
# which seems to be the case based on your URL structure
countries = soup.find_all('div', {'class': 'country'})

for country in countries:
    # Extract the country name
    country_name = country.find('h3', {'class': 'country-name'}).get_text(strip=True)
    
    # Extract other information within each country's div
    # Example: extracting the capital
    capital = country.find('span', {'class': 'country-capital'}).get_text(strip=True)
    population = country.find('span', {'class': 'country-population'}).get_text(strip=True)
    area = country.find('span', {'class': 'country-area'}).get_text(strip=True)
    
    # Append the collected information as a dictionary to all_data list
    all_data.append({
        'Country': country_name,
        'Capital': capital,
        'Population': population,
        'Area': area
    })

# Create a DataFrame from the all_data list of dictionaries
df = pd.DataFrame(all_data)

# Output to check the DataFrame content
print(df)

# Save the DataFrame to an Excel file
df.to_excel('country.xlsx', index=False)
