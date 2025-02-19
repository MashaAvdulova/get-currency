import requests
import json
from bs4 import BeautifulSoup

def get_html(url: str):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0'}
    response = requests.get(url, headers=headers)
    return response.text

def get_currency(html: str):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', class_='js_sortable')

    pass

URL = 'https://www.alta.ru/currency/'
html = get_html(url=URL)
currency = get_currency(html)
# write_currency_json(currency)