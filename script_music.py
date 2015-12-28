# basic implementation of music playing functionality!

from os import system

def play_music(commands):
	song = raw_input("What song was it that you wanted to hear?\n")
	if not 'by' in song:
		system('spotify play [' + song + ']')

def main(commands):
	print ('Entering DJ mode...')
	active = True
	current_commands = commands;
	while active:
		for word in current_commands:
			if word == 'quit':
				system('spotify quit')
				print ('Leaving DJ mode...')
				return
			elif word == 'play':
				play_music(commands)
				break
			elif word == 'resume':
				system('spotify play')
				break
			elif word == 'pause':
				system('spotify pause')
				break
			elif word == 'back':
				system('spotify prev')
				break
			elif word == 'skip':
				system('spotify next')
				break
		# current_commands = raw_input('What\'s next?\n').split(' ')

