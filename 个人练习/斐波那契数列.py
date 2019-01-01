# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 09:52:11 2018

@author: shichao
"""

import turtle as t
def feibo(n):
    num = 0
    if n == 0 or n == 1:
        num = 1
    else :
        num = feibo(n-1) + feibo(n-2)
    return num

def f(n):
    for i in range(n):
        print(feibo(i),end=",")
        
n = eval(input("请输入阶数："))
f(n)
t.setup(800,800)
t.pensize(2)
for i in range(n):
    t.circle(-feibo(i),90)
    t.hideturtle()