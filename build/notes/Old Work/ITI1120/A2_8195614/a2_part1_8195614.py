# Course:  IT1 1120 
# A2 Part 1
# McDonald, John (Brennan)
# 8195614
import random

def perform_test(operation, n):
	correct = 0
	if not operation:
		print("Please give the answers for the following additions:")
		for i in range(n):
			n1 = round(random.random() * 10)
			n2 = round(random.random() * 10)
			if (int(input(str(n1) + " + " + str(n2) + " = ")) == n1 + n2):
				correct += 1
			else:
				print("Incorrect - the answer is " + str(n1 + n2))
	elif operation:
		print("Please give the answers for the following multiplications:")
		for i in range(n):
			n1 = round(random.random() * 10)
			n2 = round(random.random() * 10)
			if (int(input(str(n1) + " * " + str(n2) + " = ")) == n1 * n2):
				correct += 1
			else:
				print("Incorrect - the answer is " + str(n1 * n2))
	return correct

print("Welcome to addition / multiplication test \n")

print("How many questions would you like to be tesed on?")
q = input("Enter a non negative integer for the answer: ")
q = int(q)
if q == 0:
	print("Good Bye")
	exit()
print("This software tests you with " + str(q) + " questions ......")

print("0) Addition")
print("0) Multiplication")
t = input("Please make a selection (0 or 1): ")
t = int(t)
r = perform_test(t,q)
if (r / q) * 100 < 80:
	print("Not too bad but please study and practice some more.")
elif  (r / q) * 100 > 80:
	print("Well done! Congratulations")


