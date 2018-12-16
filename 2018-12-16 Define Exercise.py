def number_a(n):
    count = 0
    for i in range(1,n+1,2):
        if i < n:
            count += i*2
        else :
            count += n
    print("和为{:.2f}".format(count))
def number(x):
    a = x%2
    if a == 1 :
        number_a(x)
    else:
        number_a(x-1)
def he(x):
    for i in range(1,x+1):
        number(i)
he(5)
