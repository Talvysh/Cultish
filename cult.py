import pygame
from element import Container, Text


class Cult:
    def __init__(self):
        self.name = "Cultish"
        self.followers = 0
        self.crowns = 0

        self.container = Container([50, 200, 100, 100], pygame.Surface((100, 100)))
        self.name_text = Text(self.name, [0, 0], parent=self.container)
        self.followers_text = Text("Followers:", [0, 30], parent=self.container)
        self.crowns_text = Text("Crowns:", [0, 30], parent=self.container)

    def update_stats(self):
        pass


cult = Cult()
