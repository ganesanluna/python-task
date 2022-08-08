#!/usr/bin/env python3
"""system module"""
import random
import sys


def play():
    game_input = input("Do you want to play again? (yes or no)\n")
    if game_input == "yes":
        print("games continues")
    elif game_input == "no":
        print("games quit. bye!")
        sys.exit()
    else:
        print("Invalid input")

def main():
    """
    Dragon game
    """
    while True:
        while True:
            try:
                message_input = int(input("You are in a land full of dragons. In front of you.\n"
                           	          "you see two caves. In one cave, the dragon is friendly and\n"
                                          "will share his treasure with you. The other dragon is\n" 
                                          "greedy and hungry, and will eat you on sight.\n"
                                          "Which cave will you go into? (1 or 2) "))
                break
            except ValueError:
                print("\nOOPS!Use whole number.Try again\n")

        value = random.randint(1,2)

        if message_input == value :
            print("\nYou approach the cave. It is dark and spooky.\n"
                  "A large dragon jumps out in front of you! He opens his jaws\n"
                  "and Gobbles you down in one bite!\n")
            play()
        else:
            print("You approach the cave. It is look like beautiful\n"
                  "and heaven. A dragon in front of you and gives to\n"
                  "lot of treasures.\n")
            play()

if __name__ == '__main__':
	main()
