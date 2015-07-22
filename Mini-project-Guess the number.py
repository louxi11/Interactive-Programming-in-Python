#! /usr/bin/env python
#coding=utf-8
# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

num_range = 100
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
        
    global secret_number,remain_guess
    
    secret_number = random.randrange(0,num_range)
    remain_guess = int(math.ceil(math.log(num_range,2)))
    
    print "New game has started."    
    print "Guess the secret number between 0 and ",num_range," and remain ",remain_guess," guesses."

    # remove this when you add your code    

    # define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 100
    new_game()
    # remove this when you add your code    
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global remain_guess
    remain_guess -= 1    
    print "Guess was " , guess
    guess = int(guess)
    
    if guess == secret_number :
        print "Correct!"
        new_game()
    elif (guess > secret_number) and (remain_guess > 0) :
        print "Lower.", remain_guess, "guesses remaining."
    elif (guess < secret_number)  and (remain_guess > 0):
        print "Higher.", remain_guess, "guesses remaining."
    else :
        print "Sorry. Starting New Game"
        new_game()
    # remove this when you add your code
    

    
# create frame
f = simplegui.create_frame("Guess the number",200,200)

# register event handlers for control elements and start frame
f.add_button("Range is [0,100)", range100,200)
f.add_button("Range is [0,1000)", range1000,200)
f.add_input("Enter a guess", input_guess,200)
# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
