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
            "\nEnter \n1 for Rock, \n2 for Paper, \n3 for Scissors, \nor 0 to exit: "
        )

        if playerchoice not in ["1", "2", "3"]:
            print("You must enter 1, 2, or 3.")
            return play_rps()
        
        player = int(playerchoice)

        computerchoice = random.choice("123") # Randomly select a choice for the computer

        computer = int(computerchoice)

        print(f"\nYou chose {str(RPS(player)).replace('RPS.','').title()}")
        print(f"\nPython chose {str(RPS(computer)).replace('RPS.','').title()}")
