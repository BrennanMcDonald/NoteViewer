import turtle
s=turtle.Screen()
t=turtle.Turtle(shape='turtle')
for i in range (-7, 7):
	t.penup()
	t.goto(70 * i,0)
	t.pendown()
	t.setheading(-45)
	t.circle(50,90)

# your code should go right after this line

t.penup()
t.goto(-100,200)
t.pendown()
t.circle(50)
t.penup()
t.goto(0,-50)


