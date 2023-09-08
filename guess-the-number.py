#!/usr/bin/python3
import random

range_number = input("Type a number for range: ")

if range_number.isdigit():
  range_number = int(range_number)
  if range_number <= 0:
    print("Please type a number larger than 0 next time.")
    quit()
else:
  print("Please type a number next time.")
  quit()

random_number = random.randint(0, range_number)
count_guesses = 0

while True:
  count_guesses += 1
  guess = input("Make a guess: ")
  if guess.isdigit():
    guess = int(guess)
  else:
    print("Please type a number next time.")
    continue

  if guess == random_number:
    print("You got it right!")
    print("You got it in", count_guesses, "guesses")
    break
  else:
    print("You got it wrong!")