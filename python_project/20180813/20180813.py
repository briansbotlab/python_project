from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import PhotoImage
from tkinter import Canvas

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        
        self.pack()
        self.create_widgets() #建立所有物件
        
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
        self.filemenu.add_command(label='Open', command=self.open_file)##同样的在`File`中加入`Open`小菜单
        self.filemenu.add_command(label='Save', command=self.save_file)##同样的在`File`中加入`Save`小菜单

        self.filemenu.add_separator()##这里就是一条分割线
        ##同样的在`File`中加入`Exit`小菜单,此处对应命令为`root.quit`
        self.filemenu.add_command(label='Exit', command=root.destroy)
        
        self.submenu = tk.Menu(self.filemenu)##和上面定义菜单一样，不过此处实在`File`上创建一个空的菜单
        self.filemenu.add_cascade(label='Import', menu=self.submenu, underline=0)##给放入的菜单`submenu`命名为`Import`
        self.submenu.add_command(label="Submenu1", command=self.do_job)##这里和上面也一样，在`Import`中加入一个小菜单命令`Submenu1
        
        root.config(menu=self.menubar) #很重要  顯示menubar
        
        '''
        \\\\\\\\\
        
        canvas
        
        \\\\\\\\\
        '''
        # create the canvas, size in pixels
        self.show_img = Canvas(width=300,height=300,bg='red')

        # pack the canvas into a frame/form
        self.show_img.pack(fill='both',expand=0)
        self.img = PhotoImage(file='C:/Users/admin/Desktop/test.gif')
        self.show_img.create_image(0,0, anchor='nw', image=self.img)
        
        self.show_img.update()
        
    def open_file(self):
            
        self.filename =  filedialog.askopenfilename(initialdir = "/",
                            title = "Select file",
                            filetypes = (("GIF files","*.gif"),("jpeg files","*.jpg"),("all files","*.*")))
       
        print(self.filename)
        
        # load the gif image file
        self.gif1 = PhotoImage(file=str(self.filename))

        # put image on canvas
        # pic's upper left corner (NW) on the canvas is at x=50 y=10
        self.show_img.create_image(20, 20,image=self.gif1, anchor="nw")
        
        self.show_img.update()
            
    def save_file(self):
            
        self.filename =  filedialog.asksaveasfilename(initialdir = "/",
                            itle = "Select file",
                            filetypes = (("GIF files","*.gif"),("jpeg files","*.jpg"),("all files","*.*")))
         
        
        print(self.filename)  
            
            
    def do_job(self):
           
        print("do")
             
             
if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.master.title("My Application") #title
    #app.master.minsize(240, 480) #最小邊界
    app.mainloop()             
             
             
             
        