import sys
import random
from enum import Enum

def rps(name="PlayerOne"):
    """Function to play Rock, Paper, Scissors."""
    game_count = 0  # Initialize game count
    player_wins = 0  # Initialize player wins
    python_wins = 0  # Initialize Python wins

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins # Use nonlocal to modify outer variables

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input(
            f"\n{name}, enter \n1 for Rock, \n2 for Paper, \n3 for Scissors:\n\n")

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, you must enter 1, 2, or 3.")
            return play_rps()
        
        player = int(playerchoice)

        computerchoice = random.choice("123") # Randomly select a choice for the computer

        computer = int(computerchoice)

        print(f"\n{name}, you chose {str(RPS(player)).replace('RPS.','').title()}.")
        print(f"Python chose {str(RPS(computer)).replace('RPS.','').title()}.\n")
        

        def decide_winner(player, computer):
            """Function to decide the winner of the game."""
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins  # Use nonlocal to modify outer variables

            if player == 1 and computer == 3:
                player_wins += 1
                return f"{name}, you win! 🎉"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"{name}, you win! 🎉"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "You win! 🎉"
            elif player == computer:
                return "😲 Tie game!"
            else:
                python_wins += 1
                return f"🐍 Python wins!\nSorry, {name}..😢"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count  # Use nonlocal to modify outer variable
        game_count += 1  # Increment game count

        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nPython wins: {python_wins}")

        print(f"\nDo you play again {name}?")

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
            print(f"Thanks for playing {name}!\n")
            sys.exit(f"Bye {name}! 👋")  # Exit the game

    return play_rps

if __name__ == "__main__":

    import argparse # parser for command line arguments

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    # add an argument for the name of the person to greet
    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="Name of the person playing the game."
    )

    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()  # Start the game if this script is run directly