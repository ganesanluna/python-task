#!/usr/bin/env python3
"""System module"""
import random
import sys
import copy

NROW = 8
NCOL = 8

TITLE = """
+++++ +++++ *       * +++++ +++++ ++++++ +++++ +++++++ ++++++ +     +
+   + +     +       * +     +   + +      +     +       +    + ++   ++
+   + +     *       + +     +   + +      +     +       +    + + + + +
+++++ +++++  +     +  +++++ +++++ ++++++ +++++ +  ++++ ++++++ +  +  +
++    +       +   +   +     ++         + +     +     + +    + +     +
+ +   +        + +    +     + +        + +     +     + +    + +     +
+  ++ +++++     +     +++++ +  ++ ++++++ +++++ +++++++ +    + +     +
"""


def get_token():
    """ Player get token"""
    while True:
        player_token = input("Do you want to be X or O : ")
        player_token = player_token.upper()
        if player_token == "X":
            computer_token = 'O'
        elif player_token == "O":
            computer_token = 'X'
        else:
            print("Invalid input, Allowed only X and O")
            continue
        return player_token, computer_token


def init_board():
    """ get init board """
    board = []
    for _ in range(NROW):
        board.append([' '] * NCOL)
    board[3][3] = board[4][4] = "X"
    board[3][4] = board[4][3] = "O"
    return board


def display_board(board):
    """ Display the Board, argument based"""
    hr_index = ("   1   2   3   4   5   6   7   8")
    print(hr_index)
    for x_row in range(NROW):
        print(" " + (" ---" * NROW))
        print(x_row + 1, end="")
        for y_col in range(NCOL):
            print(f"| {board[x_row][y_col]} ", end="")
        print("|",x_row + 1)
    print("", (" ---" * (NROW)), "\n" + hr_index)


def score_card(board):
    """ Display of score in each player """
    x_score = 0
    o_score = 0
    for x_row in range(NROW):
        for y_col in range(NCOL):
            if board[x_row][y_col] == 'X':
                x_score += 1
            elif board[x_row][y_col] == 'O':
                o_score += 1
    return {'X': x_score, 'O': o_score}


def get_player_move(board, player_token):
    """ Get player move"""
    while True:
        move = input("Enter your move, 'quit' to end the game "
                     "hints to toggle hints: ").lower()
                     
        if move in ['quit', "hints"]:
            return move
        if len(move) == 2 and move.isdigit() and (0 < int(move[0]) and int(move[1]) <= 8):
            x_val = int(move[0]) - 1
            y_val = int(move[1]) - 1
            if not is_valid_move(board, player_token, x_val, y_val):
                print("Invalid value")
            else:
                break
        else:
            print("That is not a valid move.",
                  "Enter the row (1-8) and",
                  "then the column (1-8).")
            print("For example, 18 will move on the top-right corner.")
    return [x_val, y_val]


def is_valid_move(board, tile, x_start, y_start):
    '''Checking is valid move or not'''
    tiles_to_flip = []
    if board[x_start][y_start] != " " or (7 < x_start < 0 and 7 < y_start < 0):
        return tiles_to_flip

    if tile == 'X':
        other_tile = 'O'
    else:
        other_tile = 'X'

    list_val = [[0, 1], [1, 1], [1, 0], [1, -1],
                [0, -1], [-1, -1], [-1, 0], [-1, 1]]
    for x_dir, y_dir in list_val:
        x_val, y_val = x_start, y_start
        x_val += x_dir
        y_val += y_dir
        while (0 <= x_val <= 7 and 0 <= y_val <= 7 and
               board[x_val][y_val] == other_tile):

            x_val += x_dir
            y_val += y_dir

            if ((0 <= x_val <= 7 and 0 <= y_val <= 7) and
               board[x_val][y_val] == tile):

                while True:
                    x_val -= x_dir
                    y_val -= y_dir
                    if x_val == x_start and y_val == y_start:
                        break
                    tiles_to_flip.append([x_val, y_val])
    return tiles_to_flip


def get_moves(board, token):
    """getting valid moves"""
    valid_moves = []
    for x_axis in range(NROW):
        for y_axis in range(NCOL):
            if is_valid_move(board, token, x_axis, y_axis):
                valid_moves.append([x_axis, y_axis])
    return valid_moves


def make_move(board, token, x_start, y_start):
    """Making move"""
    tokens_to_flip = is_valid_move(board, token, x_start, y_start)

    if not tokens_to_flip:
        return False

    board[x_start][y_start] = token
    for x_axis, y_axis in tokens_to_flip:
        board[x_axis][y_axis] = token
    return True


def get_computer_move(board, computer_token):
    """Getting Computers move"""
    possible_moves = get_moves(board, computer_token)
    best_score = -1

    for x_val, y_val in possible_moves:
        if x_val in [0, NROW - 1] and y_val in [0, NCOL - 1]:
            return [x_val, y_val]
        board_copy = copy.deepcopy(board)
        make_move(board_copy, computer_token, x_val, y_val)
        score = score_card(board_copy)[computer_token]

        if score > best_score:
            best_move = [x_val, y_val]
            best_score = score
    return best_move


def get_hints(board, hints, token):
    """Function for showing hints"""
    if hints is True:
        board_copy = copy.deepcopy(board)
        for row, column in get_moves(board_copy, token):
            board_copy[row][column] = "."
        display_board(board_copy)
    else:
        display_board(board)


def play_game(player_token, computer_token):
    """Playing game"""
    turn = random.choice(["player", "computer"])
    print(f"The {turn} will go first.")
    hints = False
    board = init_board()

    while True:
        player_moves = get_moves(board, player_token)
        computer_moves = get_moves(board, computer_token)

        if not player_moves and not computer_moves:
            return board

        if turn == 'player':
            if player_moves:
                get_hints(board, hints, player_token)
                scores = score_card(board)
                print(f"You: {scores[player_token]} points.",
                      f"Computer: {scores[computer_token]} points.", sep="\n")
                move = get_player_move(board, player_token)
                if move == 'quit':
                    print('Thanks for playing!')
                    sys.exit()
                elif move == "hints":
                    hints = not hints
                    continue
                else:
                    make_move(board, player_token, move[0], move[1])
            turn = 'computer'
        elif turn == 'computer':
            if computer_moves:
                display_board(board)
                scores = score_card(board)
                print(f"You: {scores[player_token]} points.",
                      f"Computer: {scores[computer_token]} points.", sep="\n")
                move = get_computer_move(board, computer_token)
                make_move(board, computer_token, move[0], move[1])
            turn = 'player'


def choices():
    """ Asking user to play again or not"""
    while True:
        choice = input("Do you want to play again Press (y/n): ")
        if choice in ('y', 'Y'):
            print("Playing again")
        elif choice in ('n', 'N'):
            print("Thank you for playing")
        else:
            print("Invalid input")
            continue
        return choice


def main():
    """Main function"""
    print(TITLE)
    choice = 'y'

    while choice == 'y':
        player_token, computer_token = get_token()
        final_board = play_game(player_token, computer_token)
        display_board(final_board)
        scores = score_card(final_board)
        print(f"X scored {scores['X']} points. O scored {scores['O']} points.")

        if scores[player_token] > scores[computer_token]:
            print("You beat the computer by "
                  f"{scores[player_token] - scores[computer_token]}"
                  "points! Congratulations!")
        elif scores[player_token] < scores[computer_token]:
            print("You lost. The computer beat you by "
                  f"{scores[computer_token] - scores[player_token]} points.")
        else:
            print("The game was a tie!")
        choice = choices()


if __name__ == '__main__':
    main()
