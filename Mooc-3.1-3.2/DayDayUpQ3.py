#DayDayUpQ3.py
dayfactor=0.01
dayup=1
for i in range(365):
    if i%7 in [1,2,3,4,5]:
        dayup=(1+dayfactor)*dayup
    else:
        dayup=(1-dayfactor)*dayup
print("工作日的力量：{:.2f}".format(dayup))
    
 
