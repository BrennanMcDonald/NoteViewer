s1 = "good"
s2 = "bad"
s3 = "silly"

print("ll" in s3)
print("\ " in s1)
print(s1 + s2 + s3)
print("\ " in (s1 + s2 + s3))
print(s3 * 10)
print(len(s1 + s2 + s3))

print()
print()
print()

aha = "abcdefgh"

print(aha[0:4])
print(aha[3:6])
print(aha[-1])
print(aha[-3:-1])
print(aha[3:])
print(aha[-3:])
print(aha[0] + aha[3] + aha[-2])
print(aha[1] + aha[4])

s = '''It was the best of times, it was the worst of times;
it was the age of wisdom, it was the age of foolishness;
it was the epoch of belief, it was the epoch of incredulity;
it was ...''' 

print(s.replace('.',' ').replace(',',' ').replace(';', ' ').replace('\n', ' '))

print()
print()

print(s.strip())

print()
print()

print(s.lower())

print()
print()

print(s.count("it was"))

print()
print()

print(s.replace("was", "is"))


for i in range(11):
	print(i, end=", " if i != 10 else " ")
print()
for i in range(1,10):
	print(i, end=", " if i != 9 else " ")
print()
for i in range(0, 10, 2):
	print(i, end=", " if i != 8 else " ")
print()
for i in range(1,10,2):
	print(i, end=", " if i != 9 else " ")
print()
for i in range(0,70,10):
	print(i, end=", " if i != 60 else " ")
print()
for i in reversed(range(1,11)):
	print(i, end=", " if i != 1 else " ")