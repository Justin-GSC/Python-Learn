import turtle as t
def koch(size,n):
    if n == 0:
        t.fd(size)
    else:
       for angle in [0,90,-90,-90,90]:
           t.left(angle)
           koch(size/5,n-1)
def main(size):
    t.setup(800,800)
    t.penup()
    t.goto(-200,100)
    t.pendown()
    t.pensize(2)
    for i in range(4):
        koch(size,1)
        t.right(90)
    t.hideturtle()
        
main(500)

