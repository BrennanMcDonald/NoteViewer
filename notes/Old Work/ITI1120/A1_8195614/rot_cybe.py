import turtle
import math
s=turtle.Screen()
t=turtle.Turtle(shape='turtle')
t.ht()
t.speed(5000)
def draw_line(x1, y1, x2, y2):
	t.penup()
	t.goto(x1, y1)
	t.pendown()
	t.goto(x2, y2)
	t.penup()

def rotate_cube():
	t.speed(5000)
	x = 0
	while True:
		x += 1
		n = round(math.cos(math.radians(x)),100) * 100
		y = round(math.sin(math.radians(x)),100) * 100
		draw_line(y,n,n,y)

def draw_cube(x,y,s, a=0):
	#x = math.cos(math.radians(x) * s) + s
	#x = math.sin(math.radians(x) * s) + s
	draw_line(x,y, x+s,y)
	draw_line(x+s,y, x + s, y + s)
	draw_line(x+s,y+s, x, y+s)
	draw_line(x,y+s, x, y)


draw_line(-300,150,300,150)
draw_line(300,150,300,-150)
draw_line(300,-150,-300,-150)
draw_line(-300,-150,-300,150)

draw_line(-175,150,-175,-150)
draw_line(175,150,175,-150)

turtle.mainloop()