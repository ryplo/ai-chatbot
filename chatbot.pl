ask(A,S):-
	related-action(A,S).

ask(A,S):-
	random(S).

part-of(S,[S|_]).
part-of(S,[_|X]):- 
	part-of(S,X).

related-action(P,S):-
	play(P),
	part-of(S,P).

related-action(E,S):-
	eat(E),
	part-of(S,E).

related-action(D,S):-
	do(D),
	part-of(S,D).

related-action(C,S):-
	see(C),
	part-of(S,C).

related-action(L,S):-
	learn(L),
	part-of(S,L).

related-action(M,S):-
	make(M),
	part-of(S,M).

random(S):-
	related-action(P,S).

play([slides, sandbox, toys, trains, cars, playmat, build, bears, soft_toys, alphabets, numbers]).
eat([cake, toffee, candy, sandwich, pizza, cheerios, veggies, fries]).
do([build, veggies, trains, draw]).
see([cake, trains, alphabets, draw]).
learn([alphabets, cars, numbers, draw, words, math]).
make([cake, sandwich, pizza, friends, memories]).

like(nothing).
dislike(nothing).
