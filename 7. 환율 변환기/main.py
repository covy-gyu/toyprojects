import requests
from bs4 import BeautifulSoup as bs


def get_exchange_rate(target1, target2):
    headers = {"User-Agent": "Mozilla/5.0", "Content_Type": "text/html; charset=utf-8"}

    response = requests.get(
        "https://kr.investing.com/currencies/{}-{}".format(target1, target2),
        headers=headers,
    )
    content = bs(response.content, "html.parser")
    containers = content.find("span", {"data-test": "instrument-price-last"})
    print(containers.text)


get_exchange_rate("usd", "krw")
