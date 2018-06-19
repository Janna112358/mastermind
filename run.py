#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 22:40:25 2017

@author: Janna112358
Mastermind game
"""
from mastermind import game, display

if __name__ == "__main__":
    print("Welcome to mastermind \n")
    
    # loop allows to keep running mastermind until the user quits
    while True:
        print("Mastermind main menu \n")
        print("Choose one of the following options\n"
              "start: start a game \n"
              "rules: display the rules of mastermind \n"
              "credits: display credits \n"
              "quit: quit mastermind \n")
        quit = False
                
        # loop allows to aks for input until we have valid input for any
        # of the game options or the user quits
        while True:
            ans = input('>> ')
            if ans == "quit" or ans == "q":
                quit = True
                break
            elif ans == "start" or ans == "s":
                game()
                break
            elif ans == "rules" or ans == "r":
                display('rules')
                break
            elif ans == "credits" or ans == "c":
                display('credits')
                break
            else:
                print("sorry, that option is not recognised")
                continue
        if quit:
            break
