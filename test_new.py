# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 14:53:46 2021

@author: ASUS
"""

class A():
    def __new__(cls, *arg, **kwarg):
        print("A new")
        return super(A, cls).__new__(cls) 
    def __init__(self, *arg, **kwarg):
        print("A init")
        pass
    pass
class B(A):
    def __new__(cls, *arg, **kwarg):
        print("b new")
        return super(B, cls).__new__(cls) 
    def __init__(self, *arg, **kwarg):
        super(B, self).__init__()
        print("B init")
        pass
    pass
class C(B, A):
    def __new__(cls, *arg, **kwarg):
        print("C new")
        return super(C, cls).__new__(cls) 
    def __init__(self, *arg, **kwarg):
        super(B, self).__init__()
        print("C init")
        pass
    pass
k = C(1)