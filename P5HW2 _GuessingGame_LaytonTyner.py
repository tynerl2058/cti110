#
#13 Jun 2018
#CTI-110 P5HW2 - Random Number Guessing Game
#Layton Tyner
#

import random

# Declare some variables
# Variable   	Data type   Definition
# random        int         random number generated between 1 - 100
# guess   	int         guess of random number

def main():
# This program generates a random number between 1-100
    displayComments()
    answer = 'y'
    while answer == 'y':
        gameLoop()
        answer = input("Do you want to continue? ")

def gameLoop():
    number = random.randrange(1,100)
    guess = 0
    while guess != number:
        guess = getGuess()
        if guess < number:
            print("You are wrong! Too low; guess again.")
        elif guess > number:
            print("You are wrong! Too high; guess again.")
        else:
            print ("You are correct!!")
        
def displayComments():
    print("This program will generate a random number between 1-100.")
    print("Guess the secret number.")
    print(" ")

#Have contestant guess the secret number
def getGuess():
    guess = int(input("What is your guess (between 1-100)? "))
    return guess



# program start
main()
