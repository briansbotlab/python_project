import requests
import re
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

r = requests.get('https://shopee.tw/mall/search/?keyword=%E7%A8%AE%E5%AD%90', headers)


html=r.content
html_doc=str(html,'utf-8') #html_doc=html.decode("utf-8","ignore")



soup= BeautifulSoup(html_doc, 'lxml')

aaa = soup.find_all('div')



for a in aaa:
    name = a.text
    href = a.get('href')
    print(name)
    print(href)
    print('------')

'''

content = r.text

soup = BeautifulSoup(content, 'lxml')

aaa = soup.find_all('div')




for a in aaa:
    joke = a.text
    print(joke)
    print('------')

'''



'''

td = soup.find_all('a',class_="style2")


for m in td:
    info = m.text
    print(info)
    print('----------')
'''    


