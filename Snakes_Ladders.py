# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 12:23:06 2018

@author: Sanjana
"""
import random
from PIL import Image
end = 100
def show_board():
    img = Image.open("snakes-ladders.jpg")
    img.show()
    
def check_ladder(points):
    if points == 2:
        print("Ladder!")
        return 23
    elif points == 7:
        print("Ladder")
        return 29
    elif points == 22:
        print("Ladder")
        return 41
    elif points == 28:
        print("Ladder")
        return 77
    elif points == 30:
        print("Ladder")
        return 32
    elif points == 44:
        print("Ladder")
        return 58
    elif points == 54:
        print("Ladder")
        return 69
    elif points == 70:
        print("Ladder")
        return 90
    elif points == 80:
        print("Ladder")
        return 83
    elif points == 87:
        print("Ladder")
        return 93
    else:
        return points
    
def check_snake(points):
    if points == 27:
        print("Snake")
        return 7
    elif points == 35:
        print("Snake")
        return 5
    elif points == 39:
        print("Snake")
        return 3
    elif points == 50:
        print("Snake")
        return 34
    elif points == 59:
        print("Snake")
        return 46
    elif points == 66:
        print("Snake")
        return 24
    elif points == 73:
        print("Snake")
        return 12
    elif points == 76:
        print("Snake")
        return 63
    elif points == 89:
        print("Snake")
        return 67
    elif points == 97:
        print("Snake")
        return 87
    elif points == 99:
        print("Snake")
        return 26
    else:
        return points
    
    
    
def play():
    p1_name = input("Player 1,please enter your name:")
    p2_name = input("Player 2, please enter your name:")
    p1_points = 0
    p2_points = 0
    turn = 0
    while(1):   #Infinite loop which ends only when user enters 0
        c = int(input("Enter 1 to continue playing and 0 to quit : "))
        if c == 0:
            break
        if (turn % 2 == 0): #Player 1 turn
            print(p1_name + ", Its your turn to play")
            dice = random.randint(1,6) #Roll the dice 
            print("You rolled a " + dice)  #Display the dice value
            p1_points+=dice     #Add the dice values to the player 1 points
            p1_points = check_snake(p1_points)  #Check if snake is encountered
            p1_points = check_ladder(p1_points)   #Check if ladder is encountere
            if p1_points == end or p1_points > end :
                print(p1_name + "You win!")
                break
            

        else:
            print(p2_name + ", Its your turn to play")
            dice = random.randint(1,6) #Roll the dice 
            print("You rolled a " + dice)  #Display the dice value
            p2_points+=dice     #Add the dice values to the player 2 points
            p2_points = check_snake(p2_points)  #Check if snake is encountered
            p2_points = check_ladder(p2_points)   #Check if ladder is encountered
            if p2_points == end or p2_points > end :
                print(p2_name + "You win!")
                break
show_board()
play()