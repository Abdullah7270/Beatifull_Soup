from bs4 import BeautifulSoup
import requests
import pandas as pd

titles_list = []
authors_list = []
summaries_list = []
links_list = []
images_list = []

for page in range(0, 4):
    url = f'https://time.com/tag/artificial-intelligence/?page={page}'

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all article containers
    articles = soup.find_all('div', class_='taxonomy-tout')

    for article in articles:
        # Scrape title
        title_tag = article.find('h2', class_='headline')
        title = title_tag.text.strip() if title_tag else ""
        titles_list.append(title)

        # Scrape author
        author_tag = article.find('span', class_='byline')
        author = author_tag.text.strip() if author_tag else ""
        authors_list.append(author)

        # Scrape summary
        summary_tag = article.find('h3', class_='summary')
        summary = summary_tag.text.strip() if summary_tag else ""
        summaries_list.append(summary)

        # Scrape link
        link_tag = article.find('a', href=True)
        link = 'https://time.com' + link_tag['href'] if link_tag else ""
        links_list.append(link)

        # Scrape image
        image_tag = article.find('img', src=True)
        image = image_tag['src'] if image_tag else ""
        images_list.append(image)

# Ensure all lists are the same length
max_length = max(len(titles_list), len(authors_list), len(summaries_list), len(links_list), len(images_list))
while len(titles_list) < max_length:
    titles_list.append("")
while len(authors_list) < max_length:
    authors_list.append("")
while len(summaries_list) < max_length:
    summaries_list.append("")
while len(links_list) < max_length:
    links_list.append("")
while len(images_list) < max_length:
    images_list.append("")

# Create a pandas DataFrame from the lists
df = pd.DataFrame({
    'Article Title': titles_list,
    'Author Name': authors_list,
    'Summary': summaries_list,
    'Article Link': links_list,
    'Image': images_list
})

# Save the DataFrame to a CSV file
df.to_csv('aimagazine.csv', index=False)

# Print the DataFrame to verify
print(df)
