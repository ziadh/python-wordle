import random
import json


def get_colored_word(word, guess):
    colored_word = ""
    for i in range(len(word)):
        if word[i] == guess[i]:
            colored_word += "\033[92m" + word[i] + "\033[0m"  # green
        elif guess[i] in word:
            colored_word += "\033[93m" + guess[i] + "\033[0m"  # yellow
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
        print("You win!")
        break
    else:
        tries -= 1
        print("Incorrect. You have {} tries left.".format(tries))
        colored_word = get_colored_word(word, guess)
        print("Word: {}".format(colored_word))
if tries == 0:
    print("You lost! The word was "+word+"!")
