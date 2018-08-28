# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 11:08:42 2018

@author: admin
"""

from tkinter import *

canvas_width = 900
canvas_height =500

master = Tk()

show = Canvas(master, 
           width=canvas_width, 
           height=canvas_height
           ,bg='red')
show.pack()

img = PhotoImage(file="C:/Users/admin/Desktop/test.gif")
show.create_image(0,0, anchor=NW, image=img)

mainloop()