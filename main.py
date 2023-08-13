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
    print("\nLet's begin!")


    # Game Loop
    for player_idx in range(no_of_players):

        sleep(2)
        print("----------------------------------------------------------------------")
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
                        should_hold = input("Roll Again? (y). Press (h) to hold: ")

                        if should_hold.lower() == 'q':
                            rolling = False

        else:
            rolling = False
            current_score = 0
                        

        # inserting score of each player into list to compare them and declare the winner
        sleep(1)
        print(f"Your final points: {current_score}")
        scores[player_idx] = current_score


    # if no player manages to score more than 50
    # then we compare the scores of every player and declare the player with max score as winner

    else:

        # Displaying final score for all players:
        print("----------------------------------------------------------------------")
        print("\nFINAL POINTS:\n")

        for index in range(len(scores)):
            print(f"Player {index + 1}: {scores[index]} points")

        
        # Displaying winner
        if all_scores_equal(scores):
            print("\nIt's a tie among all players. Thanks for playing!")

        else:        
            player_max_score = max(scores)
            idx = scores.index(player_max_score)

            print(f"\nPlayer {idx + 1} won the game with {player_max_score} points.")      


# Driver Code
if __name__ == '__main__':
    main()

