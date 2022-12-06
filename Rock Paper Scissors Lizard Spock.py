# let's play 🪨📰✂️🦎🖖
import random
import os
import time
 
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
 
def rpsls():
     
    global win_loose_matrix
    global game_options
    
    # Game Loop for each game of Rock-Paper-Scissors-Lizard-Spock
    while True:
        clear()
        print("--------------------------------------")
        print("\t\tMenu")
        print("--------------------------------------")
        print("Enter \"Rock\",\"Paper\",\"Scissors\",\"Lizard\",\"Spock\" to play")
        print("Enter \"exit\" to quit")
        print("--------------------------------------")
         
        print()
 
        # Player Input
        inp = input("Enter your move: ")
 
        if inp.lower() == "exit":
            clear()
            break  
        elif inp.lower() == "rock":
            player_move = 0
        elif inp.lower() == "paper":
            player_move = 1    
        elif inp.lower() == "scissors":
            player_move = 2
        elif inp.lower() == "lizard":
            player_move = 3
        elif inp.lower() == "spock":
            player_move = 4
        else:
            clear()
            print('Choose from "Rock","Paper","Scissors","Lizard","Spock" only.')
            time.sleep(2)
            continue
 
        comp_move = random.randint(0, 4)
      
        print("Computer chooses:", game_options[comp_move].upper())
 
        winner = win_loose_matrix[player_move][comp_move]
        print()
        if winner == player_move:
            print("Congratulations! You win! 🥳 ")
        elif winner == comp_move:
            com_win_choices = ["Oops!", "Sorry!"]
            print(random.choice(com_win_choices)+" COMPUTER WIN!😥 ")
        else:
            print("Game Ties!")       
        print()
        time.sleep(3)
        clear()
 

if __name__ == '__main__':
 
    # The mapping between moves and numbers
    game_options = {0:"rock",
                1:"paper",
                2:"scissors",
                3:"lizard",
                4:"Spock"}
 
    # Win-lose matrix
    win_loose_matrix = [[-1, 1, 0, 0, 4],
                   [1, -1, 2, 3, 1],
                   [0, 2, -1, 2, 4],
                   [0, 3, 2, -1, 3],
                   [4, 1, 4, 3, -1]
                   ]
 
    # The GAME LOOP
    while True:
 
        # The Game Menu
        print()
        print("Enter 1 to play Rock-Paper-Scissors-Lizard-Spock")
        print("Enter 2 to quit")
        print()
 
        # Try block to handle the player choice 
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            clear()
            print("You must enter a valid choice")
            time.sleep(1)
            continue
 
    
        # Play the game
        if choice == 1:
            rpsls()
 
        # Quit the game with some random wish
        elif choice == 2:
            quit_wishes = [
                "Bye", "Have a nice day",
                "See you soon", "Will miss you",
                "It was nice playing with you"
                ]
            clear()
            print(random.choice(quit_wishes)+"!")
            break
 
        # Other wrong input
        else:
            clear()
            print("Sorry! You have only 2 options to choose from.")
            time.sleep(1)
 