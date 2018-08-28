# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 10:09:15 2018

@author: superuser
"""

class Human:
    
    def __init__(self, do ,name='G'):
        self.do=do
        self.name=name
    
    def can1(self):
        print(self.name+' Can '+self.do)
        
class Man(Human):
    
    def __init__(self, do, name):
        super(Man,self).__init__(do, name)  # 呼叫父類別__init__()
        
    def can2(self):
        print('The man who is ' + self.name + ' Can ' + self.do )
        
        
        
if __name__ == '__main__':
    hg = Human('work')
    hg.can1()
   
    ha = Human('run','A')
    ha.can1()
    
    ms = Man('sleep','S')
    ms.can1()
    
    md = Man('donothing','D')
    md.can2()
    
    
    