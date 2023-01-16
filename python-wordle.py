import random
import json
from time import sleep
import os
import time


import keyboard
from colorama import init, Back, Style, Fore
from InquirerPy import inquirer, prompt
from InquirerPy.separator import Separator
import requests
import webbrowser

version = "2.32"
r = requests.get("https://api.github.com/repos/ziadh/python-wordle/releases")
json_data = r.json()
newest_version = json_data[0]["tag_name"]


def version_checker():

    update_choice = input(
        "There's a new version available. Would you like to update? y/n \n")
    if update_choice.lower() == "y" or update_choice.lower() == "" or update_choice.lower() == " ":
        print("Downloading update... \nPress any of the arrow keys to continue")
        download_update()


def download_update():
    link = "https://github.com/ziadh/python-wordle/archive/refs/tags/"+newest_version+".zip"
    webbrowser.open(link)


os.system(f"title Wordle Python v{version}")

init()

global total_wins
global total_losses


def main_menu():
    print(f"Welcome to Python-Wordle!V{version}")
    if float(newest_version) > float(version):
        version_checker()

    menu_choices = [
        "Play the game",
        "Instructions",
        "Credits",
        "Exit",
    ]

    choice = inquirer.select(
        message=f"\nPlease select an option:",
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


wins = 0
losses = 0


def play_game():
    global wins
    global losses

    won_game = False

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

    with open("src/guess-words.json", "r") as f:
        guess_words = json.load(f)
    word = random.choice(guess_words)

    with open("src/accepted-words.json", "r") as f:
        accepted_words = json.load(f)

    tries = 6
    while tries > 0:
        guess = input("Enter your guess: ").lower()
        # ONLY UNCOMMENT THIS FOR DEV REASONS
        # print(word)
        if guess == word:
            print(word)
            print("Congrats, you won!")
            wins += 1
            won_game = True

            with open("src/stats.json", "w") as f:
                json.dump({"wins": wins}, f)
            if wins > 1:
                print(f"You are on a {wins}-game winning streak!")
                sleep(1)
            playagain = input("Would you like to play again? y/n \n")
            if playagain == "y" or playagain == "Y":
                play_game()
            else:
                os.system('cls')
                main_menu()
        elif len(guess) > 5 or len(guess) < 5:
            print("Invalid length. Please try again.")
        elif guess not in accepted_words:
            print("Word does not exist. Please try again.")
            sleep(1)
            print("You still have {} tries left.".format(tries))
        else:
            tries -= 1
            print("Incorrect. You have {} tries left.".format(tries))
            colored_word = get_colored_word(word, guess)
            print("Word: {}".format(colored_word))
    if tries == 0:
        losses += 1
        with open("src/stats.json", "w") as f:
            json.dump({"wins": wins, "losses": losses}, f)
        print("You lost! The word was "+word+"!")
        playagain = input("Would you like to play again? y/n \n")
        if playagain == "y" or playagain == "Y":
            play_game()
        else:
            os.system('cls')
            main_menu()
    with open("src/stats.json", "w") as f:
        json.dump({"wins": wins, "losses": losses}, f)


def instructions():
    print("You have 6 tries to guess the 5-letter word. If you get a green color that means that the letter belongs in the spot. \n Yellow implies that the letter goes in a different spot. Black means the letter doesn't belong in this word.\n")
    print(Fore.RED + "Press F5 at any time if you wish to go back to the main menu.")
    while True:
        if keyboard.read_key() == "f5":
            os.system('cls')
            main_menu()
            break


def show_credits():
    print("This game was inspired by the original Wordle game available on the NYT Games website.\n")
    print(Fore.RED + "Press F5 at any time if you wish to go back to the main menu.")
    while True:
        if keyboard.read_key() == "f5":
            os.system('cls')
            main_menu()
            break


main_menu()
