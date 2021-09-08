import pygame
pygame.font.init()

window = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
game_surface = pygame.Surface((640, 360))


class GFX:
    draw_queue = []  # Only draw when an element is updated
    target_resolution = (640, 360)
    scale = 1

    def __init__(self, rect, _surface=game_surface) -> None:
        self.rect = pygame.Rect(rect)
        self.parent = None
        self.children = []
        self.show = True
        self.surface = _surface

        self.image = None
        self.fill = pygame.Color(0, 0, 0, 255)
        self.outline = pygame.Color(255, 0, 0, 255)
        self.outline_width = 3
        self.outline_radius = 0

    def set_parent(self, _parent):
        self.parent = _parent
        self.parent.children.append(self)
        self.surface = self.parent.surface

    def draw(self) -> None:
        if self.image is not None:
            self.surface.blit(self.image, self.rect.topleft)

        pygame.draw.rect(
            self.surface,
            self.outline,
            self.rect,
            self.outline_width,
            self.outline_radius
        )

        for c in self.children:
            c.draw()

    @staticmethod
    def set_scale():
        window_aspect = window.get_width() / window.get_height()
        base_aspect = 16/9
        GFX.scale = window_aspect - base_aspect


class Text(GFX):
    font = pygame.font.Font("Assets/Roboto-Regular.ttf", 24)

    def __init__(self, text: str, rect) -> None:
        super().__init__(rect)
        self.text = text
        self.line_height = Text.font.size("Tg")[1]
        self.text_color = pygame.Color(255, 255, 255, 255)

    def draw(self) -> None:
        super().draw()
        self.wrap(self.surface), [20, 20]
    
    def wrap(self, surf: pygame.Surface) -> None:
        y = 0
        _text = self.text
        
        while _text:
            i = 0
            while self.font.size(_text[:i])[0] < surf.get_size()[0] and i < len(_text):
                i += 1
            
            render = self.font.render(_text[:i], True, self.text_color)
            surf.blit(render, [0, y])

            y += self.line_height
            _text = _text[i:]


class Button(GFX):
    def __init__(self, rect: tuple):
        super().__init__(rect)
        self.text = None

    def add_text(self, _text: str):
        self.text = Text(_text, self.rect)
        self.text.set_parent(self)
