# Copyright (c) 2020 Ayush Gupta, Kartikey Pandey, Pranjal Rastogi
# Author: Pranjal Rastogi

import pygame
from pathlib import Path
import platform

# CWD
SRC_PATH = str(Path(__file__).parents[0])
ROOT_PATH = str(Path(__file__).parents[1])

# game
SCREEN_TITLE = "Cast x Space"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TICK_RATE = 60
CLOCK = pygame.time.Clock()
MAIN_DISPLAY = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
TITLE_SCREEN_BACKGROUND_IMAGE = pygame.image.load(f"{ROOT_PATH}/assets/images/bg/bg.png").convert()

# fonts
if platform.system() == "Windows":
    TITLE_FONT = pygame.font.Font(fr'{ROOT_PATH}\assets\fonts\SourceSansPro-Regular.ttf', 36)
    TITLE_FONT2 = pygame.font.Font(fr'{ROOT_PATH}\assets\fonts\SourceSansPro-Regular.ttf', 64)
    BUTTON_FONT = pygame.font.Font(fr'{ROOT_PATH}\assets\fonts\SourceSansPro-Regular.ttf', 18)
    BOLD_FONT = pygame.font.Font(fr'{ROOT_PATH}\assets\fonts\SourceSansPro-Black.ttf', 24)
else:
    TITLE_FONT = pygame.font.Font(f'{ROOT_PATH}/assets/fonts/SourceSansPro-Regular.ttf', 36)
    TITLE_FONT2 = pygame.font.Font(f'{ROOT_PATH}/assets/fonts/SourceSansPro-Regular.ttf', 64)
    BUTTON_FONT = pygame.font.Font(f'{ROOT_PATH}/assets/fonts/SourceSansPro-Regular.ttf', 18)
    BOLD_FONT = pygame.font.Font(f'{ROOT_PATH}/assets/fonts/SourceSansPro-Black.ttf', 24)


