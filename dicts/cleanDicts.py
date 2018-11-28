######
#this file takes disctionaries [american-english, british-english] and removes those entries
#that have stopwords, apostrophes or start with capital letters
######

#input dictionary files
inputDicts = ['american-english', 'british-english']

def checkCharacter(c, string):
	return c in string

def checkCapitalLetter(string):
	return string[0].isupper()


for dict in inputDicts:
	outputDict = open(dict+"_clean","w") 
	openedFile = open(dict, "r")

	for line in openedFile:
		#print('{} contains {}? {}'.format(line, '\'', checkCharacter('\'', line))) 
		#print('{} startsWithCapital? {}'.format(line, checkCapitalLetter(line))) 
		if( not(checkCharacter('\'', line) | checkCapitalLetter(line)) ):
			outputDict.write(line)


		



