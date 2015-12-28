"""
Does very few things! Actually, it only salutes people and
displays a help text. The eventual format is there, however.

"""



from PyDictionary import PyDictionary
from os import system

from textblob import TextBlob
import datetime
import string

now = datetime.datetime.now()


def create_synonym_list(word_list):
	dictionary = PyDictionary(word_list)
	new_list   = word_list
	for entries in dictionary.getSynonyms():
		key = entries.keys()[0]
		new_list.append(key)
		for word in entries[key]:
			new_list.append(word)
	return new_list

def answer_logic(words):
	positive = create_synonym_list(["yes","definitely","absolutely","sure", "yeah"])
	moderate = create_synonym_list(["maybe", "possibly"])
	negative = create_synonym_list(["no","nope","unlikely","not"])
	words  = words.split(' ')
	for word in words:
		if word in positive:
			return True
		if word in moderate:
			return answer_logic(raw_input("So is that a yes or a no?"))
		if word in negative:
			return False

def define_salutation(t):
	late  = list(range(0,5))
	early = list(range(5,8))
	morning = list(range(8,11))
	day = list(range(11,17))
	if t.hour in late:
		salutation = "evening, sir. My, it is late."
	elif t.hour in early:
		salutation = "morning, sir. You're up early!"
	elif t.hour in morning:
		salutation = "morning, sir."
	elif t.hour in day:
		salutation = "day, sir."
	else:
		salutation = "evening, sir."
	return salutation

def display_help():
	print("You can ask me to play a song, take a note, give you a fun fact or a pickup line or the weather, send you a reminder, or order you Dominos. Let me know if you'd like one of these tasks fulfilled.")

def command_finder(word_list):
	if "help" in word_list:
		display_help();
		return
	for word in word_list:
		if word == "music":
			#spotify_logic(word_list)
			return
		elif word == "note":
			#write_to_file(word_list)
			return
		elif word == "fact":
			#display_fact()
			return
		elif word == "pickup":
			#display_line()
			return
		elif word == "remind":
			#planner_logic(word_list)
			return
		elif word == "weather":
			#weather_logic(word_list)
			return
		elif word == "dominos":
			#dominos_logic(word_list)
			return
	learn_word()	

active = True
salutation = define_salutation(now)
print('Good '+salutation)
while active:
	usr_string = raw_input('How may I be of service?\n')
	usr_list   = usr_string.split(' ')
	print(usr_list)
	command_finder(usr_list)
	try_again  = raw_input('Would you like anything else?\n')
	if not answer_logic(try_again):
		active = False

def learn_word():
	print("I don't know what you want me to do. Perhaps I can learn your command.")
	print("This is the functionality you can build upon:")
	words = input("Would you like to add the word that you thought I'd understand?")
	if answer_logic(words):
		print("Command learned! (Not yet really though actually this is just a test)")
		# LEARN COMMAND


