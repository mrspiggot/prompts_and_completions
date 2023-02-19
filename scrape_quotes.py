import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

quote = soup.find('span', class_='text').get_text()
author = soup.find('small', class_='author').get_text()

print(quote)
print(author)
