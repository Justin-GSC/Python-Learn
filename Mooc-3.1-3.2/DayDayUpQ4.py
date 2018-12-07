#DayDayUpQ4.py
def dayUp(df):
    dayup=1
    for i in range(365):
        if i%7 in [6,0]:
            dayup=(1-0.01)*dayup
        else:
            dayup=(1+df)*dayup
    return dayup
dayfactor = 0.01
while dayUp(dayfactor)<1.01**365:
    dayfactor +=0.001
print("工作日的努力参数是：{:.3f}".format(dayfactor))
