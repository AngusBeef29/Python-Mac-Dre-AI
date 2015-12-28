# An attempt to implement some functionality.
# no text messaging support.
# Some NLP functionality. Tons of bugs.

from PyDictionary import PyDictionary
from os import system
from textblob import TextBlob
import datetime
import re, string
import script_music

def clean_input(string):
	regex = re.compile("[^a-zA-Z ']")
	return regex.sub('',string)

# def learn_word():
# 	print("I don't know what you want me to do. Perhaps I can learn your command.")
# 	print("This is the functionality you can build upon:")
# 	words = raw_input("Would you like to add the word that you thought I'd understand?\n")

now = datetime.datetime.now()
music_keys = ['music', 'spotify', 'tunes', 'song', 'songs']

def create_synonym_list(word_list):
	dictionary = PyDictionary(word_list)
	new_list   = word_list
	for entries in dictionary.getSynonyms():
		key = entries.keys()[0]
		new_list.append(key)
		for word in entries[key]:
			new_list.append(word)
	return new_list

def answer_logic(answer):
	answer = clean_input(answer)
	positive = create_synonym_list(["yes","definitely","absolutely","sure", "yeah"])
	moderate = create_synonym_list(["maybe", "possibly"])
	negative = create_synonym_list(["no","nope","unlikely","not"])
	words  = answer.split(' ')
	for word in words:
		if word in positive:
			return True
		if word in moderate:
			return answer_logic(raw_input("So is that a yes or a no?\n"))
		if word in negative:
			return False
	nlp_words  = TextBlob(answer)
	sentiment = nlp_words.sentences[0].sentiment.polarity
	if sentiment > 0:
		return True
	elif sentiment == 0:
		return answer_logic(raw_input("So is that a yes or a no?\n"))
	else:
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
		word = word.lower()
		if word in music_keys:
			script_music.main(word_list)
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
	# learn_word()
	print ("What did you want?")

active = True
salutation = define_salutation(now)
print('Good '+salutation)
while active:
	usr_list = raw_input('How may I be of service?\n').split(' ')
	print(usr_list)
	command_finder(usr_list)
	try_again  = raw_input('Would you like anything else?\n')
	if not answer_logic(try_again):
		active = False
	else:
		print ('Awesome.\n')
		command_finder(try_again.split(' '))


