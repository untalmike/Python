import sys
import random

def guess_number(name='PlayerOne'):
    game_count = 0 # We declares a variable to count the number of games played
    player_wins = 0 # We decalres the count of player wins

    def player_guess_number():
        nonlocal name
        nonlocal player_wins

        playerchoice = input(f"\n{name}, guess wich number I'm thinking of... 1, 2, or 3.\n\n")

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return player_guess_number() # if the player choice a different option we restart the game
        
        computerchoice = random.choice("123")

        print(f"\n{name}, you chose {playerchoice}.")
        print( f"I was thinking about the number {computerchoice}.\n")

        player = int(playerchoice)

        computer = int(computerchoice)

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins

            if player == computer:
                player_wins += 1
                return f"🎉 {name}, you win!"
            else:
                return f"Sorry, {name}. Better luck next time. 😢"
            
        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nYour winning percentage: {player_wins/game_count:.2%}")
        print(f"\nPlay again, {name}?")

        while True:
            playagain = input("\nY for Yes or \nQ to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return player_guess_number()
        else:
            print(f"\n🎉🎉🎉🎉")
            print(f"Thanks for playing {name}!\n")
            if __name__ == "__main":
                sys.exit(f"Bye {name}! 👋")
            else:
                return
    return player_guess_number

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="Name of the person playing the game."
    )

    args = parser.parse_args()

    guess_my_number = guess_number(args.name)
    guess_my_number()
    