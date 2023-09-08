#!/usr/bin/python3
import random

questions = [
  ("What does CPU stands for?", "central processing unit"),
  ("What is the longest river in the world?", "nile river"),
  ("What encryption does https use?", "tls"),
  ("How many bits are in Internet Protocol?", "32")
]

def start_quiz():
  shuffled = questions.copy()
  random.shuffle(shuffled)
  # copied: list = questions.copy()
  score: int = 0
  print(shuffled)
  for [q, a] in shuffled:
    answer = input(q + "\n: ")

    if answer == a:
      print("correct!")
      score += 1
    else:
      print("wrong!")

  print("\n:::::: You got " + str(score) + " out of " + str(len(questions)))


playing = input("Do you wanna start a quiz game? ")

if playing != "yes":
  quit()
else:
  print("OK! Let's start! Please type the answers in lowercase :)")
  start_quiz()