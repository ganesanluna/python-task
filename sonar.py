#!/usr/bin/env python3
""" System module"""
import random
import string
import math
import sys

ROW = 15
COLUMN = 60


TITLE = """
++++++  ++++  +   +  ++++  ++++
+       +  +  ++  +  +  +  +  +
++++++  +  +  + + +  ++++  ++++
     +  +  +  +  ++  +  +  ++
++++++  ++++  +   +  +  +  + ++
"""
print(TITLE)


def instructions():
    """Instructions of sonar game"""
    print(
        "Instructions:\n"
        "You are the captain of the Simon,a treasure-hunting\n"
        "ship. Ur current mission is to use sonar devices to\n"
        "find three sunken treasure chest at the bottom of\n"
        "the ocean. But you only have cheap sonar that finds\n"
        "distance, not direction.\n\n"
        "Enter the coordinates to drop a sonar device. The\n"
        "ocean map will be marked with how far away the \n"
        "nearest chest is, or an X if it is beyond the sonar\n"
        "device's range. For example, the C marks are where\n"
        "chests are. The sonar device shows a 3 because the\n"
        "closest chest is 3 spaces away.\n\n 1 2 3\n"
        "  012345678901234567890123456789012 \n"
        "0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0\n"
        "1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1\n"
        "2 `~`C``3`~~~~`C`~~~~`````~~``~~~`` 2\n"
        "3 ````````~~~`````~~~`~`````~`~``~` 3\n"
        "4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4\n"
        "  012345678901234567890123456789012 \n  1 2 3\n"
        "(The game, the chests arn't visible in the ocean.)\n"
    )
    input("Press any key to continue...\n")
    print(
        "When you drop a sonar device directly on a chest,\n"
        "you retrieve it and the other sonar devices update\n"
        "to show how far away the next nearest chest is. The\n"
        "chests are beyond the range of the sonar device on\n"
        "the left, so it shows an X.\n  1 2 3\n"
        "  012345678901234567890123456789012\n"
        "0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0\n"
        "1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1\n"
        "2 `~`X``7`~~~~`C`~~~~`````~~``~~~`` 2\n"
        "3 ````````~~~`````~~~`~`````~`~``~` 3\n"
        "4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4\n"
        "  012345678901234567890123456789012\n  1 2 3\n"
        "The treasure chests don't move around. Sonar devices\n"
        "can detect treasure chests up to a distance of 9 \n"
        "spaces. Try to collect all 3 chests before running \n"
        "out of sonar devices. Good luck!\n"
    )
    input("Press any key to continue...\n")


def get_new_board():
    """Get new board"""
    board = []
    objects = ["`", "~"]
    for _ in range(ROW):
        board.append(random.choices(objects, k=COLUMN))
    return board


def display_board_index():
    """Display board index value"""
    print("    ", end="")
    for value in range(1, 6):
        print((" " * 9) + str(value), end="")


def display_board(board_list):
    """Display board"""
    display_board_index()
    print("\n   " + string.digits * 6)
    for row_value in range(ROW):
        value = ""
        for column_value in range(COLUMN):
            value = f"{value}{board_list[row_value][column_value]}"
        print(f"{row_value:2} {value} {row_value}")
    print("   " + string.digits * 6)
    display_board_index()
    print("\n")


def get_random_chests(count):
    """make treasure chests"""
    chests = []
    while count > len(chests):
        new_chest = random.choice(range(COLUMN)), random.choice(range(ROW))
        chests.append(new_chest)
    return chests


def is_on_board(x_val, y_val):
    """board limit condition"""
    return 0 <= x_val < 60 and 0 <= y_val < 15


def get_position(previous_value):
    """get the position of from user"""
    while True:
        player_position = input("Where do you want to drop the next sonar"
                                "device? (0-59 0-14) (or type quit)")
        if player_position in ["quit", "q", "Q"]:
            print("Thanks for playing!")
            sys.exit()
        player_position = player_position.split()

        if (len(player_position) == 2
                and player_position[0].isdigit()
                and player_position[1].isdigit()
                and is_on_board(int(player_position[0]),
                                int(player_position[1]))):
            player_position[0] = int(player_position[0])
            player_position[1] = int(player_position[1])
            if ([player_position[0], player_position[1]]
                    in previous_value):
                print("You already selected")
                continue
        else:
            print("Enter a number from 0 to 59, a space, then a number"
                  "from 0 to 14.")
        return [player_position[0], player_position[1]]


def move_the_board(board, treasure_chests, x_val, y_val):
    """Paste the object in to the board"""
    unknown_object = "X"
    smallest_distance = 100
    for c_x, c_y in treasure_chests:
        distance = math.sqrt((c_x - x_val) * (c_x - x_val) +
                             (c_y - y_val) * (c_y - y_val))
        if distance < smallest_distance:
            smallest_distance = distance
        smallest_distance = round(smallest_distance)

    if smallest_distance == 0:
        treasure_chests.remove([x_val, y_val])
        return "You have found a sunken treasure chest!"
    else:

        if smallest_distance < 10:
            board[y_val][x_val] = str(smallest_distance)
            return ("Treasure detected at a distance of"
                    f" {smallest_distance} from the sonar device")
        else:
            board[y_val][x_val] = unknown_object
            return ("Sonar did not detect anything, All treasure"
                    "chests out of range")
    return board, treasure_chests


def sonar():
    """major part of the sonar game"""
    while True:
        turns = 20
        the_board = get_new_board()
        the_chests = get_random_chests(3)
        display_board(the_board)
        previous_moves = []

        while turns > 0:
            print(f"You have {turns} sonar device(s) left.{len(the_chests)}"
                  "treasure chest(s) remaining.")
            x_pos, y_pos = get_position(previous_moves)
            previous_moves.append([x_pos, y_pos])
            move_result = move_the_board(the_board, the_chests, x_pos, y_pos)

            if move_result is False:
                continue
            if move_result == "You have found a sunken treasure chest!":
                for x_val, y_val in previous_moves:
                    move_the_board(the_board, the_chests, x_val, y_val)
            display_board(the_board)
            print(move_result)

            if len(the_chests) == 0:
                print("You have found all the sunken treasure chests!"
                      "Congratulations and good game!")
                break
            turns -= 1

        if turns == 0:
            print("We've run out of sonar devices! Now we have to turn"
                  "the ship around and head")
            print("for home with treasure chests still out there! Game over.")
            print("The remaining chests were here:")
            for x_val, y_val in the_chests:
                print(f"{x_val} {y_val}")


def main():
    """main function of sonar game"""
    user_ip = "yes"
    while user_ip == "yes":
        sonar()
        user_ip = input("Do You want to play again (yes or no)  : ")
    print("Thanks for participation")


if __name__ == "__main__":
    main()
