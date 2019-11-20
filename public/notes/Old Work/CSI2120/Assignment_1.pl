r1(X) :- f2(X).
r1(X) :- f1(X),r1(Y), f3(Y).
r2(X,Y) :- f3(Y),r1(Y),f1(X).
f1(a).
f1(b).
f2(c).
f2(a).
f3(c).
f3(a).
f3(b).
