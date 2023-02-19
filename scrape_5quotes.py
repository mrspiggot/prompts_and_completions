import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

for i in range(5):
    quote = soup.find_all('span', class_='text')[i].get_text()
    author = soup.find_all('small', class_='author')[i].get_text()
    print(f'Quote {i+1}:')
    print(quote)
    print(author)
    print('-' * 40)
