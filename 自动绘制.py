# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import turtle as t

def main(): # 定义基础绘制参数
    t.title("自动轨迹绘制")
    t.setup(800,600,0,0)
    t.pencolor("red")
    t.pensize(5)
    
datals = []
main()
f = open("b.txt","rt")
for line in f:
    line = line.replace("\n","")
    datals.append(list(map(eval,line.split(","))))
f.close()
for i in range(len(datals)):
    t.pencolor(datals[i][3],datals[i][4],datals[i][5])
    t.fd(datals[i][0])
    t.right(datals[i][2]) if datals[i][1] == 0 else\
    t.left(datals[i][2])
    t.write("好")
t.done()