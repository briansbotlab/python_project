import sqlite3

class Sqlite_operate:
    def __init__(self):
        pass
        
    def connect(self,sqlite_file='sqlite_file.sqlite3'):    
        # Connecting to the database file
        self.conn = sqlite3.connect(sqlite_file)
        self.c = self.conn.cursor()
        
    def execute_sql(self,sql_lan):
        
        self.c.execute(sql_lan)
        
        self.commit();
        
    def commit(self):    
        # Committing changes and closing the connection to the database file
        self.conn.commit()
        self.conn.close()
  
    def select_result(self,sql_lan):
        self.c.execute(sql_lan)
        
        result=self.c.fetchall()
        
        for row in result:
            print(row)
      
import tkinter as tk       
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets() #建立所有物件
        
    def create_widgets(self):
        #label
        self.combo_label = tk.Label(self,text="Select SQL:",font=("Arial",12))
        #combobox
        self.current_table = tk.StringVar() # create variable for table
        self.select_sql_lan = ttk.Combobox(self, width=15,textvariable = self.current_table)
        self.select_sql_lan["values"]=("Seelct","Update","Insert Into","Create Table","DELETE FROM")
        self.select_sql_lan.current(0)  #选择第一个
        self.select_sql_lan.bind("<<ComboboxSelected>>",self.select_sql)  #绑定事件,(下拉列表框被选中时，绑定self.select_sql()函数
        # button
        self.submit_btn = tk.Button(self,text = "Submit",bg='#80ffff',fg ='black',font=("Arial",12),command=self.sql_use) 
        self.exit_btn = tk.Button(self,text = "Exit",bg='#80ffff',fg ='black',font=("Arial",12),command=root.destroy)
                                
        #text with slider
        self.talkSlider = tk.Scrollbar(self, orient="vertical")
        self.talkText = tk.Text(self,font=("Arial",12),height=20, width=30,fg = "#000000",state='normal',bg='#0590ff',cursor="plus")
       
        #set relationship
        self.talkSlider.config(command=self.talkText.yview)
        self.talkText.config(yscrollcommand=self.talkSlider.set)
        #set init text
        quote = ''
        self.talkText.insert(END, quote)
         #pack them
        '''
        self.exit_btn.pack(fill=X,side = "bottom",pady=0)
        
        self.submit_btn.pack(fill=X,side = "bottom",pady=0)
        self.select_sql_lan.pack(side = "bottom",anchor="ne")
        self.combo_label.pack(side = "bottom",anchor="w")
        

        
        
        self.talkText.pack(side='left', fill=Y)
        self.talkSlider.pack(side='left', fill=Y)
        '''
        self.talkText.grid(row=0,column=0,padx=15)
        self.talkSlider.grid(row=0,column=0,sticky='ens')
        
        self.exit_btn.grid(row=1,column=0,sticky='wsne')
        self.select_sql_lan.grid(row=2,column=0,sticky='e')
        self.combo_label.grid(row=2,column=0,sticky='w')
        self.submit_btn.grid(row=3,column=0,sticky='wsne')
        
        
        
    def sql_use(self):
        context=self.talkText.get("1.0",'end-1c')
        print(str(context))
        sql =Sqlite_operate()
        sql.connect()
        
        if(str(self.select_sql_lan.get()) == 'Seelct'):
            sql.select_result(str(context))

        else:
            sql.execute_sql(str(context))
            
    def select_sql(self, event):
        slt=self.select_sql_lan.get()
        
        if(str(slt) == 'Seelct'):
            self.talkText.delete(1.0, END)
            self.talkText.insert(END, 'SELECT "欄位名" FROM "表格名";')
            
        elif(str(slt) == 'Update'):
            self.talkText.delete(1.0, END)
            self.talkText.insert(END, 'UPDATE "表格名"SET "欄位1" = [新值]WHERE "條件";')
            
        elif(str(slt) == 'Insert Into'):
            self.talkText.delete(1.0, END)
            self.talkText.insert(END, 'INSERT INTO "表格名" ("欄位1", "欄位2", ...)VALUES ("值1", "值2", ...);')
            
        elif(str(slt) == 'Create Table'):
            self.talkText.delete(1.0, END)
            self.talkText.insert(END, 'CREATE TABLE "表格名"("欄位 1" "欄位 1 資料種類","欄位 2" "欄位 2 資料種類",... );')
            
        elif(str(slt) == 'DELETE FROM'):
            self.talkText.delete(1.0, END)
            self.talkText.insert(END, 'DELETE FROM "表格名"WHERE "條件";')
            
        else:
            messagebox.showerror("Error", "Error")
            
        print("select"+slt)
        
if __name__ == '__main__':
    root = tk.Tk()
    #root.iconbitmap("0a.ico")
    #root.overrideredirect(True)
    #root.style = ttk.Style()
    #('clam', 'alt', 'default', 'classic')
    #root.style.theme_use("clam")
    app = Application(master=root)
    app.master.title("My Application") #title
    app.master.minsize(305, 450) #最小邊界
    app.master.maxsize(305, 450) #最大邊界 
    app.master["bg"]="black"
    
    app.mainloop()