# Copyright (c) 2020 Ayush Gupta, Kartikey Pandey, Pranjal Rastogi
# Author: Pranjal Rastogi


import pygame
import constants as consts
from utils import colors
from utils import widgets
import levelscreen

text = "Oh no! you have been castaway on an asteroid! The power crystals of your space craft are lost!"
text_2 = "Lets find them and get away from this barren stone!"

rendered_text_1 = consts.BUTTON_FONT.render(text, True, colors.WHITE_COLOR)
rendered_text_2 = consts.BUTTON_FONT.render(text_2, True, colors.WHITE_COLOR)


def intro():

    consts.MAIN_DISPLAY.blit(consts.TITLE_SCREEN_BACKGROUND_IMAGE, [0, 0])
    consts.MAIN_DISPLAY.blit(rendered_text_1, (10, 10))
    consts.MAIN_DISPLAY.blit(rendered_text_2, (20, 10 + rendered_text_1.get_height()))

    cont_button = widgets.TextButton(surface=consts.MAIN_DISPLAY, pos=(200,
                                                                       300),
                                     width=200, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.THEME_ALT,
                                     font=consts.BOLD_FONT, text='Continue')

    # the main game loop, looped every frame, looped every clock.tick(TICK_RATE)
    is_game_over = False
    while not is_game_over:
        mouse_down = False
        # gets all the events occurring every frame, which can be mouse movement, mouse click, etc.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # quit game if QUIT is invoked
                is_game_over = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True

        # button interaction
        if cont_button.hovered:
            cont_button.toggle_bg(colors.THEME_ALT_DARK)
            if mouse_down:
                cont_button.toggle_bg(colors.THEME_ALT)
                return levelscreen.level_chooser_screen()
        else:
            cont_button.toggle_bg(colors.THEME_ALT)

        # update all the things in game
        pygame.display.update()
        consts.CLOCK.tick(consts.TICK_RATE)
