import os
import sqlite3
import cv2
import numpy as np


import matplotlib.pyplot as plt
import matplotlib.image as mpimg

'''
def get_conn(path):
    #连接到数据库，如果文件路径存在则连接，如果不存在，则报错
    if os.path.exists(path) and os.path.isfile(path):
        conn = sqlite3.connect(path)
        print('成功连接到[{}]的数据库'.format(path))
        return conn
    else:
        print('打开错误，请检查路径')
'''

def insert_image_db(MapId,image):
    conn = sqlite3.connect('test1.sqlite3', timeout=10)
    cursor = conn.cursor() 
    img_blob = sqlite3.Binary(image)
    #cursor.execute("create table MAP (MapId TEXT, Image BLOB)")
    """ 目的是把image转化成blob格式，然后保存到sql中"""
    try:
        #cursor.execute('INSERT INTO MAP (MapId,Image) VALUES( \''+ str(MapId) +'\', \'' + str(img_blob) + '\')')
        cursor.execute("INSERT INTO MAP (MapId,Image) VALUES(?,?)",(MapId,img_blob))
        conn.commit()
        cursor.close()
    except IOError:
        print ("写入数据库失败")
        conn.close()

def retrieve_image_db(MapId):
    conn = sqlite3.connect('test1.sqlite3', timeout=10)
    cursor = conn.cursor() 
    """ 读取存在数据库中的blob格式图片"""
    try:
        sqli = "SELECT Image FROM MAP WHERE MapId = :mapid"
        param = {'mapid':MapId} 
        cursor.execute(sqli,param)
        image = cursor.fetchone()
        image = np.array(image[0])
        image.decode('base64')
        conn.close()
        return image
    except IOError:
        print ("读取数据库失败")
        conn.close()

"""测试"""

image_path = "0ajpg.jpg"
MapId = "201605055"
image = cv2.imread(image_path)
insert_image_db(MapId,image_path)
#img = retrieve_image_db(MapId)
"""读取到的是没有变形过的数据"""
#img = img.reshape(image.shape)
#img=mpimg.imread('0ajpg.jpg')
#imgplot = plt.imshow(img)
#plt.show()