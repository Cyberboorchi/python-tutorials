#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = 'https://mse.mn/mn/company/547'
data = requests.get(url)

my_data = []

html = BeautifulSoup(data.text, 'html.parser')
articles = html.select('div.bigprice')

for article in articles:

    title = article.select('.bigprice_up bp_div')[0].get_text()

    my_data.append({"title": title})

pprint(my_data)