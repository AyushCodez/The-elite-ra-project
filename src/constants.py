import pygame
from pathlib import Path

# CWD
SRC_PATH = str(Path(__file__).parents[0])
ROOT_PATH = str(Path(__file__).parents[1])

# game
SCREEN_TITLE = "Cast x Space"
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 650
TICK_RATE = 60

# fonts
TITLE_FONT = pygame.font.Font(f'{ROOT_PATH}/assets/fonts/SourceSansPro-Regular.ttf', 36)
BUTTON_FONT = pygame.font.Font(f'{ROOT_PATH}/assets/fonts/SourceSansPro-Regular.ttf', 18)
BOLD_FONT = pygame.font.Font(f'{ROOT_PATH}/assets/fonts/SourceSansPro-Black.ttf', 24)
