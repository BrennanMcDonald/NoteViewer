def pay(w,h):
	return ((h - 60) * (2 * w) + (h - (h - 60) - 40) * (1.5 * w) + 40 * w) if h >= 60 else ((w * 40 + (w * 1.5) * (h-40)) if (h > 40) else w * h)

def rps(a,b):
	r = lambda a,b: 1 if ord(a) > ord(b) else (-1 if ord(a) < ord(b) else 0)
	return r(a,b) * -1 if (a == 'S' and b == 'P') or (b == 'S' and a == 'P') else r(a,b)

def is_divisible(n,m):
	return (n % m) == 0

def is_divisible_prompt():
	a = input("Enter 1st integer: ")
	b = input("Enter 2nd integer: ")
	p = (str(a) + " is divisible by " + str(b)) if is_divisible(int(a),int(b)) else (str(a) + " is not divisible by " + str(b))
	print(p)

def is_divisible23n8(a):
	return (is_divisible(a,2) or is_divisible(a,3)) and not is_divisible(a,8)

def is_divisible23n8_prompt():
	return is_divisible23n8(int(input("Enter an integer: ")))