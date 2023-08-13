from utils import *

def main():

    # calling intro and rules for the game
    intro()
    sleep(1)
    rules()

    target_score = 50
    sleep(1)

    no_of_players = int(user_input())
    scores = [0 for _ in range(no_of_players)]
    sleep(1)

    # Game starts!
    print("Let's begin!")


