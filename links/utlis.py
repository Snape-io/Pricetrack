from django.db.models.fields import URLField
import requests
import lxml
from bs4 import BeautifulSoup

def link_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    }

    r = requests.get(url, headers=headers)

    beau = BeautifulSoup(r.text, "lxml")

    productname = beau.select_one(selector="#productTitle").getText()
    productname = productname.strip()

    price = beau.select_one(selector="#priceblock_ourprice").getText()
    price = price.replace(',','')
    price = float(price[2:])

    return productname, price
