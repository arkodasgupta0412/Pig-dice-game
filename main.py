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


    # Game Loop
    for player_idx in range(no_of_players):

        sleep(2)
        print(f"\nPlayer {player_idx + 1}'s turn")

        sleep(1)
        should_roll = input("Would you like to roll? (y/n): ")

        # checking if player wants to roll and initializing current score
        if should_roll.lower() == 'y':
            rolling = True
            current_score = 0

            while rolling:

                sleep(1)
                print("\nDice Rolled!")
                value = roll()

                # checking if value = 1, then the player loses his turn
                if value == 1:
                    sleep(1.5)
                    print(f"Unlucky! You rolled {value}")
                    current_score = 0
                    rolling = False

                # else the player continues rolling
                else:
                    sleep(1.5)
                    print(f"You rolled {value}")
                    current_score = current_score + value
                    scores[player_idx] = current_score

                    if current_score >= target_score:
                        sleep(1)
                        print(f"Congrats! You achieved the target score of {target_score}")
                        rolling = False

                    else:
                        sleep(1)

                        # Ask whether player wants to quit or risk!
                        should_quit = input("Roll Again? (y). Press (q) to quit: ")

                        if should_quit.lower() == 'q':
                            rolling = False
                        

        # inserting score of each player into list to compare them and declare the winner
        sleep(1)
        print(f"Your final score: {current_score}")
        scores[player_idx] = current_score


    # if no player manages to score more than 50
    # then we compare the scores of every player and declare the player with max score as winner

    else:

        if all_scores_equal(scores):
            print("\nIt's a draw among all players. Thanks for playing!")

        else:        
            player_max_score = max(scores)
            idx = scores.index(player_max_score)

            print(f"\nPlayer {idx + 1} won the game with maximum score of {player_max_score}")      


# Driver Code
if __name__ == '__main__':
    main()

