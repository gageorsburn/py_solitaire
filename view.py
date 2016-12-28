import tkinter as tk
from functools import partial

from card import Card

class View:
    def __init__(self):
        self.window = tk.Tk()

    def init(self):
        self.init_deck_button()
        self.init_draw_card_label()

    def init_deck_button(self):
        button = tk.Button(self.window, text='deck', command=self.draw_event)
        button.pack()

    def init_draw_card_label(self):
        self.draw_text = tk.StringVar()
        self.draw_text.set('test')
        self.draw_label = tk.Label(self.window, textvariable=self.draw_text)
        self.draw_label.pack()

    def set_draw(self, card):
        self.draw_text.set(str(card))

    def draw_event(self):
        print('View:draw_event')
