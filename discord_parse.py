import csv
import requests
from bs4 import BeautifulSoup

def get_html(url):
    responce = requests.get(url)
    return responce.text

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    table_rows = soup.find('tbody').find_all('td')

    for row in table_rows:
        row_data = row.find_all('td')
        currency = row_data[2].find('a').find('p').text
        price = row_data[3].find('a').text
        market_cap = row_data[6].find('p').text

        data = {
            'name' = currency,
            'price' = price,
            'market cap' = market_cap,
        }
        write_scv(data)









if __name__ == 'main':
    get_data(get_html('https://coinmarketcap.com/ru/'))


