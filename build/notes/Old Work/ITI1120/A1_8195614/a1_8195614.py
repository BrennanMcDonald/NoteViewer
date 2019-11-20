#################################
# Course:  IT1 1120 	        #
# A1			        #
# McDonald, John (Brennan)      #
# 8195614		        #
#################################

import urllib.request
import json
import math
import turtle

###################################################################
# Question 1
###################################################################
def f2k(t):
	return (t+459.67) * (5/9)

###################################################################
# Question 2
###################################################################
def bibformat_apa(author,title,city,publisher,year):
	return "%(author)s (%(year)s). %(title)s. %(city)s: %(publisher)s." % {"author":author, "year":year, "title":title, "city":city, "publisher": publisher}

###################################################################
# Question 3
###################################################################
def joker():
	name = input("Enter your name: ")
	try:
		response_string = urllib.request.urlopen("http://api.icndb.com/jokes/random?firstName="+ name +"&lastName=").readall().decode('utf-8')
		return str(json.loads(response_string)["value"]["joke"]).replace("  ", " ").replace("&quot;", "\"")
	except:
		return "Jesus can walk on water, but " + name + " can walk on Jesus."

###################################################################
# Question 4
###################################################################
def bibformat_apa_display():
	author = input("What is the Author's name: ")
	title = input("What is the Title of the book: ")
	year = input("What year was the book published in: ")
	publisher = input("Who was the publisher: ")
	city = input("what city was it published in: ")
	bibformat_apa(author,title,city,publisher,year)

###################################################################
# Question 5
###################################################################
def bmi(w,h):
	return (int(w) / (int(h) ** 2)) * 703

###################################################################
# Question 6
###################################################################
def f2fi(f):
	return (math.floor(f),round((f - (math.floor(f))) * 12,3))

###################################################################
# Question 7
###################################################################
def bmi_calculator():
	title = input("What is your appelation (title): ")
	first_name = input("What is your first name: ")
	last_name = input("What is your last name: ")
	height = input("What is your height (in inches): ")
	weight = input("What is your weight (in pounds): ")
	feet = math.floor(int(height) / 12)
	inches = math.floor(int(height)%  12)
	print("""BMI Record for %(title)s %(first_name)s %(last_name)s: 
Subject is %(feet)s feet %(inches)s inches tall and weights %(weight)s pounds.
The subject's BMI is %(BMI)s"""
	 % {"title":title,"first_name":first_name,"last_name":last_name,"feet":feet,"inches":inches,"weight":weight,"BMI":bmi(height,weight)})

###################################################################
# Question 8
###################################################################

def draw_court():
	s=turtle.Screen()
	t=turtle.Turtle(shape='turtle')
	t.speed(500)
	t.penup()
	t.goto(0,-150)
	t.pendown()
	t.goto(0,150)
	t.penup()
	t.goto(0,-30)
	t.pendown()
	t.circle(30)
	for i in [1,-1]:
		t.penup()
		t.goto(300, 150*i)
		t.pendown()
		t.goto(-300, 150*i)
		t.penup()
		t.goto(300*i, 150)
		t.pendown()
		t.goto(300*i, -150)
	for i in [1,-1]:
		t.penup()
		t.goto(-300*i,-120*i)
		t.pendown()
		t.forward(50)
		t.seth(180 if i < 0 else 0)
		t.circle(120, 180)
		t.forward(50)
	for i in [1,-1]:
		t.penup()
		t.goto(-300*i, 35*i)
		t.pendown()
		t.goto(-165*i, 35*i)
		t.penup()
		t.goto(-300*i, -35*i)
		t.pendown()
		t.goto(-165*i, -35*i)
		t.penup()
		t.goto(-165*i, -35)
		t.pendown()
		if i < 0:
			t.penup()
			t.goto(165, 35)
			t.pendown()
		t.circle(35,180)
		t.penup()
		t.goto(165*i, 35)
		t.pendown()
		t.goto(165*i, -35)
	# Uncomment the following line in order to keep the turtle window on screen.
	# turtle.mainloop()


###################################################################
# Question 9
###################################################################

def forms_triangle(a, b, c):
	return a + b > c and a + c > b and b + c > a
 
###################################################################
# Question 10
###################################################################

def change_to_coins(amount):
	amount *= 100
	amount = round(amount)
	coins_list = [1,5,10,25]
	sums = [0]
	for i in range(1, amount+1):
		sums.append(-1)
		for values in coins_list:
			if i-values >=0 and sums[i-values] != -1 and i-values + values == i:
				if sums[i] > sums[i-values] or sums[i] == -1:
					sums[i] = 1 + sums[i-values]
	return sums[amount]
