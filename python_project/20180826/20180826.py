# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 09:58:56 2018

@author: superuser
"""

import tkinter as tk #引用


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets() #呼叫 create_widgets 方法

    def create_widgets(self):
        
         #創造 button 物件
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"  #設定button的文字
        self.hi_there["command"] = self.say_hi  #設定觸發button時執行的方法
        self.hi_there.pack(side="top")  #pack 顯示在application中 相對位置為 上


         #創造 button 物件
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        #root.destory 為銷毀root物件 即關閉application
        
        self.quit.pack(side="bottom")  #pack 顯示在application中 相對位置為 下

    def say_hi(self):
        print("hi there, everyone!")
        
if __name__ == '__main__':
    root = tk.Tk() 
    app = Application(master=root)
    app.mainloop()