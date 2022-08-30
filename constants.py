import platform
from colors import *
import pygame.math
from screeninfo import get_monitors

ratio = 3 / 4
WIDTH, HEIGHT = int(1920 * ratio), int(1080 * ratio)

vec = pygame.math.Vector2
# game
FPS = 60
