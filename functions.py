from textblob import TextBlob
import string
import sys
from os import system
from PyDictionary import PyDictionary
import text


def clean_input(input):
	new_str = [x.strip(string.punctuation) for x in input.split()]
	return ' '.join(new_str)

def stop_running():
	print('and here we are')
	system('echo 0 > is_running.txt')

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
	print(answer)
	positive = create_synonym_list(["yes","definitely","absolutely","sure", "yeah"])
	moderate = create_synonym_list(["maybe", "possibly"])
	negative = create_synonym_list(["no","nope","unlikely","not"])
	words  = answer.split(' ')
	for word in words:
		if word in positive:
			return True
		if word in moderate:
			return answer_logic(text.input("So is that a yes or a no?\n"))
		if word in negative:
			return False
	nlp_words  = TextBlob(answer.decode('utf-8'))
	print(nlp_words)
	sentiment = nlp_words.sentences[0].sentiment.polarity
	print(sentiment)
	if sentiment > 0:
		return True
	elif sentiment == 0:
		return answer_logic(text.input("So is that a yes or a no?\n"))
	else:
		return False
