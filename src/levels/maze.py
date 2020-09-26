import pygame
import constants as consts
from utils import colors
from utils import widgets
from levels import mine
import levelscreen
import time
import platform


def maze_level():
    consts.MAIN_DISPLAY.fill(colors.DARK_GREY_COLOR)
    if platform.system() == "Windows":
        maze = pygame.image.load(fr'{consts.ROOT_PATH}\assets\images\textures\maze.png')
    else:
        maze = pygame.image.load(fr'{consts.ROOT_PATH}/assets/images/textures/maze.png')
    maze = pygame.transform.scale(maze, (500, 500))
    consts.MAIN_DISPLAY.blit(maze, (consts.SCREEN_WIDTH/5+10, 40))

    is_game_over = False

    while not is_game_over:

        # gets all the events occurring every frame, which can be mouse movement, mouse click, etc.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # quit game if QUIT is invoked
                is_game_over = True

        # update all the things in game
        pygame.display.update()
        consts.CLOCK.tick(consts.TICK_RATE)
