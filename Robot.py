import turtle as t

sc = t.Screen()
# sc.title("মানব রোবট")
def rectangle(horizontal, vertical, color):
    t.pendown()
    t.pensize(2)
    t.color(color)
    t.begin_fill()

    for counter in range(1,3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()

t.penup()
t.speed('slow')
import time
time.sleep(2)
# t.bgcolor('#C70039')

t.goto(-100, -150)
rectangle(50, 20, 'blue')

t.goto(-30, -150)
rectangle(50, 20, 'blue')

t.goto(-25, -50)
rectangle(15, 100, 'grey')
t.goto(-55, -50)
rectangle(-15, 100, 'grey')

t.goto(-90, 70)
rectangle(100, 150, 'black')

t.goto(-150, 70)
rectangle(60, 15, 'grey')
t.goto(-150, 110)
rectangle(15, 48, 'grey')

t.goto(10, 70)
rectangle(60, 15, 'grey')
t.goto(55, 110)
rectangle(15, 40, 'grey')

t.goto(-50, 120)
rectangle(15, 50, 'grey')

t.goto(-85, 170)
rectangle(80, 50, 'green')

t.goto(-60, 160)
rectangle(30,10,'white')
t.goto(-55, 155)
rectangle(5,5, '#581845')
t.goto(-40, 155)
rectangle(5, 5, '#581845')

t.goto(-65, 136)
t.right(5)
rectangle(35, 5, '#581845')
#
t.left(5)
t.goto(-155, 130)
rectangle(25, 25, '#FFC300')
t.goto(-147, 130)
rectangle(10, 15, t.bgcolor())
t.goto(50, 130)
rectangle(25, 25, '#FFC300')
t.goto(58, 130)
rectangle(10, 15, t.bgcolor())


t.hideturtle()

t.done()
