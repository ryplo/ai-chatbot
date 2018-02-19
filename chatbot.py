from pyswip import *
import easygui

def start():
	prolog = Prolog()
	prolog.consult("chatbot.pl")
	play = True
	item = 'slides'
	while play:
		response = ask(item)
		if response == 'Yes':
			prolog.assertz("like(%s)" % (item))
		elif response == 'No':
			prolog.assertz("dislike(%s)" % (item))
		else:
			play = False

	for soln in prolog.query("like(X)"):
		print "likes:", soln["X"]

	for soln in prolog.query("dislike(X)"):
		print "dislikes:", soln["X"]

def ask(item):
	response = easygui.buttonbox('Was there a %s at school today?' % (item), 'Conversation', ('Yes', 'No', 'Quit'))
	return response
start()
