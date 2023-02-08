from bs4 import BeautifulSoup
import requests
from csv import writer
import pandas as pd

job_list = []

url = 'https://100jobsofthefuture.com/browse/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

for box in soup.find_all('li', 'job-card'):
    
    job = box.find('span').text
    descrip = box.find('p').text
    
    data = {'Job Name': job, 'Job Description': descrip}
    job_list.append(data)

df = pd.DataFrame(job_list)
df.to_csv('Future_Jobs2.csv', index=False)
print(df)