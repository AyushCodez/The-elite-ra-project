# Copyright (c) 2020 Ayush Gupta, Kartikey Pandey, Pranjal Rastogi
# main.py
# entry point for the application


import pygame
pygame.init()

import sys
from utils import colors
from utils import widgets
import constants as consts
from levels import mine


# init window and clock
# TODO: set an icon to the game

pygame.display.set_caption(consts.SCREEN_TITLE)
# TODO: Bg image
TITLE_SCREEN_BACKGROUND_IMAGE = pygame.image.load(f"{consts.ROOT_PATH}/assets/images/bg/bg.png").convert()
consts.MAIN_DISPLAY.blit(TITLE_SCREEN_BACKGROUND_IMAGE, [0, 0])

# TODO: Load game settings from another file


def starting_screen():

    play_button = widgets.TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 100,
                                                                       (consts.SCREEN_HEIGHT / 2) - 20),
                                     width=200, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.THEME_ALT,
                                     font=consts.BOLD_FONT, text='Play')
    # the main game loop, looped every frame, looped every clock.tick(TICK_RATE)
    is_game_over = False
    while not is_game_over:
        mouse_down = False
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
                return level_chooser_screen()
        else:
            play_button.toggle_bg(colors.THEME_ALT)

        # update all the things in game
        pygame.display.update()
        consts.CLOCK.tick(consts.TICK_RATE)


def level_chooser_screen():
    pygame.display.set_caption(consts.SCREEN_TITLE)
    consts.MAIN_DISPLAY.blit(TITLE_SCREEN_BACKGROUND_IMAGE, [0, 0])
    # Render font
    levels_title = consts.TITLE_FONT.render("LEVELS", True, colors.WHITE_COLOR)
    consts.MAIN_DISPLAY.blit(levels_title, (40, 10))

    pygame.draw.line(consts.MAIN_DISPLAY, colors.WHITE_COLOR, (5, 10 + levels_title.get_height()),
                     (consts.SCREEN_WIDTH-10, 10 + levels_title.get_height()), 3)

    # TODO: blit buttons for levels 1 thru 6
    lvl1_button = widgets.TextButton(surface=consts.MAIN_DISPLAY, pos=(10, levels_title.get_height() + 30),
                                     width=50, height=50, fg_color=colors.WHITE_COLOR, bg_color=colors.THEME_ALT,
                                     font=consts.BOLD_FONT, text='1')
    lvl2_button = widgets.TextButton(surface=consts.MAIN_DISPLAY, pos=(70, levels_title.get_height() + 30),
                                     width=50, height=50, fg_color=colors.WHITE_COLOR, bg_color=colors.THEME_ALT,
                                     font=consts.BOLD_FONT, text='2')
    lvl3_button = widgets.TextButton(surface=consts.MAIN_DISPLAY, pos=(130, levels_title.get_height() + 30),
                                     width=50, height=50, fg_color=colors.WHITE_COLOR, bg_color=colors.THEME_ALT,
                                     font=consts.BOLD_FONT, text='3')
    lvl4_button = widgets.TextButton(surface=consts.MAIN_DISPLAY, pos=(190, levels_title.get_height() + 30),
                                     width=50, height=50, fg_color=colors.WHITE_COLOR, bg_color=colors.THEME_ALT,
                                     font=consts.BOLD_FONT, text='4')
    lvl5_button = widgets.TextButton(surface=consts.MAIN_DISPLAY, pos=(250, levels_title.get_height() + 30),
                                     width=50, height=50, fg_color=colors.WHITE_COLOR, bg_color=colors.THEME_ALT,
                                     font=consts.BOLD_FONT, text='5')
    lvl6_button = widgets.TextButton(surface=consts.MAIN_DISPLAY, pos=(310, levels_title.get_height() + 30),
                                     width=50, height=50, fg_color=colors.WHITE_COLOR, bg_color=colors.THEME_ALT,
                                     font=consts.BOLD_FONT, text='6')

    is_game_over = False
    while not is_game_over:
        mouse_down = False
        # gets all the events occurring every frame, which can be mouse movement, mouse click, etc.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # quit game if QUIT is invoked
                is_game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True

        # TODO: add button handlers
        if lvl1_button.hovered:
            lvl1_button.toggle_bg(colors.THEME_ALT_DARK)
            if mouse_down:
                lvl1_button.toggle_bg(colors.THEME_ALT)
                print("SCAM")
                return mine.mine_level()
        else:
            lvl1_button.toggle_bg(colors.THEME_ALT)

        # update all the things in game
        pygame.display.update()
        consts.CLOCK.tick(consts.TICK_RATE)


if __name__ == '__main__':
    starting_screen()

pygame.quit()
sys.exit()
