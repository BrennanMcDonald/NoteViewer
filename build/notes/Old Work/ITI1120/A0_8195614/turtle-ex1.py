# Course:  IT1 1120 
# Exercise 1
# McDonald, John (Brennan)
# 8195614

import turtle
s=turtle.Screen()
t=turtle.Turtle()

# Place your code after this line

# Draw line from [-100, 0] to [100, 0]
t.penup()
t.goto(-100,0)
t.pendown()
t.goto(100,0)

# Draw line from [0, -100] to [0, 100]
t.penup()
t.goto(0,-100)
t.pendown()
t.goto(0,100)

# Draw line from [-100, -100] to [100, 100]
t.penup()
t.goto(-100,-100)
t.pendown()
t.goto(100,100)

# Draw line from [100, -100] to [-100, 100]
t.penup()
t.goto(100,-100)
t.pendown()
t.goto(-100,100)

# Draw circles 
t.penup()
t.goto(0,0)
t.pendown()
t.goto(0,-10)
t.circle(10)
t.goto(0,-20)
t.circle(20)
t.goto(0,-40)
t.circle(40)
t.goto(0,-80)
t.circle(80)
