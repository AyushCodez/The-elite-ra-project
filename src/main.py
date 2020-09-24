# Copyright (c) 2020 Ayush Gupta, Kartikey Pandey, Pranjal Rastogi
# main.py
# entry point for the application


import pygame
# initialize pygame
pygame.init()
import sys
from utils import colors
from utils import widgets
import constants as consts


# init window and clock
# TODO: set an icon to the game

clock = pygame.time.Clock()

game_display = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))

game_display.fill(colors.THEME_PRIMARY)
pygame.display.set_caption(consts.SCREEN_TITLE)

# TODO: Load settings option from another file

# this can be static, doesnt need to be remade each time game is run, but, it is remade...
title = consts.TITLE_FONT.render(consts.SCREEN_TITLE, True, colors.THEME_ALT_LIGHT)


def welcome_screen():
    # the main game loop, looped every frame, looped every clock.tick(TICK_RATE)
    is_game_over = False
    mouse_down = False
    while not is_game_over:

        play_button = widgets.TextButton(surface=game_display, pos=((consts.SCREEN_WIDTH / 2) - 100, (consts.SCREEN_HEIGHT / 2) - 20),
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
                return None
        else:
            play_button.toggle_bg(colors.THEME_ALT)

        # update all the things in game
        pygame.display.update()
        clock.tick(consts.TICK_RATE)


if __name__ == '__main__':
    welcome_screen()

pygame.quit()
sys.exit()
