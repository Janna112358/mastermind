# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 22:40:25 2017

@author: jgoldstein

mastermind
"""

from numpy.random import randint


def rules():
    """
    Display mastermind rules on screen
    """
    rules = open('rules.txt', 'r')
    for r in rules:
        print r


def get_guess(n):
    """
    Allow user to input a guess
    
    Parameters
    ----------
    n: int
        the length of the code in the game
        
    Returns
    -------
    bool
        if True, user indicated to quit the game
    string
        valid length n guess
    """
    # loop allows to aks for input until we have something valid
    while True:
        quit_game = False
        guess = raw_input("guess >> ")
        if guess == "quit" or guess == "q":
            quit_game = True
            guess = None
            break
        
        # check if guess has correct length and consists of integers
        # (by trying to convert the guess to a single integer, which should work
        # for any code of 4 digits)
        if len(guess) == n:
            try:
                int(guess)
                valid_guess = True
                break
            except:
                valid_guess = False
        else:
            valid_guess = False
        if not valid_guess:
            print "Invalid input, guess needs to be a code of %d integers"%n
            # this ensures the loop continues
            continue
    
    return quit_game, guess
    
def get_n():
    """
    Allows user to input a length for the code to use
    
    Returns
    -------
    bool
        if True, user indicated to quit the game
    int
        length of the code to generate
    """
    # loop allows to aks for input until we have something valid
    while True:
        quit_game = False
        n = raw_input("Choose a code length >> ")
        if n == "quit" or n == "q":
            quit_game = True
            n = None
            break
        
        # check wether the input is valid, i.e. an integer
        try:
            n = int(n)
            valid_n = True
            break
        except:
            valid_n = False
        if not valid_n:
            print "Invalid input, needs to be an integer"
            continue
    
    return quit_game, n
    
def get_score(n, code, guess):
    """
    Score a guess given a code and the length
    
    Parameters
    ----------
    n: int
        length of the code
    code: string
        n-digit code
    guess: string
        n-digit guess
        
    Returns
    -------
    int
        number of correct digits in the right place
    int
        number of correct digits in the wrong place
    """
    score1 = 0  # number of correct digits in the right place
    score2 = 0  # number of correct digits in the wrong place
    
    for i in range(n):
        if guess[i] == code[i]:
            score1 += 1
    
    # this allows for correct scoring of doubles
    for j in set(guess):
        score2 += min(code.count(j), guess.count(j))        
        
    return score1, score2 - score1


def game():
    """
    Allow user to play a game
    
    Returns
    -------
    int
        0 if user quit the game
        otherwise the number of turns it took to win
    """
    print "play a game!"
    print "Type quit anytime to quit the game \n"
    
    quit_game, n = get_n()
    if quit_game:
        return 0
    print "You have chosen a code length of %d \n"%n
    
    
    code = ''
    for i in range(n):
        code += str(randint(0, 9))
    
    turn = 1
    while True:
        quit_game, guess = get_guess(n)
        if quit_game:
            break

        score1, score2 = get_score(n, code, guess)
        # win condition is that all of the digits are correct and in the right
        # place, so the first score should be equal to the number of digits
        # in the code
        if score1 == n:
            print "you win! turns: %d"%turn
            print
            return turn
            
        print "turn %d, guess: %s, score: %d %d"%(turn, guess, score1, score2)
        turn += 1
    
