ack(0,N,A) :- A is N + 1.

ack(M,0,A) :-
	M > 0,
	M1 is M - 1,
	ack(M1,1,A).

ack(M,N,A) :-
	M > 0,
	N > 0,
	M1 is M-1,
	N1 is N-1,
	ack(M,N1,A1),
	ack(M1,A1,A).
