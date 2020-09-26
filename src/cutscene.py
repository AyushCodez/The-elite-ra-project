# Copyright (c) 2020 Ayush Gupta, Kartikey Pandey, Pranjal Rastogi
# Author: Pranjal Rastogi

import constants as consts
from utils import colors
import pygame
import time
import levelscreen
import platform

if platform.system() == "Windows":
    BG_IMAGE = pygame.image.load(f"{consts.ROOT_PATH}\\assets\\images\\bg\\cutscene_bg.png")
    crystal = pygame.image.load(f"{consts.ROOT_PATH}\\assets\\images\\textures\\crystal.png")
else:
    BG_IMAGE = pygame.image.load(f"{consts.ROOT_PATH}/assets/images/bg/cutscene_bg.png")
    crystal = pygame.image.load(f"{consts.ROOT_PATH}/assets/images/textures/crystal.png")
crystal = pygame.transform.scale(crystal, (180, 180))

end_pos_1 = (75, 200)
end_pos_2 = (315, 200)
end_pos_3 = (540, 200)


def redraw_crystal(crystals, x, y, lvl):
    global end_pos_3, end_pos_2, end_pos_1

    consts.MAIN_DISPLAY.blit(BG_IMAGE, (0, 0))
    if lvl == 1:
        consts.MAIN_DISPLAY.blit(crystals[0], (x,y))
    if lvl == 2:
        consts.MAIN_DISPLAY.blit(crystals[0], end_pos_1)
        consts.MAIN_DISPLAY.blit(crystals[1], (x, y))
    if lvl == 3:
        consts.MAIN_DISPLAY.blit(crystals[0], end_pos_1)
        consts.MAIN_DISPLAY.blit(crystals[1], end_pos_2)
        consts.MAIN_DISPLAY.blit(crystals[2], (x, y))


def cut_scene(level):
    consts.MAIN_DISPLAY.blit(BG_IMAGE, (0, 0))
    global crystal_1, crystal_2, crystal_3, crystal_1x, crystal_1y, crsytal_2x, crsytal_2y, crystal_3x, crsystal_3y

    if level == 1:
        crystal_1 = crystal
        crystal_1x, crystal_1y = 75, 550
    elif level == 2:
        crystal_1 = crystal
        consts.MAIN_DISPLAY.blit(crystal_1, end_pos_1)
        crystal_2 = crystal
        crystal_2x, crystal_2y = 315, 550
    elif level == 3:
        crystal_1 = crystal
        crystal_2 = crystal
        crystal_3 = crystal
        consts.MAIN_DISPLAY.blit(crystal_1, end_pos_1)
        consts.MAIN_DISPLAY.blit(crystal_2, end_pos_2)
        crystal_3x, crystal_3y = 540, 550

    is_game_over = False
    while not is_game_over:

        # gets all the events occurring every frame, which can be mouse movement, mouse click, etc.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # quit game if QUIT is invoked
                is_game_over = True

        if level == 1:
            if crystal_1y > end_pos_1[1]:
                crystal_1y -= 3
                redraw_crystal([crystal_1], crystal_1x, crystal_1y, level)
            else:
                time.sleep(1)
                return levelscreen.level_chooser_screen()

        elif level == 2:
            if crystal_2y > end_pos_2[1]:
                crystal_2y -= 3
                redraw_crystal([crystal_1, crystal_2], crystal_2x, crystal_2y, level)
            else:
                time.sleep(1)
                return levelscreen.level_chooser_screen()

        elif level == 3:
            if crystal_3y > end_pos_2[1]:
                crystal_3y -= 3
                redraw_crystal([crystal_1, crystal_2, crystal_3], crystal_3x, crystal_3y, level)
            else:
                time.sleep(1)
                return levelscreen.level_chooser_screen()

        # update all the things in game
        pygame.display.update()
        consts.CLOCK.tick(consts.TICK_RATE)
