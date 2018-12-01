import requests
from bs4 import BeautifulSoup

def fujifilm_spider(max_pages):
    page = 1
    while page < max_pages:
        url = "https://www.ebay.com/b/" \
              "Fujifilm-Digital-Cameras/31388/bn_745?_pgn=" + str(page)
        source_code = requests.get(url)
