from turtle import *

colormode(255)
r=120
seth(-150)
up()

######## red colr part###########
color('red')
begin_fill()
fd(r)
down()
right(90)
circle(-r,120)
fd(r*3**.5)
left(120)
circle(2*r,120)
left(60)
fd(r*3**.5)
end_fill()
######## green colr part###########
left(180)
color('green')
begin_fill()
fd(r*3**.5)
left(120)
circle(2*r,120)
left(60)
fd(r*3**.5)
left(180)
circle(-r,120)
end_fill()
######## yellow color part ###########
left(180)
circle(r,120)
color('yellow')
begin_fill()
circle(r,120)
right(180)
fd(r*3**.5)
right(60)
circle(-2*r,120)
right(120)
fd(r*3**.5)
end_fill()
######## Blue Circle ################
up()
left(98)
fd(r/20)
seth(60)
color('blue')
down()
begin_fill()
circle(distance(0,0))
end_fill()
ht()
done()
