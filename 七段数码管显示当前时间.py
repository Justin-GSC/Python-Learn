import time
import turtle

now = time.ctime()
Y = eval(now[-4:])
S = eval(now[-7:-5])
M = eval(now[-10:-8])
H = eval(now[-13:-11])

def seven(n):
    if n == 1:
        turtle.right(90)
        turtle.fd(8)
        penup()
        turtle.fd(1)
        pendown()
        
print("{}年{}时{}分{}秒".format(Y,H,M,S))
print(now)
