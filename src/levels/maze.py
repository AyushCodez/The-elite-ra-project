import pygame
import constants as consts
from utils import colors
from utils import widgets
from levels import mine
import levelscreen
import time
import platform
import cutscene

if platform.system() == "Windows":
    maze = pygame.image.load(fr'{consts.ROOT_PATH}\assets\images\textures\maze.png')
    player_image = pygame.image.load(fr'{consts.ROOT_PATH}\assets\sprites\alien.png')
else:
    maze = pygame.image.load(fr'{consts.ROOT_PATH}/assets/images/textures/maze.png')
    player_image = pygame.image.load(fr'{consts.ROOT_PATH}/assets/sprites/alien.png')

maze = pygame.transform.scale(maze, (580, 580))
player_image = pygame.transform.scale(player_image, (26, 34))


def maze_level():
    consts.MAIN_DISPLAY.fill(colors.DARK_GREY_COLOR)
    consts.MAIN_DISPLAY.blit(maze, (110, 10))
    consts.MAIN_DISPLAY.blit(player_image, (0,0))
    is_game_over = False
    st = time.time()
    while not is_game_over:

        # gets all the events occurring every frame, which can be mouse movement, mouse click, etc.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # quit game if QUIT is invoked
                is_game_over = True

            # if event.type == pygame.K_w
        if time.time() - st > 6:  # TODO: remove
            return cutscene.cut_scene()

        # update all the things in game
        pygame.display.update()
        consts.CLOCK.tick(consts.TICK_RATE)
