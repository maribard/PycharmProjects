# We'll use this later
import random


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:

    def __init__(self):
        # Note this only happens once upon creation of a new Deck
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # This assumes the Card class has already been defined!
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        # Note this doesn't return anything
        random.shuffle(self.all_cards)

    def deal_one(self):
        # Note we remove one card from the list of all_cards
        return self.all_cards.pop()


class Player:

    def __init__(self, name):
        self.name = name
        # A new player has no cards
        self.all_cards = []

    def remove_one(self):
        # Note we remove one card from the list of all_cards
        # We state 0 to remove from the "top" of the deck
        # We'll imagine index -1 as the bottom of the deck
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'




player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()

new_deck.shuffle()


for x in range(0, 26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round = 1
while game_on:
    if len(player_one.all_cards) == 0:
        print("Player one has 0 card")
        print("Player two is a winner")
        break

    if len(player_two.all_cards) == 0:
        print("Player two has 0 card")
        print("Player one is a winner")
        break


    print("Round {}".format(round))
    round += 1
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())


    if player_one_cards[-1].value > player_two_cards[-1].value:
        player_one.add_cards(player_one_cards)
        player_one.add_cards(player_two_cards)
       # continue

    elif player_one_cards[-1].value < player_two_cards[-1].value:
       player_two.add_cards(player_one_cards)
       player_two.add_cards(player_two_cards)
       #continue

    else:
        print("WAR")
        war_on = True
        while war_on:
            if len(player_one.all_cards) < 5:
                print("Player one doesn't have enough cards")
                print("Player two is a winner")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("Player two doesn't have enough cards")
                print("Player one is a winner")
                game_on = False
                break

            else:
                for x in range(0, 5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

                if player_one_cards[-1].value > player_two_cards[-1].value:
                    player_one.add_cards(player_one_cards)
                    player_one.add_cards(player_two_cards)
                    print('Player one wins a WAR')
                    war_on = False

                elif player_one_cards[-1].value < player_two_cards[-1].value:
                    player_two.add_cards(player_one_cards)
                    player_two.add_cards(player_two_cards)
                    print('Player two wins a WAR')
                    war_on = False

                else:
                    pass