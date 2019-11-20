
sum_int(N,X) :- sum_int(N,0,X).

sum_int(0,X,X).

sum_int(N,Y,X) :- N > 0, N1 is N - 1, Y1 is Y + N, sum_int(N1, Y1, X).
