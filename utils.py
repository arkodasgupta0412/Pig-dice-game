from time import sleep
import random

def intro():

    print("Welcome to PIG dice-game")
    print("Play with your friends!")


def rules():

    print("Win by achieving a target score of 50 or outperform your friends!")


def user_input():

    while True:

        number_of_players = input("\nEnter number of players (2-4): ")

        if number_of_players.isdigit():
            
            if 2 <= int(number_of_players) <= 4:
                break

            else:
                print("Must be between 2 and 4")
        
        else:
            print("Invalid! Please try again")

    return number_of_players


def roll():

    min_value = 1
    max_value = 6

    value = random.randint(min_value, max_value)

    return value


def all_scores_equal(seq):

    for val in range(len(seq)):

        if seq[val] != seq[val - 1]:
            return False
        
    return True


