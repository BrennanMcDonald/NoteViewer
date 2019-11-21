partial_sun(blue_lobeila).
partial_sun(periwinkle).
partial_sun(anemone).
partial_sun(black_eyed_susan).
partial_sun(bleeding_heart).
partial_sun(chrysanthemum).
partial_sun(false_lupine).
partial_sun(heather).
partial_sun(iris).

shade(blue_lobeila).
shade(periwinkle).
shade(impatiens).
shade(periwinkle).
shade(bleeding_heart).

sun(blue_lobeila).
sun(periwinkle).
sun(anemone).
sun(marigold).
sun(black_eyed_susan).
sun(chrysanthemum).
sun(false_lupine).
sun(heather).
sun(iris).


colors(blue_lobeila,[blue]).
colors(impatiens,[red,white,pink]).
colors(periwinkle,[blue]).
colors(anemone,[pink,white]).
colors(marigold,[yellow,orange]).
colors(black_eyed_susan,[yellow]).
colors(bleeding_heart,[pink,white]).
colors(chrysanthemum,[red,yellow,blue,white]).
colors(false_lupine,[yellow]).
colors(heather,[purple]).
colors(iris,[blue,orange,pink,red,white]).
colors(phlox,[purple,red,pink]).

sizes(blue_lobeila,6,12).
sizes(impatiens,12,36).
sizes(periwinkle,0,6).
sizes(anemone,12,36).
sizes(marigold,3,12).
sizes(black_eyed_susan,12,24).
sizes(bleeding_heart,6,12).
sizes(chrysanthemum,12,36).
sizes(false_lupine,12,96).
sizes(heather,36,96).
sizes(iris,6,36).
sizes(phlox,12,36).

zones(blue_lobeila,2,11).
zones(impatiens,10,11).
zones(periwinkle,4,9).
zones(anemone,4,8).
zones(marigold,1,12).
zones(black_eyed_susan,3,11).
zones(bleeding_heart,3,9).
zones(chrysanthemum,5,9).
zones(false_lupine,4,8).
zones(heather,4,8).
zones(iris,3,9).
zones(phlox,2,11).

annual(blue_lobeila).
annual(impatiens).
annual(marigold).
annual(black_eyed_susan).
annual(phlox).

perennial(chrysanthemum).
perennial(bleeding_heart).
perennial(periwinkle).
perennial(anemone).
perennial(chrysanthemum).
perennial(false_lupine).
perennial(heather).
perennial(iris).

hardy(P) :-
    zones(P,X,Y),
    Y > 6,
    sizes(P,X1,Y1),
    Y1 >= 48,
    perennial(P).

trio(P1,X,P2,Y,P3,Z) :-
    colors(X,C1),
    contains(P1,C1),
    colors(Y,C2),
    contains(P2,C2),
    colors(Z,C3),
    contains(P3,C3).

contains(I,[I|T]).
contains(I,[H|T]) :-
    contains(I,T).

suggestion(P1,P2) :- P1,P2.

paul(X) :- 
    colors(X,C1),
    not(contains(yellow,C1)),
    zones(X,Z1,Z2),
    Z1 =< 7,
    7 =< Z2.

mary(Y) :- 
    sizes(Y,S1,S2),
    S1 =< 36,
    36 =< S2,
    zones(Y,Z1,Z2),
    Z1 =< 7,
    7 =< Z2.

