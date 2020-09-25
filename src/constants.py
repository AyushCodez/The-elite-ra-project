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

# fonts
if platform.system() == "Windows":
    TITLE_FONT = pygame.font.Font(fr'{ROOT_PATH}\assets\fonts\SourceSansPro-Regular.ttf', 36)
    BUTTON_FONT = pygame.font.Font(fr'{ROOT_PATH}\assets\fonts\SourceSansPro-Regular.ttf', 18)
    BOLD_FONT = pygame.font.Font(fr'{ROOT_PATH}\assets\fonts\SourceSansPro-Black.ttf', 24)
else:
    TITLE_FONT = pygame.font.Font(f'{ROOT_PATH}/assets/fonts/SourceSansPro-Regular.ttf', 36)
    BUTTON_FONT = pygame.font.Font(f'{ROOT_PATH}/assets/fonts/SourceSansPro-Regular.ttf', 18)
    BOLD_FONT = pygame.font.Font(f'{ROOT_PATH}/assets/fonts/SourceSansPro-Black.ttf', 24)

# game display and clock
CLOCK = pygame.time.Clock()

MAIN_DISPLAY = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
