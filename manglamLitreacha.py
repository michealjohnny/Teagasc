#!/usr/bin/env python
import random

words = ["python", "féile", "haiceáil", "coláiste", "íosagáin", "fiontar", "Gaeilge", "cluiche", "códáil", "ríomhchlárú", "foghlaim"]

word = random.choice(words)

letters = list(word)
#print(letters)

random.shuffle(letters)
#print(letters)

jumbled_word = "".join(letters)
#print(jumbled_word)
print("Cén focal atá sa mhanglam litreacha seo,", jumbled_word)

while True:
	guess = input("Tabhair buille faoi thuairim: ")
	if guess.lower() != word.lower():
		print("Mí-cheart! Bain triail eile as...")
	else:
		break

print("Ceart - Fuair tú é! Comhghairdeas!")