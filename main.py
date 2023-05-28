from constants import *
from game import Game
import pygame

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Pathfinding")
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    game = Game(win)
    game.run()
