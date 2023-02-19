import requests
from bs4 import BeautifulSoup
import textwrap

url = 'https://en.wikipedia.org/wiki/Beautiful_Soup_(HTML_parser)'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

first_paragraph = soup.find('div', class_='mw-parser-output').p.get_text()

wrapped_text = textwrap.fill(first_paragraph, width=80)

print(wrapped_text)

