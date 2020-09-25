import pygame
import constants as consts
from utils import colors
from utils import widgets
from levels import mine
import levelscreen
import time


def maze_level():
    consts.MAIN_DISPLAY.blit(consts.TITLE_SCREEN_BACKGROUND_IMAGE, [0, 0])

    is_game_over = False
    st = time.time()
    while not is_game_over:

        # gets all the events occurring every frame, which can be mouse movement, mouse click, etc.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # quit game if QUIT is invoked
                is_game_over = True

        # TODO: remove (temp)
        if time.time() - st > 3:
            return levelscreen.level_chooser_screen()

        # update all the things in game
        pygame.display.update()
        consts.CLOCK.tick(consts.TICK_RATE)
