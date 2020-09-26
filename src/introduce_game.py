# Copyright (c) 2020 Ayush Gupta, Kartikey Pandey, Pranjal Rastogi
# Author: Pranjal Rastogi


import pygame
import constants as consts
from utils import colors
from utils import widgets
import levelscreen

text = "Oh no! Your spaceship crashed!"
text_2 = "You are castaway on an asteroid!"
text_3 = "The power crystals for your ship are lost!"
text_4 = "Find them and get off the lonely rock!"

rendered_text_1 = consts.TITLE_FONT.render(text, True, colors.WHITE_COLOR)
rendered_text_2 = consts.TITLE_FONT.render(text_2, True, colors.WHITE_COLOR)
rendered_text_3 = consts.BUTTON_FONT.render(text_3, True, colors.WHITE_COLOR)
rendered_text_4 = consts.BUTTON_FONT.render(text_4, True, colors.WHITE_COLOR)


def intro():

    consts.MAIN_DISPLAY.blit(consts.TITLE_SCREEN_BACKGROUND_IMAGE, [0, 0])
    consts.MAIN_DISPLAY.blit(rendered_text_1, (consts.SCREEN_WIDTH/2-rendered_text_1.get_width()/2, 50))
    consts.MAIN_DISPLAY.blit(rendered_text_2, (consts.SCREEN_WIDTH / 2 - rendered_text_2.get_width() / 2, 50
                                               + rendered_text_1.get_height()))
    consts.MAIN_DISPLAY.blit(rendered_text_3, (consts.SCREEN_WIDTH/2-rendered_text_3.get_width()/2, 55
                                               + rendered_text_1.get_height() + rendered_text_2.get_height()))
    consts.MAIN_DISPLAY.blit(rendered_text_4, (consts.SCREEN_WIDTH / 2 - rendered_text_4.get_width() / 2, 55
                                               + rendered_text_2.get_height() + rendered_text_1.get_height() +
                                               rendered_text_3.get_height()))

    cont_button = widgets.TextButton(surface=consts.MAIN_DISPLAY, pos=(consts.SCREEN_WIDTH/2-100, 300),
                                     width=200, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.BUTTON_ENABLED,
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
            cont_button.toggle_bg(colors.BUTTON_DISABLED)
            if mouse_down:
                cont_button.toggle_bg(colors.BUTTON_ENABLED)
                return levelscreen.level_chooser_screen()
        else:
            cont_button.toggle_bg(colors.BUTTON_ENABLED)

        # update all the things in game
        pygame.display.update()
        consts.CLOCK.tick(consts.TICK_RATE)
