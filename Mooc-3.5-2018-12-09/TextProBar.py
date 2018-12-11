#TexeProBar.py
import time
start_1 = time.perf_counter()
scale = 50
print("执行开始".center(scale//2,"-"))
start = time.perf_counter()
for i in range(scale + 1):
    a = "*" * i
    b = "." * (scale-i)
    c = (i/scale)*100
    dur = time.perf_counter()-start
    time.sleep(0.1)
    print("\r{:.0f} [{}->{} {:.2f}s]".format(c,a,b,dur),end="")
    
start_2 = time.perf_counter()
time_s = start_2 - start_1
print("\n总用时：{:.10f}s".format(time_s),end="")
print("\n"+"执行结束".center(scale//2,"-"))
