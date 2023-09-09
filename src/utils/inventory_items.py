import json

import requests
from bs4 import BeautifulSoup

# 76561198127020542
url = "https://steamcommunity.com/profiles/76561198173702941/inventory/#730"
url2 = "https://steamcommunity.com/inventory/76561198173702941/730/2?l=russian&count=75"
# soup = BeautifulSoup(requests.get(url2).content, 'html.parser')

with open('data.json', encoding="utf-8", errors='ignore') as f:
    data = json.load(f)
    # for i in range(30):
    i = 0
    while True:
        print(data["descriptions"][i]["name"])
        i += 1
# descriptions
#  "tradable": 1,
#       "name": "Кейс «Разлом»",
#       "name_color": "D2D2D2",
#       "type": "Контейнер, базового класса",
#       "market_name": "Кейс «Разлом»",
#       "market_hash_name": "Fracture Case",
#       "commodity": 1,
#       "market_tradable_restriction": 7,
#       "marketable": 1,
#       "tags":
