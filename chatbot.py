import easygui # library for message boxes
import random

from pyswip import * # python and prolog bridge

# Different message starters.
POSITIVE_MESSAGES = ["Great!", "That\'s wonderful!", "Nice!", "Cool!", "Wow!"]
NEGATIVE_MESSAGES = ["Aw that\'s a shame.", "That\'s unfortunate.", "That\'s okay.", "Oh no!"]

# Main function
def start():
	prolog = Prolog()

	# Consult chatbot.pl. Should be in same directory
	prolog.consult("chatbot.pl")

	# Flag to check if user wants to quit
	play = True

	# Variable to save the next item to ask about
	item = ""

	# First intro message
	easygui.msgbox('Let\'s figure out what you did today at school!', 'Conversation Intro')

	ask_message = ""
	# Loop for conversation
	while play:

		# Calls 'ask' in prolog to find the next item to ask about
		# If there is an item (not the first message to be sent), the previously called
		# item will be passed as an argument in the ask query. 
		# If it is the first time a message is being sent (beginning of conversation), 
		# only one argument is passed to get a random item.
		if item:
			item = list(map(lambda x: x["S"], prolog.query("ask(%s,S)" % (item))))[0]
		else:
			item = list(map(lambda x: x["S"], prolog.query("ask(S)")))[0]

		# Calls the ask function to create the message box
		response = ask(item, ask_message)

		# Keeps track of which items were asked about
		prolog.assertz("previous(%s)" % item)

		# If the user did interact with the item, the message begins with a positive response
		# The item is also recorded as having been encountered with in the knowledge base
		if response == 'Yes':
			prolog.assertz("did(%s)" % item)
			ask_message = random.choice(POSITIVE_MESSAGES)

		# If the user did not encounter the item, the message begins with a negative response
		# The item is recorded as being not encountered in the knowledge base
		elif response == 'No':
			prolog.assertz("didnot(%s)" % (item))
			found = False
			ask_message = random.choice(NEGATIVE_MESSAGES)
		else:
			play = False

# Prints out the message in message box with options for Yes, No and Quit
# The value returned from the easygui buttonbox is the string "Yes", "No",
# or "Quit" depending on the user's selection
def ask(item, message=""):
	response = easygui.buttonbox('%s Was there a %s at school today?' % (message, item), 'Conversation', ('Yes', 'No', 'Quit'))
	return response

start()
