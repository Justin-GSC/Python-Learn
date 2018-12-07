#DayDayUpQ2.py
dayfactor=0.01 #bianliang
dayup=pow(1+dayfactor,365)
daydown=pow(1-dayfactor,35)
print("向上:{:.2f}，向下:{:.2f}".format(dayup,daydown))
