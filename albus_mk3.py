# Can send weather and translate simple phrases
# Limited control over Spotify
# Has text messaging support.
# Some NLP functionality.

from os import system
import sys, inspect
import text
import datetime
import re, string
import text_music, text_weather, text_translate
import functions

file = open("new_text.txt", "w")
file.write("")
file.close

now = datetime.datetime.now()
music_keys = ['music', 'spotify', 'tunes', 'song', 'songs','play']

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
	text.send("You can ask me to play a song, take a note, give you the weather, send you a reminder, translate a phrase to English, or order you Dominos. Let me know if you'd like one of these tasks fulfilled.")

def command_finder(word_list):
	if "help" in word_list:
		display_help();
		return
	for word in word_list:
		word = word.lower()
		if word in music_keys:
			text_music.main()
			return
		elif word == "note":
			#write_to_file(word_list)
			return
		elif word == "weather":
			text_weather.main(word_list)
			return
		elif word == "remind":
			#planner_logic(word_list)
			return
		elif word == "translate":
			text_translate.main()
			return
		elif word == "dominos":
			#dominos_logic(word_list)
			return
		elif word == "quit":
			sys.exit()
	# learn_word()
	print ("Ambiguous command")

active = True
salutation = define_salutation(now)
# text.send('Good '+salutation)
while active:
	usr_str = text.input('How may I be of service?')
	usr_list = usr_str.split(' ')
	command_finder(usr_list)
	try_again  = text.input('Would you like anything else?')
	if not functions.answer_logic(try_again):
		active = False
	else:
		command_finder(try_again.split(' '))


