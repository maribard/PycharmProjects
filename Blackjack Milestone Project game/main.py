import random
import numpy
from random import random, shuffle

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10,'Queen': 10, 'King': 10, 'Ace': 11}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)


class Deck:
    def __init__(self):
        self.my_deck = []
        for suit in suits:
            for rank in ranks:
                self.my_deck.append(Card(suit, rank))

    def shuffle1(self):
        numpy.random.shuffle(self.my_deck)

    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.my_deck:
            deck_comp += '\n ' + card.__str__()  # add each Card object's print string
        return 'The deck has:' + deck_comp

    def deal_one(self):
        # Note we remove one card from the list of all_cards
        return self.my_deck.pop()


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)
        if card.rank == 'Ace':
            self.aces += 1

        self.value += card.value

    def adjust_for_ace(self):
        self.value -= 10
        self.aces -+ 1


class Chips:

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet():
    bet_user = int(input("Put a bet: "))
    return bet_user


def hit(deck, hand):
    one_card = deck.deal_one()
    hand.add_card(one_card)


def show_some(player, dealer):
    deck_player = ''
    deck_dealer = ''
    for card in player.cards:
        deck_player += '\n ' + card.__str__()  # add each Card object's print string
    print('The hand player:' + deck_player + "\n" + "Values:  " + str(player.value))

    deck_dealer += '\n ' + dealer.cards[0].__str__()
    print('The 1 card dealer:' + deck_dealer + "\n" + "Values:  " + str(values[dealer.cards[0].rank]))


def show_all(player, dealer):
    deck_player = ''
    deck_dealer = ''
    for card in player.cards:
        deck_player += '\n ' + card.__str__()  # add each Card object's print string
    print('The hand player:' + deck_player + "\n" + "Values:  " + str(player.value))

    for card in dealer.cards:
        deck_dealer += '\n ' + card.__str__()  # add each Card object's print string
    print('The hand dealer:' + deck_dealer + "\n" + "Values:  " + str(dealer.value))


def player_busts():
    print("Player busts")


def player_wins():
    print("Player wins")


def dealer_busts():
    print("Dealer busts")


def dealer_wins():
    print("Dealer wins")


while True:
    print("LETS START! \n \n")
    playing = True

    new_deck = Deck()
    new_deck.shuffle1()

    hand_player = Hand()
    hand_dealer = Hand()

    hit(new_deck, hand_player)
    hit(new_deck, hand_player)

    hit(new_deck, hand_dealer)
    hit(new_deck, hand_dealer)

    player_chips = Chips()
    player_chips.bet = take_bet()

    show_some(hand_player, hand_dealer)

    while playing:
        print("1. Change values Ace from 11 to 1")
        print("2. Take a hit")
        print("3. Stand")

        option = int(input("Player, choose option: " ))
        if option == 1:
            hand_player.adjust_for_ace()
        elif option == 2:
            hit(new_deck, hand_player)
        elif option == 3:
            break

        show_some(hand_player, hand_dealer)

        if hand_player.aces == 0 and hand_player.value > 21:
            #player_busts()
            break



    while hand_dealer.value < 17:
        hit(new_deck, hand_dealer)
        if hand_dealer.value > 21 and hand_dealer.aces == 1:
            hand_dealer.adjust_for_ace()

    show_all( hand_player, hand_dealer )
    if hand_player.value > 21:
        player_busts()
        player_chips.lose_bet()
    elif hand_dealer.value > 21:
        dealer_busts()
        player_chips.win_bet()
    elif hand_dealer.value > hand_player.value:
        dealer_wins()
        player_chips.lose_bet()
    elif hand_dealer.value < hand_player.value:
        player_wins()
        player_chips.win_bet()
    else:
        print("remis")

    print("Your chips: {}".format(player_chips.total))

    go_or_no = input("Do you want one more time? (Y or N): ")
    if go_or_no == 'N':
        break
    else:
        continue






