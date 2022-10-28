#!/usr/bin/env python3
"""System module"""
import random


def display_board(board):
    """Tic tac toe display board 3x3"""
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print("\n")


def user_turn(player_obj, board):
    """
    If select number between 1 to 9.
    Excees of value 10 and below zero values are not allowed.
    """
    while True:
        try:
            user_pos = int(input("what is your next move? (1-9) :"))
        except ValueError:
            print("Allowed only whole integer value")
        if 0 < user_pos < 10:
            if board[user_pos - 1] in ["X", "O"]:
                print("altready filled\n")
                continue
            board[user_pos - 1] = player_obj
            break
        print("Invalid Number! number limit (1-9)")
    display_board(board)
    return board


def computer_turn(player_obj, board):
    """
    If select number between 1 to 9.
    Filled value is does not select.
    """
    board_check = []
    print("computer Turn :")
    for turn in range(9):
        if board[turn] not in ["X", "O"]:
            board_check.append(turn)
    computer_number = random.choice(board_check)
    board[computer_number - 1] = player_obj
    display_board(board)
    board_check.clear()
    return board


def check_win(board, player):
    """Player checking for win status"""
    return (board[0] == board[1] == board[2] == player or
            board[3] == board[4] == board[5] == player or
            board[6] == board[7] == board[8] == player or
            board[0] == board[3] == board[6] == player or
            board[1] == board[4] == board[7] == player or
            board[2] == board[5] == board[8] == player or
            board[0] == board[4] == board[8] == player or
            board[2] == board[4] == board[6] == player)


def get_computer_objects(user_obj):
    """Computer Objects"""
    if user_obj == "X":
        computer_obj = "O"
    else:
        user_obj = "X"
    return computer_obj


def main():
    """Main function of tictactoe"""
    board_list = list(range(1, 10))
    user_obj = input("Do you want to be X or O :")
    user_obj = user_obj.upper()
    computer_obj = get_computer_objects(user_obj)
    i = 0
    display_board(board_list)
    while i < len(board_list):
        if (i % 2) == 0:
            user_turn(user_obj, board_list)
            if check_win(board_list, user_obj) is True:
                print("User Win")
                break
        else:
            computer_turn(computer_obj, board_list)
            if check_win(board_list, computer_obj) is True:
                print("Computer Win")
                break
        i += 1


def tictactoe_play():
    """Play tictactoe game"""
    user_ip = "yes"
    while user_ip == "yes":
        main()
        user_ip = input("Do You want to play again (yes or no)  : ")
    print("Thanks for participation")


if __name__ == "__main__":
    tictactoe_play()
