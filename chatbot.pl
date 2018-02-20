/* 
* Ask takes in two arguments (A - previous item. S - new item)
* If this is not the beginning of the conversation, then there was an item
* that the user was previously asked about. This item is passed into ask. 
* If the user encountered the item previously, an item from the related action list will be asked about, 
* and a check is made to ensure that the same item is not asked about twice in a conversation.
* If the user did not encounter the item previously, a new random item that is not part of the same
* action list will be asekd about.
*/
ask(A,S):-
	did(A),
	related-action(A,S),
	\+ previous(S);
	unrelated-random(A,S),
	\+ previous(S).

/*
* If it is the beginning of the conversation, and no item is passed into the ask query, 
* a random item is selected.
*/
ask(S):-
	random(S).

/*
* Checks whether or not an item is part of an existing list of actions.
*/
part-of(S,[S|_]).
part-of(S,[_|X]):- 
	part-of(S,X).

/*
* Gets another item from the same related action list as an item passed into the query
*/
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

/* Queries for a new item */
random(S):-
	related-action(P,S).

/*
* This queries for a new random item that is unrelated to the one passed in.
* See the comment for Ask for more details on when this is used.
*/
unrelated-random(O,S):-
	random(S),
	\+ related-action(O,S).

/* List of actions with related items */
play([slides, sandbox, toys, trains, cars, playmat, build, bears, soft_toys, alphabets, numbers]).
eat([cake, toffee, candy, sandwich, pizza, cheerios, veggies, fries]).
do([build, veggies, trains, draw]).
see([cake, trains, alphabets, draw]).
learn([alphabets, cars, numbers, draw, words, math]).
make([cake, sandwich, pizza, friends, memories]).

/* This is so that prolog is aware of these queries before they are populated with more items */
did(nothing).
didnot(nothing).
previous(nothing).
