import sys
import random
from enum import Enum

def rps():
    """Function to play Rock, Paper, Scissors."""
    game_count = 0  # Initialize game count
    player_wins = 0  # Initialize player wins
    python_wins = 0  # Initialize Python wins

    def play_rps():
        nonlocal player_wins, python_wins # Use nonlocal to modify outer variables

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input(
            "\nEnter \n1 for Rock, \n2 for Paper, \n3 for Scissors, \nor 0 to exit: ")

        if playerchoice not in ["1", "2", "3"]:
            print("You must enter 1, 2, or 3.")
            return play_rps()
        
        player = int(playerchoice)

        computerchoice = random.choice("123") # Randomly select a choice for the computer

        computer = int(computerchoice)

        print(f"\nYou chose {str(RPS(player)).replace('RPS.','').title()}")
        print(f"\nPython chose {str(RPS(computer)).replace('RPS.','').title()}")
        

        def decide_winner(player, computer):
            """Function to decide the winner of the game."""
            nonlocal player_wins, python_wins  # Use nonlocal to modify outer variables

            if player == 1 and computer == 3:
                player_wins += 1
                return "You win! 🎉"
            elif player == 2 and computer == 1:
                player_wins += 1
                return "You win! 🎉"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "You win! 🎉"
            elif player == computer:
                return "😲 Tie game!"
            else:
                python_wins += 1
                return "🐍 Python wins!"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count  # Use nonlocal to modify outer variable
        game_count += 1  # Increment game count

        print(f"\nGame count: {str(game_count)}")
        print(f"\nPlayer wins: {str(player_wins)}")
        print(f"\nPython wins: {str(python_wins)}")

        print("\nPlay again?")

        while True:
            playagain = input("\nY for Yes or \n Q to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_rps()
        else:
            print(f"\n🎉🎉🎉🎉")
            print("Thanks for playing!\n")
            sys.exit("Bye! 👋")  # Exit the game

    return play_rps

rock_paper_scissors = rps()

if __name__ == "__main__":
    rock_paper_scissors()  # Start the game if this script is run directly
