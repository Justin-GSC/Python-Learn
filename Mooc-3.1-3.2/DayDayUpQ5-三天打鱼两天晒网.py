#DayDayUpQ5.py 三天打鱼两天晒网
dayfactor=0.01
dayup=1
for i in range(365):
    if i%5 in [1,2,3]:
        dayup=(1+dayfactor)*dayup
    else:
        dayup=(1-dayfactor)*dayup
print("工作日的力量：{:.2f}".format(dayup))
    
 
