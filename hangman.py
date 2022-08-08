#!/usr/bin/env python3
"""system module"""
import random

HMAN = (
"""
|  |   /\   |\  | |-----  |\  /|   /\   |\  |
|--|  /--\  | \ | | _ __  | \/ |  /--\  | \ |
|  | /    \ |  \| |_ _ _| |    | /    \ |  \|
""",
"""
+----+
     |
     |
     |
     |
   =====
""",
"""
+----+
0    |
     |
     |
     |
   =====
""",
"""
+----+
0    |
|    |
     |
     |
   =====
""",
"""
+----+
0    |
|    |
|    |
     |
   =====
""",
"""
 +----+
 0    |
/|\   |
 |    |
      |
    =====
""",
"""
 +----+
 0    |
/|\   |
 |    |
/ \   |
    =====
"""
)

def main():
     """
     Hangman game
     """
     count = 0
     wlist = [
          "guess",
          "boss",
          "beat",
          "able",
          "eat",
          "agree",
          "apart",
          "blind",
          "ahead",
          "block",
          "apply",
     ]
     choose = random.choice(wlist)
     word = list(choose)
     wrd = word.copy()
     disp = "_" * len(word)
     print(disp)
     disp_list = list(disp)
     i = 1
     print(HMAN[1])
     while i < 7:
          user_input = input("Guess a letter : ")
          flag = 0
          for x in word:
               if user_input == x:
                    print("correct")
                    index = word.index(user_input)
                    disp_list[index] = user_input
                    word[index] = "!"
                    print(" ".join(disp_list))
                    flag = 1
                    break
          if flag == 0:
               print("wrong")
               count += 1
               if count == 1:
                    print(HMAN[2])
               elif count == 2:
                    print(HMAN[3])
               elif count == 3:
                    print(HMAN[4])
               elif count == 4:
                    print(HMAN[5])
               else:
                    print(HMAN[6])
                    break

          elif wrd == disp_list:
               break
               i = i + 1


if __name__ == '__main__':
     print(HMAN[0])
     user_ip = "yes"
     while user_ip == "yes" :
     	  main()
     	  user_ip = input("Do You want to play again (yes or no)  : ")
     print("Thanks for participation")

