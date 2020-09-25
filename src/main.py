# Copyright (c) 2020 Ayush Gupta, Kartikey Pandey, Pranjal Rastogi
# main.py
# entry point for the application


import pygame
pygame.init()

import sys
from utils import colors
from utils import widgets
import constants as consts


# init window and clock
# TODO: set an icon to the game

pygame.display.set_caption(consts.SCREEN_TITLE)
TITLE_SCREEN_BACKGROUND_IMAGE = pygame.image.load(f"{consts.ROOT_PATH}/assets/images/bg/bg.png").convert()
consts.MAIN_DISPLAY.blit(TITLE_SCREEN_BACKGROUND_IMAGE, [0, 0])

# TODO: Load game settings from another file

# this can be static, doesnt need to be remade each time game is run, but, it is remade...
title = consts.TITLE_FONT.render(consts.SCREEN_TITLE, True, colors.THEME_ALT_LIGHT)


def starting_screen():
    # the main game loop, looped every frame, looped every clock.tick(TICK_RATE)
    is_game_over = False
    mouse_down = False
    while not is_game_over:

        play_button = widgets.TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 100,
                                                                           (consts.SCREEN_HEIGHT / 2) - 20),
                                         width=200, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.THEME_ALT,
                                         font=consts.BOLD_FONT, text='Play')

        # gets all the events occurring every frame, which can be mouse movement, mouse click, etc.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # quit game if QUIT is invoked
                is_game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True

        # button interaction
        if play_button.hovered:
            play_button.toggle_bg(colors.THEME_ALT_DARK)
            if mouse_down:
                play_button.toggle_bg(colors.THEME_ALT)
                print("TODO")
                return level_chooser_screen()
        else:
            play_button.toggle_bg(colors.THEME_ALT)

        # update all the things in game
        pygame.display.update()
        consts.CLOCK.tick(consts.TICK_RATE)


def level_chooser_screen():
    consts.MAIN_DISPLAY.fill(colors.THEME_ALT)
    pygame.display.set_caption(consts.SCREEN_TITLE)

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


if __name__ == '__main__':
    starting_screen()

pygame.quit()
sys.exit()
