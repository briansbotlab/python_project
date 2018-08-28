# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 14:02:15 2018

@author: admin
"""

import requests
from bs4 import BeautifulSoup
import json


url = 'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=%E5%B0%8F%E7%99%BD%E8%8F%9C&page=1&sort=rnk/dc'

res = requests.get(url)

data = json.loads(res.text)


webdatas = data['prods']


print('查詢筆數:' + str(len(webdatas)))
print('______________________________')

for product in webdatas:
    print('產品名稱:' + product['name'])
    print('產品價格:' + str(product['price']))
    print('購買網址:' + 'https://24h.pchome.com.tw/prod/' + product['Id'])
    print('- - - - - - - - - - - - - - - - - - - - - - -')