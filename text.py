from os import system
from time import sleep
import functions

def read():
	with open ('new_text.txt','r') as f:
		return functions.clean_input(f.read())

def send(response):
	command1 = "osascript -e \'tell application \"Messages\" to send \""
	command2 = "\" to buddy \"Geoffrey Angus\"\'"
	keyText = command1 + response + command2 
	system(keyText.encode('utf-8'))

def input(question):
	send(question)
	old_str = read()
	new_str = old_str
	while old_str == new_str:
		sleep(0.1)
		new_str = read()
	return new_str