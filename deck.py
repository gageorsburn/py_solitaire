from card import Card
from card import Suit

from random import shuffle

class Deck:
    def __init__(self):
        self.cards = []
        self.temp_cards = []

        self.cycle_count = 0

        suits = [Suit('heart', 'red'),
                 Suit('diamond', 'red'),
                 Suit('club', 'black'),
                 Suit('spade', 'black')]

        number = 1
        suit_counter = 0

        for x in range(1, 53):
            card = Card(suits[suit_counter], number)
            self.cards.append(card)
            number += 1

            if x % 13 == 0:
                number = 1
                suit_counter += 1

    def shuffle(self):
        shuffle(self.cards)

    def play(self):
        """
        Will need more input here. For example,
        we're only going to want to pop the card if
        it can actually be played.
        """

        return self.cards.pop()

    def draw(self):
        try:
            self.temp_cards.insert(0, self.cards.pop())
            self.draw_event(self.cards[-1])
            print(str(self.cycle_count))
        except IndexError:
            self.cycle_count += 1
            self.cards = self.temp_cards
            self.temp_cards = []
            self.draw_event(Card(None, None))

    def take(self):
        """
        We'll use this method in the beginning to take the 
        top cards from the deck for the board.
        """
        pass

    def draw_event(self, card):
        print('Deck:draw_event')
