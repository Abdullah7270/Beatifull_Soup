from urllib. request import Request, urlopen
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://researchersgallery.com/album.php'

response = Request(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'})

webpage = urlopen(response).read()

# Saving the webpage to a file
with open('file.txt','wb') as file:
    file.write(webpage)

# Now, read from the saved file and parse it with BeautifulSoup
with open('file.txt', 'rb') as file:
    soup = BeautifulSoup(file, 'html.parser')

titles = soup.find_all('h3')
dates = soup.find_all('p')

# Extracting text from the titles and dates
titles = [title.text.strip() for title in titles]
dates = [date.text.strip() for date in dates]

# Check if titles and dates lists are of the same length
if len(titles) == len(dates):
    # Creating a DataFrame
    data = {'Title': titles, 'Date': dates}
    df = pd.DataFrame(data)

    # Save the DataFrame to a CSV file
    df.to_csv('data.csv', index=False)
    print("Data has been saved to 'data.csv'.")
else:
    print("The lengths of titles and dates do not match.")   
