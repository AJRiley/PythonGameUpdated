#!/usr/bin/env python3

import random

number = random.randint(1, 10)
tries = 1
win = False


name = input("Hello, What is your username?")

print("Hello", name + ".", )

question = input("Would you like to play a game? [Y/N] ")
if question == "n":
    print("oh..okay")

if question == "y":
    print("I'm thinking of a number between 1 & 10")
while not win:
    guess = int(input("Have a guess: "))
    tries = tries + 1
    if guess == number:
        win = True
    elif guess < number:
        print("Guess Higher")
    elif guess > number:
        print("Guess Lower")
if win:
    print("Congrats, you guessed correctly. The number was indeed {}".format(number))
    print("it had taken you {} tries".format(tries))
