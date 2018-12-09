#TextProBarV2.py
import time
scale = 10
A = "执行开始"
B = "执行结束"
print("{:-^20}".format(A))
for i in range(scale+1):
    a = "*"*i
    b = "."*(scale-i)
    c = (i/scale)*100
    print("\r{:^3.0f}%[{}->{}]".format(c,a,b),end="")
    time.sleep(0.5)
print("{:-^20}".format(B))
