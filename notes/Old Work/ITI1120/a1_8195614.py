import urllib.request
import json
import math
import turtle
import sys

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
	return (math.floor(f),(f - (math.floor(f))) * 12)

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
	inches = math.floor(int(height) % 12)
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






###################################################################
# Question 9
###################################################################

def forms_triangle(a, b, c):
	return a + b > c and a + c > b and b + c > a
 
###################################################################
# Question 10
###################################################################

def change_to_coins(total):
	coins = [1, 5, 10, 25]
	counts = [None] * (len(coins) + 1)
	counts[0] = 0
	gggg = (int)(total * 100)
	for i in range(gggg):
		count = sys.maxsize
		for j in range(len(coins)):
			if i - coins[j] >= 0 and count > counts[i - coins[j]]:
				count = counts[i-coins[j]]
		if count < sys.maxsize:
			counts[i] = count + 1
		else:
			counts[i] = sys.maxsize
	minCount = counts[total]
	return minCount

def recMC(coinValueList,change):
   minCoins = change
   if change in coinValueList:
     return 1
   else:
      for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recMC(coinValueList,change-i)
         if numCoins < minCoins:
            minCoins = numCoins
   return minCoins

print(recMC([1,5,10,25], 202))