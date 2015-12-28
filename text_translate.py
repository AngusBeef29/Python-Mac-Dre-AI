import text
import functions
from textblob import TextBlob

def main():
	while True:
		phrase = text.input('What is the phrase?')
		phrase = TextBlob(phrase.decode('utf-8'))
		translated = "In English, that means:\n"+str(phrase.translate(to='en'))
		translated = translated.replace('\'','`')
		text.send(translated)
		try_again = text.input('Any other phrases?')
		if not functions.answer_logic(try_again):
			return

