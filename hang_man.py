import random
from words import words
import pics
import os
import time

# Functions

def get_word():
    word = random.choice(words.split(', '))
    return word.upper()


def play_game():
    play = input("Start a new game?(y/n): ")
    return play == "y"


def screen():
    clear()
    print(pics.pics[bad_choices])
    print(" ".join(progress) + "    " + " ".join(letters_tried))


def clear():
    os.system('cls||clear')


clear()
print(pics.title)
time.sleep(3)

while True:
    clear()
    print('Lets get started!')
    word = get_word()
    bad_choices = 0
    progress = ["_"] * len(word)
    letters_tried = []
    while True:
        screen()
        choice = input("\nPick a letter: ")

        if choice.upper() in word:
            for i in range(len(word)):
                if word[i] == choice.upper():
                    progress[i] = word[i]
        else:
            bad_choices += 1
            letters_tried.append(choice.upper())

        if "_" not in progress:
            screen()
            print("\nWell done!")
            break
        elif bad_choices > 6:
            screen()
            print("\nYou lose! The word was - {}".format(word))
            break
        else:
            continue
    if input("\nPlay again?(y/n) ") != 'y':
        clear()
        print("\nThanks for playing Hangman!\n")
        break
