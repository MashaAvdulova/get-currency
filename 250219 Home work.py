import requests
import json
from bs4 import BeautifulSoup

# 1. Получить курсы валют с сайта (сайт в видео)
# 2. Формат результата:
# {
# 	'USD':{
# 		'currency_number': 840,
# 		'name': 'Американский доллар',
# 		'price': 90.04
# 	},
# 	'EUR':{
# 		'currency_number': 111,
# 		'name': 'Евро',
# 		'price': 100.04
# 	},
# }
# def get_html(url: str):
#     headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0'}
#     response = requests.get(url, headers=headers)
#     return response.text
# # 3. Сохранить в currencies.json
#
# def get_currency(html: str):
#     soup = BeautifulSoup(html, 'html.parser')
#     table = soup.find('table', class_='js_sortable')
#
#
# URL = 'https://www.alta.ru/currency/'
# html = get_html(url=URL)
# currency = get_currency(html)