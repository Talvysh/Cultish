import pygame
import pygame.freetype
pygame.freetype.init()

window = pygame.display.set_mode((1280, 720), pygame.RESIZABLE | pygame.SCALED, True)
# game_surface = pygame.Surface((640, 360))


class Element:
    instances = []

    def __init__(self, name: str, position: list, surface: pygame.Surface, parent=None) -> None:
        self.name = name
        self.position: list = position
        self.parent = None  # GFX Object
        self.children = []
        self.show = True
        self.surface = surface
        self.image = None

        if parent is not None:
            self.set_parent(parent)

        Element.instances.append(self)

    def set_parent(self, _parent):
        self.parent = _parent
        self.parent.children.append(self)
        self.surface = self.parent.draw_on

    def add_child(self, child):
        if type(child) is Text:
            self.children.append()

    def draw(self) -> None:
        if not self.show:
            return

        if self.image is not None:
            self.surface.blit(self.image, self.position)

        for c in self.children:
            c.draw()

    @classmethod
    def draw_active(cls):
        for i in cls.instances:
            i.draw()


# Grid system?
class GridGUI:
    def __init__(self):
        self.columns = 1
        self.rows = 1
        self.elements = []

    def add_element(self):
        self.elements.append(self)


class Container(Element):
    def __init__(self, rect: list, surface: pygame.Surface):
        super().__init__(rect, surface)

        self.rect = pygame.Rect(rect)

        """
        {
            "name-of-element": ElementObject
        }
        """
        self.elements = {}


class _Text:
    font = pygame.freetype.Font("Assets/Roboto-Regular.ttf")

    def __init__(self, name: str, text: str, x, y, surface: pygame.Surface = window, parent = None, size = 16) -> None:
        self. name = name

    def draw(self):
        pass


class Text(Element):
    font = pygame.freetype.Font("Assets/Roboto-Regular.ttf")

    def __init__(self, text: str, position: list, surface: pygame.Surface, parent=None, size=24) -> None:
        super().__init__(position, parent=parent)

        self.text = text
        self.bounds: pygame.Rect = None
        self.text_color = pygame.Color(255, 255, 255, 255)
        self.size = size

    def __int__(self, text: str, parent: Element):


    def draw(self) -> None:
        super().draw()

        Text.font.render_to(self.surface, self.position, self.text, self.text_color, size=self.size)

    # def wrap(self, surf: pygame.Surface) -> None:
    #     y = 0
    #     _text = self.text
    #     text_rect = Text.font.get_rect(self.text, size=self.size)
    #
    #     while _text:
    #         i = 0
    #         while self.font.size(_text[:i])[0] < surf.get_size()[0] and i < len(_text):
    #             i += 1
    #
    #         render = self.font.render(_text[:i], True, self.text_color)
    #         surf.blit(render, [0, y])
    #
    #         y += Text.font.get_sized_height(self.size)
    #         _text = _text[i:]


class Button:
    pass
