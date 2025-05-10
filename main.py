import pygame
from player import Player
from constants import *


def main():
    pygame.init()
    time = pygame.time.Clock()

    dt = 0

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        time_passed = time.tick(60)
        dt = time_passed / 1000


if __name__ == "__main__":
    main()
