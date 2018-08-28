# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 12:27:29 2018

@author: superuser
"""

import csv

# 開啟 CSV 檔案
with open('test.csv', newline='') as csvfile:

  # 讀取 CSV 檔案內容
  rows = csv.reader(csvfile)

  # 以迴圈輸出每一列
  for row in rows:
    print(row)
    
    
'''
讀取特定行
'''   
import csv
f = open('test.csv', 'r')
for row in csv.DictReader(f):
    print (row['num'])
f.close()

