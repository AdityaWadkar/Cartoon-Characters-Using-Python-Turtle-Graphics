
import turtle
import math
import time

def draw_shape():
    window = turtle.Screen()
    time.sleep(2)
    # window.bgcolor("gray=")

    cursor = turtle.Turtle()  # Cursor
    # cursor.shape("turtle")
    cursor.color("black")
    cursor.speed("slowest")
    cursor.pensize(4)

    # Draw the head
    cursor.fillcolor("#f7eac6")
    cursor.begin_fill()
    movePenY(cursor, -150)
    cursor.circle(150)
    cursor.end_fill()



    # Draw the nose

    noseMouthOffset = -15
    cursor.fillcolor("pink")
    cursor.begin_fill()
    movePenY(cursor, -20 + noseMouthOffset)
    cursor.circle(20)
    cursor.end_fill()

    # Draw the mouth

    movePen(cursor, -100, -20 + noseMouthOffset)
    cursor.right(90)
    cursor.circle(50, 180)
    cursor.left(180)
    cursor.circle(50, 180)

    # Draw the eyes

    eyeSpacingX = 30
    eyePosY = 40
    eyeRadius = 30

    # Right eye

    movePen(cursor, eyeSpacingX, eyePosY)
    cursor.right(180)
    cursor.circle(eyeRadius, -180)

    cursor.penup()
    cursor.goto(69,45)
    cursor.fillcolor("#c1eef7")
    cursor.begin_fill()
    cursor.pendown()
    cursor.circle(10)
    cursor.end_fill()
    cursor.penup()
    cursor.goto(60, 45)
    cursor.pendown()
    cursor.circle(1)
    # Left eye

    movePen(cursor, -eyeSpacingX, eyePosY)
    cursor.circle(eyeRadius, 180)

    cursor.penup()
    cursor.goto(-71, 45)
    cursor.fillcolor("#c1eef7")
    cursor.begin_fill()
    cursor.pendown()
    cursor.circle(10)
    cursor.end_fill()
    cursor.penup()
    cursor.goto(-62, 45)
    cursor.pendown()
    cursor.circle(1)

    # # Draw the tongue
    #
    movePen(cursor, -20, -60 + noseMouthOffset)
    cursor.fillcolor("#faaaf9")
    cursor.begin_fill()
    cursor.circle(20, 180)
    cursor.pensize(0)
    cursor.goto(0,-50)
    cursor.pensize(4)
    cursor.end_fill()

    # Draw the ears

    # Right ear


    earBeginAngle = 25
    earSize = 85
    earWidth = 22

    positionA = positionAlongCircle(0, 0, 150, earBeginAngle)
    movePen(cursor, positionA[0], positionA[1])

    positionB = positionAlongCircle(0, 0, 150 + earSize, earBeginAngle + earWidth)
    cursor.setposition(positionB[0], positionB[1])

    positionC = positionAlongCircle(0, 0, 150, earBeginAngle + earWidth * 2)
    cursor.setposition(positionC[0], positionC[1])


    # Left ear

    positionA = positionAlongCircle(0, 0, 150, -earBeginAngle)
    movePen(cursor, positionA[0], positionA[1])

    positionB = positionAlongCircle(0, 0, 150 + earSize, -earBeginAngle + -earWidth)
    cursor.setposition(positionB[0], positionB[1])

    positionC = positionAlongCircle(0, 0, 150, -earBeginAngle + -earWidth * 2)
    cursor.setposition(positionC[0], positionC[1])

    # Whiskers

    whiskerLength = 160

    # Right whiskers

    movePen(cursor, 50, -15)
    cursor.setheading(0)
    cursor.forward(whiskerLength)

    movePen(cursor, 50, 0)
    cursor.left(5)
    cursor.forward(whiskerLength)

    # Left whiskers

    movePen(cursor, -50, -15)
    cursor.setheading(180)
    cursor.forward(whiskerLength)

    movePen(cursor, -50, 0)
    cursor.left(-5)
    cursor.forward(whiskerLength)
    cursor.hideturtle()
    window.exitonclick()


def movePen(cursor, x, y):
    cursor.penup()
    cursor.setposition(x, y)
    cursor.pendown()


def movePenX(cursor, x):
    cursor.penup()
    cursor.setx(x)
    cursor.pendown()


def movePenY(cursor, y):
    cursor.penup()
    cursor.sety(y)
    cursor.pendown()


def positionAlongCircle(x, y, radius, angle):
    radians = math.radians(angle)
    return [x + (radius * math.sin(radians)),
            y + (radius * math.cos(radians))]


draw_shape()
