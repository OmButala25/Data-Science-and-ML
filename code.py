import pandas as pd
import requests
from bs4 import BeautifulSoup

# Read the input Excel file
input_file_path = 'input.xlsx'
df = pd.read_excel(input_file_path)

# Function to extract article text from a given URL
def extract_article_text(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract title and article text
        title = soup.title.text.strip()
        article_text = ' '.join([p.text.strip() for p in soup.find_all('p')])

        return title, article_text
    except Exception as e:
        print(f"Error extracting data from {url}: {str(e)}")
        return None, None

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    url_id = row['URL_ID']
    url = row['URL']

    # Extract article text
    title, article_text = extract_article_text(url)

    # Save the extracted data to a text file
    if title and article_text:
        output_file_path = f'{url_id}.txt'
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(f'Title: {title}\n\n')
            file.write(f'Article Text: {article_text}')

        print(f"Data extracted from {url} and saved to {output_file_path}")

print("Extraction complete.")
