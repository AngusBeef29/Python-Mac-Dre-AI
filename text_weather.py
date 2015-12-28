# -*- coding: utf-8 -*-
import pywapi
import text

def get_weather(zipcode):
	weather_dict = pywapi.get_weather_from_yahoo(zipcode,units='imperial')
	cur_location = weather_dict['location']['city']
	cur_weather = weather_dict['condition']['text']+', at '+weather_dict['condition']['temp']+u'°F'
	cur_sunset  = weather_dict['astronomy']['sunset']
	cur_high = weather_dict['forecasts'][0]['high']+u'°F'
	cur_low  = weather_dict['forecasts'][0]['low']+u'°F'
	text.send('In '+cur_location+', it is currently '+cur_weather+'. The sun sets at '+cur_sunset+'. The high is '+cur_high+' and the low is '+cur_low)


def main(commands):
	print ('Sending weather...')
	has_zip = False
	while has_zip is False:
		for word in commands:
			if len(word) == 5 and word.isdigit():
				get_weather(word)
				return
		commands = text.input('So sorry, what was your zipcode?').split(' ')
