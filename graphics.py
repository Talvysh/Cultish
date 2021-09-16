import pygame
import pygame.freetype

window = pygame.display.set_mode([640, 360])


class Text:
    def __init__(self, text):
        self.text = text
        self.font = pygame.freetype.Font("Assets/Roboto-Regular.ttf", 16)
        self.size = 12

    def draw(self, surf):
        self.font.render_to(surf, [5, 5], self.text, [255, 255, 255])

    def wrap(self, surf) -> None:
        y = 0
        _text = self.text
        text_rect = self.font.get_rect(self.text, size=self.size)

        while _text:
            i = 0
            while self.font.size(_text[:i])[0] < surf.get_size()[0] and i < len(_text):
                i += 1

            render = self.font.render(_text[:i], True, self.text_color)
            surf.blit(render, [0, y])

            y += Text.font.get_sized_height(self.size)
            _text = _text[i:]
