# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 12:31:41 2018

@author: superuser
"""


from datetime import datetime

import matplotlib.dates as mdates
import matplotlib.pyplot as plt

import csv
dates=[]
times=[]
f = open('test_1.csv', 'r')
for row in csv.DictReader(f):
    dates.append(row['日期'])
    #print (row['日期'])
    times.append(row['時間'])
    #print (row['時間'])
f.close()




ys = ['2','23']
xs = [datetime.strptime(d,'%Y/%m/%d').date() for d in dates]
ys = [datetime.strptime(t,'%H:%M:%S').time() for t in times]
# 配置横坐标

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())

# 配置縱坐标

#plt.gca().yaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
#plt.gca().yaxis.set_major_locator(mdates.HourLocator())


# scatter
#plt.scatter(xs,ys)
# plot
plt.plot(xs, ys,'g')

plt.gcf().autofmt_xdate()  # 自动旋转日期标记
plt.axis(['2018-05-24','2018-06-16', '08:00:00', '23:00:00'])
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5) #輸出大小
plt.show()
fig.savefig('test.png', dpi=500)#存檔
