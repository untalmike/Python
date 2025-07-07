# suit = "hearts"
# rank = "K"
# value = 10

# print(f"\nYour card is: {rank} of {suit}\n")
# suits.append("snakes") # Add snakes in last position

import random

class Deck:    
    cards = []
    suits = ["spades", "clubs", "hearts", "diamonds"]
    ranks = [
        {"rank": "A", "value": "11"},
        {"rank": "2", "value": "2"},
        {"rank": "3", "value": "3"},
        {"rank": "4", "value": "4"},
        {"rank": "5", "value": "5"},
        {"rank": "6", "value": "6"},
        {"rank": "7", "value": "7"},
        {"rank": "8", "value": "8"},
        {"rank": "9", "value": "9"},
        {"rank": "10", "value": "10"},
        {"rank": "J", "value": "10"},
        {"rank": "Q", "value": "10"},
        {"rank": "K", "value": "10"},
    ] # we create a dictionary
    # ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    for suit in suits:
        for rank in ranks:
            cards.append([suit, rank])

    def shuffle():
        random.shuffle(cards)

    def deal(number):
        cards_dealt = []
        for x in range(number):
            card = cards.pop()
            cards_dealt.append(card)
        return cards_dealt

    # shuffle()
    # card = deal(1)[0]

    # print(card[1]["value"])

    # cards_dealt = deal(2)
    # card = cards_dealt[0]
    # rank = card[1]

    # if rank == "A":
    #     value = 11
    # elif rank == "J" or rank == "Q" or rank == "K":
    #     value = 10
    # else:
    #     value = rank

    # rank_dict = {"rank": rank, "value": value} # Assign a key name when you put the word between quotation marks

    # print(rank_dict["rank"], rank_dict["value"])