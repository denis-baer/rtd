"""Module docstring.

"""
    
import random

def create_card_list(number_of_cards):
    """
    Create a List of cards of 4 colors.

    :param number_of_cards: number of cards per color
    :type number_of_cards: int
    :return list cards: fully card deck of number_of_cards * 4 cards
    :rtype: list

    """    
    list_cards = []
    for i in range(1, number_of_cards + 1):
        for j in ["grün", "gelb", "blau", "rot"]:
            list_cards.append((i, j))
    return list_cards


def bigger_card(card_one, card_two, trumpf):
    """
    Compare to cards according to game-rules.

    :param card_one: number and color of a card
    :type card_one: tuple
    :param card_two: number and color of a card
    :type card_two: tuple
    :param trumpf: color of the joker
    :type trumpf: str
    :return: integer indication the winner
    :rtype: int

    """    
    if card_one[1] == trumpf:
        # card one is trumpf
        if card_two[1] == trumpf:
            # card two is trumpf, check bigger number of both cards
            if card_one[0] > card_two[0]:
                return 2
            elif card_one[0] == card_two[0]:
                return 1
            else:
                return 0
        else:
            # card two is no trumpf -> card one is bigger
            return 2
    elif card_two[1] == trumpf:
        # card one no trumpf & card two is trumpf -> card two is bigger
        return 0
    else:
        # no trumpf card - only value
        if card_one[0] > card_two[0]:
            return 2
        elif card_one[0] == card_two[0]:
            return 1
        else:
            return 0


def deal_cards(list_cards, players, number_of_cards):
    """
    Deal cards to th players.

    :param list_cards: List of cards
    :type list_cards: list
    :param players: number of players
    :type players: int
    :param number_of_cards: number of cards each player receives
    :type number_of_cards: int
    :return: list of lists. Each list represent the hand of one player
    :rtype: list
    
    """    
    return_list = []
    for i in range(players):
        return_list.append(list_cards[i * number_of_cards:i * number_of_cards + number_of_cards])
    return return_list


if __name__ == '__main__':
    pass
    #A =create_card_list(3.0)
    #print(A)
