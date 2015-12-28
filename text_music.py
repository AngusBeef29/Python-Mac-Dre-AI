# TEXT implementation
from os import system
import text

play_keys = ['request','requests','play']

def play_music():
	song = text.input("What song was it that you wanted to hear?")
	system('spotify play [' + song + ']')

def music_logic(word):
	if word in play_keys:
		play_music()
	elif word == 'resume':
		system('spotify play')
	elif word == 'pause':
		system('spotify pause')
	elif word == 'back':
		system('spotify prev')
	elif word == 'skip':
		system('spotify next')

def main():
	print ('Entering DJ mode...')
	active = True
	current_commands = text.input('Alright, Spotify is open.').split(' ');
	while active:
		for word in current_commands:
			word = word.lower()
			if word == 'quit':
				text.send('Dope, leaving DJ mode.')
				return
			music_logic(word)
		cur_str = text.input('Anything else, DJ?')
		print(cur_str)
		current_commands = cur_str.split(' ')
		# current_commands = text.input("What's next?").split(' ')

