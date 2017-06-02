# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 22:40:25 2017

@author: jgoldstein

mastermind
"""

import numpy as np
from numpy.random import randint


def get_guess(n):
    while True:
        quit_game = False
        guess = raw_input("enter guess: ")
        if guess == "quit" or guess == "q":
            quit_game = True
            guess = None
            break
        
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
            print "Invalid input, guess needs to be a code of 4 integers"
            continue
    
    return quit_game, guess
    
def get_score(n, code, guess):
    score1 = 0
    score2 = 0
    
    for i in range(n):
        if guess[i] == code[i]:
            score1 += 1
    
    for j in set(guess):
        score2 += min(code.count(j), guess.count(j))        
        
    return score1, score2 - score1


def game():
    print "play a game!"
    print "Type quit anytime to quit the game"
    print
    
    n = 4
    code = ''
    for i in range(n):
        code += str(randint(0, 9))
    
    turn = 1
    while True:
        quit_game, guess = get_guess(n)
        if quit_game:
            break

        score1, score2 = get_score(n, code, guess)
        if score1 == n:
            print "you win! turns: %d"%turn
            print
            return turn
            
        print "turn %d, guess: %s, score: %d %d"%(turn, guess, score1, score2)
        turn += 1
    
