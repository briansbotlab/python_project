# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 09:48:13 2018

@author: admin
"""

import requests
from bs4 import BeautifulSoup
import json

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
#name = input('Input Product Name:')

url = 'http://poedb.tw/xyz.php?name='+'獸腹'+'&league=Warbands'

res = requests.get(url,headers)

html=res.content

soup = BeautifulSoup(html,'lxml')

#al = soup.find_all('span',class_='sortable', attrs={'data-name': 'price','data-value':'value'})
al = soup.find_all('span')

for item in al:
    print(item.text)
    print('________________________')





#data = json.loads(res.text)


#print(name)

'''
webdatas = data['prods']


print('查詢筆數:' + str(len(webdatas)))
print('______________________________')

for product in webdatas:
    print('產品名稱:' + product['name'])
    print('產品價格:' + str(product['price']))
    print('購買網址:' + 'https://24h.pchome.com.tw/prod/' + product['Id'])
    print('- - - - - - - - - - - - - - - - - - - - - - -')
    
    '''