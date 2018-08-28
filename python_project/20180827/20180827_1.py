# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 15:52:01 2018

@author: superuser
"""
import tkinter as tk
win=tk.Tk() #建立視窗容器物件
win.title("Tk GUI")
label=tk.Label(win, text="Hello World!")   #建立標籤物件
label.pack()       #顯示元件
button=tk.Button(win, text="OK",command = win.destroy)
button.pack()     #顯示元件
win.mainloop()
