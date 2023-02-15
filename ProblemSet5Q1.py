# Aryan Gidwani
# November 26, 2021
# ICS3UO - A
# The purpose of this program is for the user to guess the randomly generated
# number from one to ten that the program has in mind. The program will show the
# number of guesses and the number of wins it takes for the user to guess it.
import random
# imports a module that helps with generating a random number
import sys
# imports a module

def stopProgram(userInput):
    global fixedGuesses
    # variable is made global
    if userInput.lower() == "quit":
        print("Thank you for using this program!" + "\n" + "Total Wins: " + str(totalWins))
        # concluding message if they input quit, even if they input Quit
        sys.exit()
        # halts the code from running
    else:
        pass
        # passes the code; nothing happens

def informationUpdater():
    global totalWins
    # makes the variable global
    global totalGuesses
    # makes the variable global
    global fixedGuesses
    # makes the variable global
    totalWins += 1
    # increments the number of wins
    totalGuesses += 1
    # counts the final guess by incrementing the variable
    print("You guessed " + str(chosenNumber) + " , and you are correct! " + "\n" + " Total guesses: " + str(totalGuesses) + "\n" + "The magic number: " + str(randomNumber) + "\n" + "Total wins: " + str(totalWins))
    # informing, concluding message
    fixedGuesses = totalGuesses
    # creates a variable which holds all the guesses made
    totalGuesses = 0
    # sets the number of guesses back to zero
    numberCalculator()
    # calls the function so that the computer chooses a different number for
    # the user to guess

def numberChecker():
    global totalGuesses
    if (chosenNumber == randomNumber):
        informationUpdater()
        # calls the function
    else :
        print("You have chosen " + str(chosenNumber) + " , but that's not the correct number!")
        # incorrect answer message
        totalGuesses += 1
        # increments the number of guesses

def hardNumberChecker():
    global totalGuesses
    if (chosenNumber == randomNumberTwo):
        informationUpdater()
        # calls the function
    else :
        print("You have chosen " + str(chosenNumber) + " , but that's not the correct number!")
        # incorrect answer message
        totalGuesses += 1
        # increments the number of guesses
        
def easyModeGuess():
    global chosenNumber
    # makes the variable global
    chosenNumber = input("Guess the magic number! Enter in an integer from 1 to 10 of your choice. Any decimal number will not be accepted!")
    # asks the user for the number
    stopProgram(chosenNumber)
    # checks to see if the user typed in"quit"

    try:
        chosenNumber = int(chosenNumber)
        # casts to an integer
        if (chosenNumber >= 1) and (chosenNumber <= 10):
            numberChecker()
            # calls the function
            
        else :
            print("Please enter in an integer between 1 and 10!")
            # invalid input message

    except:
        print("Please input a valid value!")
        # invalid input message

def hardModeGuess():
    global chosenNumber
    # makes the variable global
    chosenNumber = input("Guess the magic number! Enter in an integer from 1 to 50 of your choice. Any decimal number will not be accepted!")
    # asks the user for the number
    stopProgram(chosenNumber)
    # checks to see if the user wanted to quit
    try:
        chosenNumber = int(chosenNumber)
        # casts it to an integer
        
        if (chosenNumber >= 1) and (chosenNumber <= 50):
            hardNumberChecker()
            # calls the function
        else :
            print("Please enter in a number between 1 and 50!")
            # invalid input message

    except:
        print("Please input a valid value!")
        # invalid input message

def numberCalculator():
    print("a. Easy" + "\n" + "b. Hard")
    chosenMode = input("Enter in the corresponding letter: ")
    # asks the user if they either want to play easy or hard mode
    stopProgram(chosenMode)
    # sees if the user inputted quit
    global randomNumber
    # makes the variable global
    randomNumber = random.randint(1, 10)
    # initializes the variable to zero
    global randomNumberTwo
    # makes the variable global
    randomNumberTwo = random.randint(1, 50)
    # initializes the variable to zero
    while True:
        
        if chosenMode == "a":
            easyModeGuess()
            # calls the function

        elif chosenMode == "b":
            hardModeGuess()
            # calls the function

        else :
            print("Input one of the letters please!")
            # determines a random number from 1 to 10
            numberCalculator()
            # calls the function again
     
name = input("Hello! What is your name? ")
stopProgram(name)
# asks the user for their name and checks to see if they wanted to quit
print("Hello " + name + "! The purpose of this game is for you, the user, to guess the magic number that the program has in mind! First, type either a or b to choose which level or mode you want to play! Any invalid inputs entered will not count as proper guesses, and you will be told if you have inputted an invalid value! Good luck!")
# introductory message
totalGuesses = 0
# stores the initial value for the total number of guesses
totalWins = 0
# stores the initial value for the total number of wins
numberCalculator()
# calls the method


