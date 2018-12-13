import random
i = 0
x = 0
y = 100
a = 0
b = 100
number = random.randint(0,100)
guess = eval(input("Please input a guess number:"))
while guess != number:
        i = i+1
        if guess > number:
              guess = eval(input("smaller"))
        elif guess < number:
             guess = eval(input("bigger"))
        elif i > 4 :
             print("Sorry ,You lost too much !")
             break
print("Congratulation !")
