
from InquirerPy import inquirer, prompt
from InquirerPy.separator import Separator
import random
import json
from colorama import init, Back, Style
from time import sleep
import keyboard
import os

init()


def main_menu():
    menu_choices = [
        "Play the game",
        "Instructions",
        "Credits",
        "Exit",
    ]

    choice = inquirer.select(
        message="Welcome to Python-Wordle! Please select an option:",
        choices=menu_choices,
        default=menu_choices[0],
    ).execute()

    if choice is menu_choices[0]:
        play_game()
    elif choice is menu_choices[1]:
        instructions()
    elif choice is menu_choices[2]:
        show_credits()
    elif choice is menu_choices[3]:
        print("Terminating program in 3 seconds")
        sleep(3)
        exit()


def play_game():

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
        guess = input("Enter your guess: ").lower()
        if guess == word:
            print("Congrats, you won!")
            playagain = input("Would you like to play again? y/n \n")
            if playagain == "y" or playagain == "Y":
                play_game()
            else:
                print("Terminating application in 5 seconds.")
                sleep(5)
                quit()
            break
        elif len(guess) > 5 or len(guess) < 5:
            print("Invalid length. Please try again.")
        else:
            tries -= 1
            print("Incorrect. You have {} tries left.".format(tries))
            colored_word = get_colored_word(word, guess)
            print("Word: {}".format(colored_word))
    if tries == 0:
        print("You lost! The word was "+word+"!")
        playagain = input("Would you like to play again? y/n \n")
        if playagain == "y" or playagain == "Y":
            play_game()
        else:
            print("Terminating application in 5 seconds.")
            sleep(5)
            quit()


def instructions():
    print("You have 6 tries to guess the 5-letter word. If you get a green color that means that the letter belongs in the spot. \n Yellow implies that the letter goes in a different spot. Black means the letter doesn't belong in this word.")
    print("Press F5 at any time if you wish to go back to the main menu.")
    while True:
        if keyboard.read_key() == "f5":
            os.system('cls')
            main_menu()
            break


def show_credits():
    print("This game was inspired by the original Wordle game available on the NYT Games website.")
    print("Press F5 at any time if you wish to go back to the main menu.")
    while True:
        if keyboard.read_key() == "f5":
            os.system('cls')
            main_menu()
            break


main_menu()
