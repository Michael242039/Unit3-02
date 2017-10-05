#Created by: Michael Taylor
#Created on: October 2, 2017
#Created for ICS3U
#This program is a number guessing game 

import ui
from numpy import random

correct_answer = random.randint(1,10)

def check_answer_button(sender):
	#checks if user input equals CORRECT_ANSWER
	global correct_answer
	
	user_guess = int(view['user_guess_input'].text)
	
	if user_guess == correct_answer:
		view['output_text'].text = 'Correct!
		correct_answer = random.randint(1,10)
	else:
		view['output_text'].text = 'Incorrect!'

view = ui.load_view()
view.present('sheet')
