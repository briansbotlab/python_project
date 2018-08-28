# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 09:48:13 2018

@author: admin
"""

import requests
from bs4 import BeautifulSoup
import json

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}


url = 'http://poedb.tw/xyz.php?name='+'獸腹'+'&league=Warbands'

res = requests.get(url,headers)

html=res.content

soup = BeautifulSoup(html,'lxml')

al = soup.find_all('span')

for item in al:
    print(item.text)
    print('________________________')






