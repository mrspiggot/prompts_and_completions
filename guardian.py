import requests
from bs4 import BeautifulSoup
import pandas as pd
from decouple import config

api_key = config('GUARDIAN_API')
url = f"https://content.guardianapis.com/search?q=business&api-key={api_key}&show-fields=bodyText"

# Get the response from the API
response = requests.get(url)

# Parse the response as JSON
data = response.json()

# Extract the results from the response
results = data["response"]["results"]

# Define an empty list to store the data
data_list = []

# Loop through the results
for result in results:
    # Get the headline and URL of the article
    prompt = result["webTitle"]
    article_url = result["webUrl"]

    # Get the content of the article
    article_response = requests.get(article_url)
    article_html = article_response.text
    soup = BeautifulSoup(article_html, 'html.parser')
    article_body = ""
    for p in soup.select('div > p'):
        article_body += p.text

    # Append the data to the list
    data_list.append([prompt, article_body])

# Create a pandas dataframe from the data
df = pd.DataFrame(data_list, columns=["Prompt", "Completion"])

# Save the dataframe to Excel
df.to_excel("guardian_business_articles.xlsx", index=False)
