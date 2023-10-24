'''
Game rules:

Rock beats scissors (breaking it).
Scissors beat paper (cutting it).
Paper beat rock (wrapping it).
The minigame is multiplayer and the computer plays the role of your opponent and chooses a random element from the list of elements
Interaction with the player:

The console is used to interact with the player.
The player can choose one of the three options: rock, paper, or scissors.
The player can choose whether to play again.
The player should be warned if they enter an invalid option.
The player is shown their score at the end of the game.
Validation of user input:

At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.
By the end of each round, the player must answer whether they want to play again or not.
The player must be able to enter a full word or just the first letter of the word.
There can be 5 rounds in total, and the player must be informed of the final score at the end of the game.


'''
import random as rd  # import random module
import sys  # import sys module to exit the program
import time  # import time module to use sleep function to delay the program for a few seconds before exiting the program 
import os  # import os module to clear the screen after each round of the game 
import re  # import re module to use regular expression to validate user input      

# define a function to clear the screen after each round of the game
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# define a function to validate user input

def validate_input(user_input):
    if re.match(r"^[rps]$", user_input):
        return True
    else:
        return False
    
# define a function to play the game

def play_game():     
    # define a list of options
    options = ['rock', 'paper', 'scissors']
    # define a variable to store the number of rounds
    rounds = 0
    # define a variable to store the number of wins
    wins = 0
    # define a variable to store the number of losses
    losses = 0
    # define a variable to store the number of ties
    ties = 0
    # define a variable to store the user input
    user_input = ''
    # define a variable to store the computer input
    computer_input = ''
    # define a variable to store the result of the game
    result = ''
    # define a variable to store the user's choice to play again
    play_again = ''
    
    # display the welcome message
    print('Welcome to the Rock Paper Scissors Game!')
    print('You will play against the computer.')
    print('The computer will randomly choose one of the three options: rock, paper, or scissors.')
    print('You will also choose one of the three options.')
    print('The winner will be determined by the following rules:')
    print('Rock beats scissors (breaking it).')
    print('Scissors beat paper (cutting it).')
    print('Paper beat rock (wrapping it).')
    print('The game will be played in 5 rounds.')
    print('The player with the most wins will be the winner.')
    print('Good luck!')
    
    # prompt the user to enter their name
    user_name = input('Please enter your name: ')
    
    # prompt the user to enter their choice to play the game
    user_choice = input('Would you like to play the game? Please enter yes or no: ')
    
    # validate the user input
    while user_choice.lower() not in ['yes', 'no']:
        print('Invalid input. Please enter yes or no.')
        user_choice = input('Would you like to play the game? Please enter yes or no: ')
    
    # if the user chooses to play the game
    if user_choice.lower() == 'yes':
        # prompt the user to enter their choice
        user_input = input('Please enter your choice: ')
        
        # validate the user input
        while validate_input(user_input) == False:
            print('Invalid input. Please enter r for rock, p for paper or s for scissors.')
            user_input = input('Please enter your choice: ')

        # randomly choose an option from the list of options
        computer_input = rd.choice(options)

        # display the user's choice and the computer's choice
        print(user_name + ': ' + user_input)
        print('Computer: ' + computer_input)

        # determine the result of the game
        if user_input == computer_input[0]:
            result = 'tie'
        elif user_input == 'r' and computer_input[0] == 's':
            result = 'win'
        elif user_input == 'p' and computer_input[0] == 'r':
            result = 'win'
        elif user_input == 's' and computer_input[0] == 'p':
            result = 'win'
        else:
            result = 'loss'

        # display the result of the game

        if result == 'tie':

            print('The game is a tie.')

        elif result == 'win':
                
                print('You win.')

        else:
            print('You lose.')

        # update the number of rounds
        rounds += 1

        # update the number of wins
        if result == 'win':
            wins += 1

        # update the number of losses
        if result == 'loss':
            losses += 1

        # update the number of ties
        if result == 'tie':
            ties += 1

        # prompt the user to enter their choice to play again
        play_again = input('Would you like to play again? Please enter yes or no: ')
        
        # validate the user input
        while play_again.lower() not in ['yes', 'no']:
            print('Invalid input. Please enter yes or no.')
            play_again = input('Would you like to play again? Please enter yes or no: ')

        # if the user chooses to play again

        while play_again.lower() == 'yes':
            # prompt the user to enter their choice
            user_input = input('Please enter your choice: ')
            
            # validate the user input
            while validate_input(user_input) == False:
                print('Invalid input. Please enter r for rock, p for paper or s for scissors.')
                user_input = input('Please enter your choice: ')

            # randomly choose an option from the list of options
            computer_input = rd.choice(options)

            # display the user's choice and the computer's choice
            print(user_name + ': ' + user_input)
            print('Computer: ' + computer_input)

            # determine the result of the game
            if user_input == computer_input[0]:
                result = 'tie'
            elif user_input == 'r' and computer_input[0] == 's':
                result = 'win'
            elif user_input == 'p' and computer_input[0] == 'r':
                result = 'win'
            elif user_input == 's' and computer_input[0] == 'p':
                result = 'win'
            else:
                result = 'loss'

            # display the result of the game

            if result == 'tie':

                print('The game is a tie.')

            elif result == 'win':
                
                print('You win.')

            else:
                print('You lose.')

            # update the number of rounds
            rounds += 1

            # update the number of wins
            if result == 'win':
                wins += 1

            # update the number of losses
            if result == 'loss':
                losses += 1

            # update the number of ties
            if result == 'tie':
                ties += 1

            # prompt the user to enter their choice to play again
            play_again = input('Would you like to play again? Please enter yes or no: ')
            
            # validate the user input
            while play_again.lower() not in ['yes', 'no']:
                print('Invalid input. Please enter yes or no.')
                play_again = input('Would you like to play again? Please enter yes or no: ')

        # display the final score
        print('The final score is:')
        print('Wins: ' + str(wins))
        print('Losses: ' + str(losses))
        print('Ties: ' + str(ties))
        print('Thanks for playing!')

    # if the user chooses not to play the game
    else:
        print('Thanks for playing!')

# call the function to play the game
play_game()

# delay the program for a few seconds before exiting the program
time.sleep(3)

# clear the screen
clear_screen()

# exit the program
sys.exit()
