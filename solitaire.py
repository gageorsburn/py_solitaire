from deck import Deck
from view import View

deck = Deck()
view = View()

deck.shuffle()

view.draw_event = deck.draw
deck.draw_event = view.set_draw

view.init()
view.window.mainloop()
