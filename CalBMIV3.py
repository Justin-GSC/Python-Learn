#CalBMIV2.py
height,weight = eval(input("请输入您的身高（米）、体重（公斤）（使用逗号隔开）："))
BMI = weight/pow(height,2)
print("BMI 数值为:{:.2f}".format(BMI))
who, nat = "",""
if BMI < 18.5:
    who, nat ="偏瘦","偏瘦"
elif 18.5<= BMI <24:
    who, nat ="正常","正常"
elif 24<=BMI <25:
    who, nat ="正常","偏胖"
elif 25<=BMI<28:
    who, nat="偏胖","偏胖"
elif 28<=BMI<30:
    who, nat="偏胖","肥胖"
elif BMI>=30:
    who, nat="肥胖","肥胖"
print("\n"+"您的BMI属于：国际{}，国内{}".format(who,nat),end="")