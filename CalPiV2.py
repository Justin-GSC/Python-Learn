#CalPiV2.py
import time
import random
start = time.perf_counter()
DARTS = 10000*10000
hits = 0.0
for i in range(1,DARTS+1):
    x,y = random.random(),random.random()
    if 1>=pow(x**2+y**2,0.5):
        hits +=1
pi = 4*(hits/DARTS)
print("pi = :{0:}".format(pi))
print("used time :{}".format(time.perf_counter()-start))
    