# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 10:32:04 2018

@author: superuser
"""

class A(object):
    def method1(self):
        print('A.method1')
        
    def method2(self):
        print('A.method2')
        
class B(A):
    def method3(self):
        print('B.method3')
        
class C(A):
    def method2(self):
        print('C.method2')
        
    def method3(self):
        print('C.method3')
        
class D(B, C):
    def method4(self):
        print('D.method4')

d = D()
d.method4() # 在 D 找到，D.method4
d.method3() # 以 D->B 順序找到，B.method3
d.method2() # 以 D->B->C 順序找到，C.method2
d.method1() # 以 D->B->C->A 順序找到，A.method1