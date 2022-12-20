#welcome to classic 🪨📰✂️ 

import random
import os
import time

rps_choices = ["rock", "paper", "scissors"]

# def clear():
#     os.system('cls' if os.name == 'nt' else 'clear')
    
def sleep_timer(t):
    time.sleep(t)

while True:
    comp_choice = random.choice(rps_choices)
    user_choice = input('Enter "Rock" or "Paper" or "Scissors" to choose: ')
    user_choice_lower = user_choice.lower()
    
    if user_choice_lower in rps_choices:
            
        def print_selection():
            print("You chose: "+user_choice.capitalize())
            print("💻 chose: "+comp_choice.capitalize())
            print()
        
        def user_win():
            salut_options = ["Congrats", "Congratulations", "Yippee"]
            print(random.choice(salut_options)+"! You win! 🥳 ")
            
        def com_win():
            salut_options = ["Oops", "Sorry", "Hard Luck"]
            print(random.choice(salut_options)+"! 💻 win! 😥 ")
            
        
        if user_choice_lower == comp_choice:
            print_selection()
            print("Game ties!")
            
        elif user_choice_lower == "rock":
            if comp_choice == "paper":
                print_selection()
                com_win()
            elif comp_choice == "scissors":
                print_selection()
                user_win()
                
        elif user_choice_lower == "paper":
            if comp_choice == "rock":
                print_selection()
                user_win()
            elif comp_choice == "scissors":
                print_selection()
                com_win()
                
        elif user_choice_lower == "scissors":
            if comp_choice == "rock":
                print_selection()
                com_win()
            elif comp_choice == "paper":
                print_selection()
                user_win()
                
    else:
        print('You can choose from "Rock", "Paper" or "Scissors" only.')
        sleep_timer(2)
        print()