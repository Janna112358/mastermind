# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 22:40:25 2017

@author: jgoldstein
Mastermind game
"""

from mastermind import game

if __name__ == "__main__":
    print "Welcome to mastermind \n"
    
    # loop allows to keep running mastermind until the user quits
    while True:
        print "Mastermind main menu"
        print "type start to play a game, type quit to quit \n"
        quit = False
                
        # loop allows to aks for input until we have valid input for any
        # of the game options or the user quits
        while True:
            ans = raw_input('>> ')
            if ans == "quit" or ans == "q":
                quit = True
                break
            elif ans == "start" or ans == "s":
                start_game = True
                break
            else:
                print "sorry, that option is not recognised"
                continue
        if quit:
            break
    
        if start_game:
            game()