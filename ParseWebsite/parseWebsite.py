'''
this script loads an html file 'web.html' and searches all alexa utterance 
voice to text translations, and prints them.

This script should be modified to access the website automatcally and keep jumping page to page downloading and parsing the website.
So this code could be all found inside a function tat is called very time a new website is opened and parsed
'''

from bs4 import BeautifulSoup as bs
import urllib
import re

quote_page = "web.html"




def findAllUtterances(data):

	soup = bs(data, "html.parser")
	voice_comms = soup.findAll("div", attrs={"class": "textInfo"})


	c = 0
	for el in voice_comms:
		#We are trying to find the utterance text in the website
		msg = el.find("div", attrs={"class":"summaryCss"})		
		if(msg):
			msg = msg.text.strip()
		else:
			msg = el.find("div", attrs={"class":"summaryNotAvailableCss"}).text.strip()
		#datettime of the utterance			
		datetime = el.find("span", attrs={"class":"subInfo"}).text.strip()		

		print('\n\n {} - {} \n {}'.format(c, datetime, msg ))
		c+=1


with open(quote_page, 'r') as myfile:
	data=myfile.read()
	findAllUtterances(data)