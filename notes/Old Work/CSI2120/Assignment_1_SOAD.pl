sosd(0,0).
sosd(X,Y) :- 
	X > 0,
	X1 is floor(X / 10),
	sosd(X1,Y1),
	Y is Y1 + (X mod 10) ^ 2.

happyNumber(0) :- !.
happyNumber(4) :- !.
happyNumber(16) :- !.
happyNumber(20) :- !.
happyNumber(37) :- !.
happyNumber(42) :- !.
happyNumber(58) :- !.
happyNumber(89) :- !.
happyNumber(15) :- !.

happyNumber(X) :- X=1,!.
happyNumber(X) :-
	X > 0,
	sosd(X,Y),
	happyNumber(Y),
	Y = 1.
