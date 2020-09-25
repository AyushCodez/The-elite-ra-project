# Copyright (c) 2020 Ayush Gupta, Kartikey Pandey, Pranjal Rastogi
# Author: Pranjal Rastogi

import constants as consts
from utils import colors
import pygame
import time
import levelscreen

# TODO: implement

def cut_scene():
    consts.MAIN_DISPLAY.blit(consts.TITLE_SCREEN_BACKGROUND_IMAGE, [0, 0])
    levels_title = consts.TITLE_FONT.render("CUT_SCENE CRYSTAL BEING PLACED!!", True, colors.WHITE_COLOR)
    consts.MAIN_DISPLAY.blit(levels_title, (40, 10))

    # the main game loop, looped every frame, looped every clock.tick(TICK_RATE)
    is_game_over = False
    start_time = time.time()

    while not is_game_over:
        mouse_down = False
        # gets all the events occurring every frame, which can be mouse movement, mouse click, etc.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # quit game if QUIT is invoked
                is_game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True

        if time.time() - start_time > 5:
            return levelscreen.level_chooser_screen()

        # update all the things in game
        pygame.display.update()
        consts.CLOCK.tick(consts.TICK_RATE)
