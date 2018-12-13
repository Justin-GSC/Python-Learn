for i in range(100,1000):
    t = str(i)
    a = t[0]
    b = t[1]
    c = t[2]
    abc = pow(eval(a),3)+pow(eval(b),3)+pow(eval(c),3)
    if abc == i :
        print(i,end=",")
