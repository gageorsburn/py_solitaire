class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def __str__(self):
        return "{} {}".format(self.suit, self.number)

class Suit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return self.name
