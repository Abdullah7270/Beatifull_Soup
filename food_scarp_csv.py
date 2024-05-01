from bs4 import BeautifulSoup 
import requests 
import json 
import time 
import csv 

def extract(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    
    recipes_box = soup.find('div', class_='col-md-8 no-right-padding')
    recipes = recipes_box.find_all('li')
    
    recipe_data = []

    for recipe in recipes:
        recipe_info = {}
        title_el = recipe.find('h4', class_='entry-title')

        if title_el is not None:
            recipe_info['Title'] = title_el.find('a').text.strip()
            recipe_info['Link'] = title_el.find('a').get('href')
            recipe_info['Description'] = recipe.find('p').text.strip()
            recipe_info['Image'] = recipe.find('img').get('data-src')

            recipe_data.append(recipe_info)
            with open('recipes.csv', 'w', newline='', encoding='utf-8') as csvfile:
                field_names = recipe_info.keys()
                writer = csv.DictWriter(csvfile, fieldnames=field_names)
                writer.writeheader()
                writer.writerows(recipe_data)
    
    return recipe_data
    

url = 'https://www.bbcgoodfoodme.com/collections/quick-and-healthy/'
recipes = extract(url)

            