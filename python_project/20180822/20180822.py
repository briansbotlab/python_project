# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 18:06:55 2018

@author: superuser
"""

import sqlite3  #引用sqlite3
conn = sqlite3.connect('example.sqlite3')
c = conn.cursor()
a=input('input:')
c.execute(a)
conn.commit()

