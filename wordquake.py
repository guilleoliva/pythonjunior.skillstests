import sys
import string
word=sys.argv[1:]
word2 = ""
for m in range(len(word)):	
	temp = word[m]
	for n in range(len(temp)):
		if n % 2 == 0: # par
			word2 = word2 + (temp[n].upper())
		else: # impar
			word2 = word2 + (temp[n].lower())
	word2 = word2 + ' '
print(word2)
