#!/usr/bin/env python3
""" system module """
import random


NO_OF_GUESSES = 10


def main():
    """
    play function of bagels game
    """
    print(
        "I am thinking of a 3-digit number. Try to guess what it is."
        "The clues I give are...\nWhen I say:    That means:\n"
        "Bagels   -   None of the digits is correct.\n"
        "Pico     -   One digit is correct but in the wrong position.\n"
        "Fermi    -   One digit is correct and in the right position.\n"
        "\nI have thought up a number. You have 10 guesses to get it.\n"
    )
    number = random.randint(100, 1000)
    number = list(str(number))
    count = 1

    while count <= NO_OF_GUESSES:
        try:
            guess = int(input(f'Guess: {count} # '))

        except ValueError:
            print("Invalid Value! Allowed only (100-999)")
            continue

        if 99 < guess <= 999:
            guess = list(str(guess))
            status = bagels_validate(number, guess)
            if status is True:
                break
            count += 1
        else:
            print("Invalid Number! number limit (100-999)")


def bagels_validate(number, guess):
    """
    bagels_validate
    """
    clue = []
    for idx, element in enumerate(number):
        if number == guess:
            print("You got it!")
            return True
        if element == guess[idx]:
            clue.append("fermi")
        elif element in guess:
            clue.append("pico")
    if len(clue) == 0:
        clue.append("bagels")
    print(" ".join(clue))
    return False

def bagels_play():
    """ user main function """
    user_ip = "yes"
    while user_ip == "yes":
        main()
        user_ip = input("Do You want to play again (yes or no)  : ")
    print("Thanks for participation")


if __name__ == "__main__":
    bagels_play()
