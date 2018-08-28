from tkinter import *
import tkinter as tk
from tkinter import ttk



class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        
        self.pack()
        self.create_widgets() #建立所有物件
        
        self.bot = ZeroA_BOT() #創造機器人   
        
    def create_widgets(self):
        '''
        \\\\\\\\\
        
        menubar
        
        \\\\\\\\\
        '''
        ##创建一个菜单栏，这里我们可以把他理解成一个容器，在窗口的上方
        self.menubar = tk.Menu(self)
        ##定义一个空菜单单元
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        ##将上面定义的空菜单命名为`File`，放在菜单栏中，就是装入那个容器中
        self.menubar.add_cascade(label='File', menu=self.filemenu)
        ##在`File`中加入`New`的小菜单，即我们平时看到的下拉菜单，每一个小菜单对应命令操作。
        ##如果点击这些单元, 就会触发`do_job`的功能
        self.filemenu.add_command(label='New', command=self.do_job)
        self.filemenu.add_command(label='Open', command=self.do_job)##同样的在`File`中加入`Open`小菜单
        self.filemenu.add_command(label='Save', command=self.do_job)##同样的在`File`中加入`Save`小菜单

        self.filemenu.add_separator()##这里就是一条分割线
        ##同样的在`File`中加入`Exit`小菜单,此处对应命令为`root.quit`
        self.filemenu.add_command(label='Exit', command=root.destroy)
        
        self.submenu = tk.Menu(self.filemenu)##和上面定义菜单一样，不过此处实在`File`上创建一个空的菜单
        self.filemenu.add_cascade(label='Import', menu=self.submenu, underline=0)##给放入的菜单`submenu`命名为`Import`
        self.submenu.add_command(label="Submenu1", command=self.do_job)##这里和上面也一样，在`Import`中加入一个小菜单命令`Submenu1
        
        root.config(menu=self.menubar) #很重要  顯示menubar
        
        '''
        \\\\\\\\\
        
        toolbar
        
        \\\\\\\\\
        '''
        
        #toolbar
        self.my_toolbar = Toolbar(self)
        
        self.my_toolbar.pack(side=TOP)
        
        '''
        \\\\\\\\\
        
        Button
        
        \\\\\\\\\
        '''
        
        # hi_there 為Button 
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top",expand =1)
        
        #quit 為 Button
        self.quit = tk.Button(self, text="QUIT", fg="red",command=root.destroy)
        self.quit.pack(side="bottom")
        
        self.entrythingy = Entry()  #設定為輸入
        self.entrythingy.pack(side="bottom")

        #here is the application variable
        self.contents = StringVar()
        # set it to some value
        self.contents.set("this is a variable")
        # tell the entry widget to watch this variable
        self.entrythingy["textvariable"] = self.contents

        # and here we get a callback when the user hits return.
        # we will have the program print out the value of the
        # application variable when the user hits return
        self.entrythingy.bind('<Key-Return>',self.print_contents)
        
        
        '''
        \\\\\\\\\
        
        text & slider
        
        \\\\\\\\\
        '''
        
        #text with slider
        self.talkSlider = Scrollbar(self)
        self.talkText = tk.Text(self,font=("Times New Roman",12),height=20, width=30,fg = "green",state='normal')
        #pack them
        self.talkSlider.pack(side=RIGHT, fill=Y)
        self.talkText.pack(side=LEFT, fill=Y)
        #set relationship
        self.talkSlider.config(command=self.talkText.yview)
        self.talkText.config(yscrollcommand=self.talkSlider.set)
        #set init text
        quote = "Hello World,\nWelcome to use My Application."
        self.talkText.insert(END, quote)
        
        self.talkText.config(state='disabled') # 設為無法更改內容
       
    def do_job(self):
        print("do job")
        
    def say_hi(self):
        print("hi there, everyone!")
        # 改變 hi_there 文字 、 外觀( 紅字 深紅底色 )
        self.hi_there.config(text = "你被桶了\n(沒有人逃得過0a這一桶)",fg="red", bg="dark red") 
        # 改變 talkText  外觀( 水藍 黑色 )
        self.talkText.config(font=("Times New Roman", 11, "bold"),fg="aqua", bg="black")
        
        
    def print_contents(self, event):
        self.talkText.config(state='normal') #啟用編輯
        
        print("hi. contents of entry is now ---->",self.contents.get())
        
        self.talkText.insert(END, '\nUser:'+self.contents.get())
        
        Bot_response = self.bot.getResponse(str(self.contents.get())) #機器人收信息
        
        self.talkText.insert(END, '\n0A:'+ str(Bot_response)) #機器人回信息
        
        print(str(Bot_response))
        
        self.contents.set("") #set contents as empty
        
        self.talkText.see("end") #看最後一行
        
        self.talkText.config(state='disabled') # 設為無法更改內容

class Toolbar(ttk.Frame):
    """ Toolbar """
    def button_one(self):
        print("button 1 pressed")

    def button_two(self):
        print("button 2 pressed")
        #self.master.button_function()

    def __init__(self,master):
        super().__init__(master)
        self.master = master
        self.pack(side=tk.TOP, fill=tk.X)
        self.button1 = ttk.Button(self,text="One",command=self.button_one)
        self.button2 = ttk.Button(self,text="Two",command=self.button_two)
        self.button1.grid(row=0,column=0)
        self.button2.grid(row=0,column=1)







        
import sys
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer      
        
class ZeroA_BOT:
    # 建立一個 ChatBot
    chatbot = ChatBot(
        # 這個 ChatBot 的名字叫做 ZeroA
        "ZeroA",
        storage_adapter = "chatterbot.storage.SQLStorageAdapter",
        # 設定訓練的資料庫輸出於根目錄，並命名為 ZeroA_db.json
        database = "./ZeroA_db.sqlite3"    
    )

    def __init__(self):
        '''
        self.chatbot.set_trainer(ChatterBotCorpusTrainer)
        
        self.chatbot.train("chatterbot.corpus.english")
        '''
        pass
    def getResponse(self, message=""):
        return self.chatbot.get_response(message)    


        
        
if __name__ == '__main__':
    root = tk.Tk()
    #root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='./0a.gif'))
    root.iconbitmap("0a.ico")
    app = Application(master=root)
    app.master.title("My Application") #title
    app.master.minsize(240, 480) #最小邊界
    #app.master.maxsize(240,480) #最大邊界 
    app.mainloop()