ask(A,S):-
	like(A),
	related-action(A,S),
	\+ previous(S);
	unrelated-random(A,S),
	\+ previous(S).

ask(S):-
	random(S).

part-of(S,[S|_]).
part-of(S,[_|X]):- 
	part-of(S,X).

related-action(X,Y):-
	play(P),
	part-of(X,P),
	part-of(Y,P).

related-action(X,Y):-
	eat(E),
	part-of(X,E),
	part-of(Y,E).

related-action(X,Y):-
	do(D),
	part-of(X,D),
	part-of(Y,D).

related-action(X,Y):-
	see(C),
	part-of(X,C),
	part-of(Y,C).

related-action(X,Y):-
	learn(L),
	part-of(X,L),
	part-of(Y,L).

related-action(X,Y):-
	make(M),
	part-of(X,M),
	part-of(Y,M).

random(S):-
	related-action(P,S).

unrelated-random(O,S):-
	random(S),
	\+ related-action(O,S).

play([slides, sandbox, toys, trains, cars, playmat, build, bears, soft_toys, alphabets, numbers]).
eat([cake, toffee, candy, sandwich, pizza, cheerios, veggies, fries]).
do([build, veggies, trains, draw]).
see([cake, trains, alphabets, draw]).
learn([alphabets, cars, numbers, draw, words, math]).
make([cake, sandwich, pizza, friends, memories]).

like(nothing).
dislike(nothing).
previous(nothing).
