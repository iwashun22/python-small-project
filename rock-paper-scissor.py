#!/usr/bin/python3
from enum import Enum
import random

choose_arr = [
  "ROCK",
  "PAPER",
  "SCISSOR"
]
shorten = {
  "r": choose_arr[0],
  "p": choose_arr[1],
  "s": choose_arr[2]
}

def start_game():
  computer = choose_arr[random.randint(0, 2)]
  user = input("Rock paper scissor!\n(choose {'rock' or 'r'}, {'paper' or 'p'}, or {'scissor' or 's'}): ").upper()
  if user.lower() in shorten.keys():
    user = shorten[user.lower()]
  if user not in choose_arr:
    print("Please type the valid choice.")
    start_game()
    return
  else:
    print("com: " + computer + "\n\t|\n" + "you: " + user)
    # check draw
    if computer == user:
      start_game()
      return
    else:
      check_who_wins(computer, user)

win_pair = {
  "ROCK": "SCISSOR",
  "PAPER": "ROCK",
  "SCISSOR": "PAPER"
}
def check_who_wins(computer, user):
  to_win = win_pair[user]
  if to_win == computer:
    print("You won!")
  else:
    print("You lose!")


start_game()