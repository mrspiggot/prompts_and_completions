import requests
from decouple import config
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://newsapi.org/v2/top-headlines'
params = {'country': 'us', 'category': 'technology', 'pageSize': 50, 'apiKey': config('NEWS_API')}

response = requests.get(url, params=params)

data = response.json()

prompts = []
completions = []

for article in data['articles']:
    prompt = article['title']
    prompts.append(prompt)
    article_url=article['url']
    article_response = requests.get(article_url)
    article_html = article_response.text
    soup = BeautifulSoup(article_html, 'html.parser')
    article_body = ""
    for p in soup.select('div > p'):
        article_body += p.text

    completions.append(article_body)

df = pd.DataFrame({'Prompt': prompts,'completion': completions})

df = df.dropna()

df.to_excel('news_api_us_tech_articles.xlsx', index=False)
