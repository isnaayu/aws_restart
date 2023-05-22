"""
Working with Loops

A loop is a segment of code that repeats. You will be introduced to two types of loops: the while loop and the for loop.
In this lab, you will:
--Use a while loop
--Use a for loop
"""
import random

# Working with a while loop
# Printing the game rules
print("Welcome to Guess the number!")
print("the rules are simple. I will think of number, and you will try to guess it")

# Importing random and writing a while loop
number = random.randint(1,10)
isGuessRight = False

while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("you guessed {}. That is correct! You win!".format(guess))
    else:
        print("you guessed {}. Sorry, that isn’t it. Try again".format(guess))
        
