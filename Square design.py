
import turtle
wn=turtle.Screen()
cube=turtle.Turtle()

squares=50
size=40
angle=20
cube.right(angle)
for _ in range(squares):
    cube.right(angle)
    for _ in range(1):
        #cube.goto(0,0)
        cube.forward(size)
        cube.right(90)
        cube.forward(size)
        cube.right(90)
        cube.forward(size)
        cube.right(90)
        cube.forward(size)
time.sleep(10)
