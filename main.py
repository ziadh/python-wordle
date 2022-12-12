# 1.3
# What's new?
# TODO fix the color issue in cmd
# TODO Moar words
# TODO Make the background of the letters colored instead of the letters themselves
# TODO make it a tkinter and enable light mode
import random
import json
from colorama import init, Back, Style
from time import sleep

init()


def get_colored_word(word, guess):
    colored_word = ""
    for i in range(len(word)):
        if word[i] == guess[i]:
            colored_word += Back.GREEN + \
                Style.BRIGHT + word[i] + Style.RESET_ALL
        elif guess[i] in word:
            colored_word += Back.YELLOW + \
                Style.BRIGHT + guess[i] + Style.RESET_ALL
        else:
            colored_word += guess[i]
    return colored_word


with open("words.json", "r") as f:
    words = json.load(f)
word = random.choice(words)

tries = 6
while tries > 0:
    guess = input("Enter your guess: ")
    if guess == word:
        print("Congrats, you won!")
        sleep(3)
        break
    else:
        tries -= 1
        print("Incorrect. You have {} tries left.".format(tries))
        colored_word = get_colored_word(word, guess)
        print("Word: {}".format(colored_word))
if tries == 0:
    print("You lost! The word was "+word+"!")
    sleep(3)
