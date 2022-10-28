#!/usr/bin/env python3
""" system module """
import string

SYMBOLS = string.ascii_letters
KEY = len(SYMBOLS)

def encrypt(user_msg, user_key):
    """ Encrypt function"""
    cipher_msg = ""
    for char in user_msg:
        char_index = SYMBOLS.find(char)
        cipher = (char_index + (user_key)) % KEY
        cipher_msg += SYMBOLS[cipher]
    return cipher_msg


def decrypt(cipher_msg, user_key):
    """
    Decrypt function
    """
    decrypt_msg = ""
    for char in cipher_msg:
        cipher_index = SYMBOLS.find(char)
        plain_text = cipher_index - (user_key)
        decrypt_msg += SYMBOLS[plain_text]
    print(decrypt_msg)


def bruteforce(user_msg, user_key):
    """
    bruteforce function all combinations value
    """
    for index in range(len(SYMBOLS)):
        print(f"{index}:{encrypt(user_msg, user_key)}")
        user_msg = encrypt(user_msg, user_key)


def user_mode(user_ip, user_key):
    """
    user selection mode function
    """
    flag = 1
    while flag:
        try:
            mode = int(input("enter your mode selection \n1) encrypt\n2) decrypt\n3) bruteforce\n"))
        except ValueError:
            print("Invalid integer. Allowed only [1-3]")
            continue
        if 0 < mode < 4:
            flag = 0
            if mode == 1 :
                print(encrypt(user_ip, user_key))
            elif mode == 2:
                decrypt(user_ip, user_key)
            elif mode == 3:
                bruteforce(user_ip, user_key)
        else:
            print("Invalid key, please choose option [1-3]")
            continue


def secret_key(user_ip):
    """
    user encryption or decryption key value
    """
    while True:
        try:
            user_key = int(input("Enter your key number (1-51) :"))

        except ValueError:
            print("Allowed only whole integer value")
            continue

        if 0 <= user_key < len(SYMBOLS):
            user_mode(user_ip, user_key)
            break

        print("Invalid Number! number limit (1-51)")
        continue


def main():
    """ ceaser program main function """
    while True:
        user_ip = input("Enter you message : ")
        if user_ip.isalpha() is True:
            secret_key(user_ip)
            break
        print("Invalid character. Character allowed only(A-z)")
        continue


def user_play():
    """ user_play in ceaser game"""
    play = "yes"
    while play == "yes":
        main()
        play = input("Do You want to play again (yes or no)  : ")
    print("Thanks for participation")


if __name__ == "__main__":
    user_play()
    