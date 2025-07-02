from random import choice

capital = "Topeka" # This is the capital city of Kansas

bird = "Western Meadowlark" # This is the state bird of Kansas

flower = "Sunflower" # This is the state flower of Kansas

song = "Home on the Range" # This is the state song of Kansas

def randomfunfact():
    """Function to return a random fact about Kansas."""
    funfacts = [
        "kansas is considered the flat, but it does have a mountain.",
        "Wichita is the largest city in the state, but many would guess that it is Kansas City.",
        "A considerable portion of Kansas City is actually in Missouri.",
        "Most Kansas are annoyed by Wizard of Oz references from people outside of Kansas.",
    ]

    index = choice("0123")  # Randomly select an index from 0 to 3
    print(funfacts[int(index)])  # Print the fun fact at the selected index

    # if __name__ == "__main__":  # Check if the module is being run directly
    randomfunfact()