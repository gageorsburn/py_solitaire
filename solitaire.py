from deck import Deck
from view import View
from board import Board

deck = Deck()
board = Board()
view = View()

deck.shuffle()
board.set(deck.take())

view.draw_event = deck.draw
deck.draw_event = view.set_draw

view.init()
view.window.mainloop()
