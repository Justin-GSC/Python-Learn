import random
guess = eval(input("请输入你猜的数字(0-100):"))
number = random.randint(0,100)
while guess != number:
    if guess > number:
        guess=eval(input("比你猜的要小，请继续输入:"))
    elif guess < number:
        guess=eval(input("比你猜的要大，请继续输入:"))
print("\n"+"\n"+"恭喜你猜对了!")
