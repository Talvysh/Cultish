import pygame
from graphics import Text


class Game:
    def __init__(self):
        pygame.init()

        self.name = "Cultish"
        pygame.display.set_caption(self.name)

        self._running = True
        self.clock = pygame.time.Clock()
        self.dt = 0.0
        self.fps_cap = 180

        self.screen_width = 640
        self.screen_height = 360
        self.window = pygame.display.set_mode((self.screen_width, self.screen_height))

        self.dt_text = Text(f"DT: {self.dt}")

    def run(self):
        while self._running:
            self.dt = self.clock.get_time()

            self._events()
            self._render()

            self.clock.tick(self.fps_cap)

    def _events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self._quit()

    def _render(self):
        self.window.fill((0, 0, 0))

        self.dt_text.text = f"DT: {self.dt}"
        self.dt_text.draw(self.window)

        pygame.display.flip()

    def _quit(self):
        self._running = False
        # Clean up code here:

