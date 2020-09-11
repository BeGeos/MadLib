import random_list as rl
import choice_list as cl
import option_list as ol
import time

print('\nWelcome and be ready to play this wonderful game: MAdLiB')

while True:
    letter_choice = input('\nPlease choose an option. Either love letter or friends:  ')

    if letter_choice == 'love letter':
        letter = ol.loveletter()
        break
    elif letter_choice == 'friends':
        letter = ol.friends()
        break
    else:
        print('Looks like that file does not exist', letter_choice)
        continue
while True:

    option = input('\nPlease choose your words, either random or write:  ')

    if option == 'random':
        objects = rl.RandomGen()
        nouns = objects.nouns
        verbs = objects.verbs
        adj = objects.adj
        break
    elif option == 'write':
        nouns = cl.choice_noun()
        verbs = cl.choice_verb()
        adj = cl.choice_adj()
        break
    else:
        print("It's either random or write")
        continue

print('The story is ready')
time.sleep(1)
letter = ol.replaceletter(letter,nouns, verbs, adj)
print(letter)
print('\nThe end.')