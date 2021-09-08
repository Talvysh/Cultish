import time

import pygame
from GFX import *
import Dialogue

pygame.init()

pygame.display.set_caption("Cultish")


running = True
clock = pygame.time.Clock()
fps_cap = 180
last_time = time.time()
dt = 0

test_text = Text(str(dt), (0, 0, 500, 500))

do_something = pygame.USEREVENT + 0
pygame.time.set_timer(do_something, 1000)

while running:
    dt = time.time() - last_time
    last_time = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == do_something:
            pass

    window.fill((0, 0, 0))
    window.blit(game_surface, ((window.get_width()/2) - (game_surface.get_width()/2), 0))

    test_text.text = str(dt)
    test_text.draw()

    pygame.display.update()
    clock.tick(fps_cap)
