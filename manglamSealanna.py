#!/usr/bin/env python
import random

words = ["python", "féile", "haiceáil", "coláiste", "íosagáin", "fiontar", "Gaeilge", "cluiche", "códáil", "ríomhchlárú", "foghlaim"]

random_word = random.choice(words)

#print('Seo focal randamach dhuit', random_word)
print('*********** CLUICHE MANGLAM FOCLA ***********')

#stóráilfear buille faoi thuairim anseo
user_guesses = ''
#cé mhéad seal a bheas ag an imreoir
chances = 10

#fad agus atá seal fágtha, AKA: an uimhir níos mó ná 0
while chances > 0:
    wrong_guesses = 0
    for character in random_word:
        if character in user_guesses:
            print(f"Litir cheart: {character}")
        else:
            wrong_guesses += 1
            print('_')

    if wrong_guesses == 0:
        print("\nCeart!\n")
        print(f"An focal a bhí uaim ná: {random_word}")
        break
    print('\n==============================')
    guess = input('Tabhair buille faoi thuairim: ')
    user_guesses += guess

    if guess not in random_word:
        chances -= 1
        print(f"Mí-cheart. Tá {chances} seal fágtha agat...\n")

        if chances == 0:
            print('\n\nNíl seal ar bith fágtha agat - na Ríomhairí abú!\n\n\tmÚHaHAhAHAhaHAH!')