#!/usr/bin/env python3
""" system module"""
import random


def main():
    """
    Guess the number on for loop condition
    """
    value = random.randint(1, 20)
    name = input("Hello, What is your name :\n")
    print(f"Well,{name}, I am thinking of a number between 1 and 20.")
    for var in range(1,7):
        while True:
            try:
                guess = int(input("Take guess\n"))
                break
            except ValueError:
                print("OOPS!Use whole number.Try again\n")
        
        if value < guess:
            print("Your guess is too high\n")
        elif value > guess:
            print("Your guess is too low\n")
        else:
            print(f"Good job,{name}!You guessed my number in {var} guesses!\n")
            break
    
    else:
        print("Sorry,{0} Your guess turn is too much. My Number is {1}."
              "Thanks for your participation" .format(name,guess))


if __name__ == "__main__":
    main()
