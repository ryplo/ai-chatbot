import easygui # library for message boxes
import random

from pyswip import * # python and prolog bridge

POSITIVE_MESSAGES = ["Great!", "That\'s wonderful!", "Nice!", "Cool!", "Wow!"]
NEGATIVE_MESSAGES = ["Aw that\'s a shame.", "That\'s unfortunate.", "That\'s okay.", "Oh no!"]

# main function
def start():
	prolog = Prolog()
	prolog.consult("chatbot.pl")

	# flag to check if user wants to quit
	play = True

	# variable to save the next item to ask about
	item = ""

	# first intro message
	easygui.msgbox('Let\'s figure out what you did today at school!', 'Conversation Intro')

	ask_message = ""
	# loop for conversation
	while play:

		# calls 'ask' in prolog to find the next item to ask about
		if item:
			item = list(map(lambda x: x["S"], prolog.query("ask(%s,S)" % (item))))[0]
		else:
			item = list(map(lambda x: x["S"], prolog.query("ask(S)")))[0]

		# calls the ask function to create the message box
		response = ask(item, ask_message)

		# keeps track of which items were asked about
		prolog.assertz("previous(%s)" % item)

		# if the user likes the item, the message begins with a positive response
		# the item is also recorded as being liked
		if response == 'Yes':
			prolog.assertz("like(%s)" % item)
			ask_message = random.choice(POSITIVE_MESSAGES)

		# if the user does not like the item, the message begins with a negative response
		# the item is recorded as being disliked
		elif response == 'No':
			prolog.assertz("dislike(%s)" % (item))
			found = False
			ask_message = random.choice(NEGATIVE_MESSAGES)
		else:
			play = False


def ask(item, message=""):
	response = easygui.buttonbox('%s Was there a %s at school today?' % (message, item), 'Conversation', ('Yes', 'No', 'Quit'))
	return response

start()
