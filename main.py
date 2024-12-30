import pygame

from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color=(0, 0, 0))
        player.update(dt)
        player.draw(screen=screen)
        time_passed = clock.tick(60)
        dt = time_passed / 1000
        pygame.display.flip()


if __name__ == "__main__":
    main()