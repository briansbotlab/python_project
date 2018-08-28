# 导入SQLite驱动:
import sqlite3

class Test:
    def __init__(self):
        # 连接到SQLite数据库
        # 如果文件不存在，会自动在当前目录创建:
        self.conn = sqlite3.connect('test.sqlite3')
        # 创建一个Cursor:
        self.cursor = self.conn.cursor() 
        
    def close_db(self):
        # 关闭Cursor:
        self.cursor.close()
        # 提交事务:  
        self.conn.commit()
        # 关闭Connection:
        self.conn.close()

    def create_table(self,table):
        # 創資料表:
        self.table = table
        self.cursor.execute('create table '+ table +' (id varchar(20) primary key, name varchar(20))')
    
    def insert(self,table,table_id,table_name):
        #插入資料
        self.tabel = table
        self.table_id = table_id
        self.table_name = table_name
        self.cursor.execute('insert into '+ table +' (id, name) values (\''+table_id+'\', \''+table_name+'\')')
        print('insert into '+ table +' (id, name) values (\''+table_id+'\', \''+table_name+'\')')
    def get_row_num(self,table):
        #查詢資料筆數
        self.tabel = table
        self.cursor.execute('SELECT * FROM \''+ table +'\'')
        result = self.cursor.fetchall()
        print(len(result))
        
    


if __name__ == '__main__':
    T=Test()
    '''
    T.create_table('Check_list')
    for i in range(10):
        T.insert('Check_list',str(i),str('user'+str(i)))
       
    T.close_db()
    '''
    T.get_row_num('Check_list')
    
  
    
    