# Copyright (c) 2020 Ayush Gupta, Kartikey Pandey, Pranjal Rastogi
# Author: Pranjal Rastogi

import pygame
import constants as consts
from utils import colors
from utils import widgets
import introduce_level

isBtn3Disabled = False
isBtn2Disabled = False
isBtn1Disabled = False


def level_chooser_screen():
    global isBtn1Disabled, isBtn2Disabled, isBtn3Disabled

    consts.MAIN_DISPLAY.blit(consts.TITLE_SCREEN_BACKGROUND_IMAGE, [0, 0])
    # Render font
    levels_title = consts.TITLE_FONT.render("CHOOSE A LEVEL", True, colors.WHITE_COLOR)
    consts.MAIN_DISPLAY.blit(levels_title, (40, 10))

    pygame.draw.line(consts.MAIN_DISPLAY, colors.WHITE_COLOR, (5, 10 + levels_title.get_height()),
                     (consts.SCREEN_WIDTH - 10, 10 + levels_title.get_height()), 3)

    lvl1_button = widgets.TextButton(surface=consts.MAIN_DISPLAY, pos=(50, levels_title.get_height() + 60),
                                     width=100, height=100, fg_color=colors.WHITE_COLOR, bg_color=colors.BUTTON_ENABLED,
                                     font=consts.TITLE_FONT, text='1')

    lvl2_button = widgets.TextButton(surface=consts.MAIN_DISPLAY, pos=(300, levels_title.get_height() + 400),
                                     width=100, height=100, fg_color=colors.WHITE_COLOR, bg_color=colors.BUTTON_ENABLED,
                                     font=consts.TITLE_FONT, text='2')

    lvl3_button = widgets.TextButton(surface=consts.MAIN_DISPLAY, pos=(600, levels_title.get_height() + 300),
                                     width=100, height=100, fg_color=colors.WHITE_COLOR, bg_color=colors.BUTTON_ENABLED,
                                     font=consts.TITLE_FONT, text='3')

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

        if not isBtn1Disabled:
            if lvl1_button.hovered:
                lvl1_button.toggle_bg(colors.BUTTON_DISABLED)
                if mouse_down:
                    lvl1_button.toggle_bg(colors.BUTTON_ENABLED)
                    isBtn1Disabled = True
                    return introduce_level.introduce(1)
            else:
                lvl1_button.toggle_bg(colors.BUTTON_ENABLED)
        else:
            # Disabled
            lvl1_button.toggle_bg(colors.GREEN_COLOR)

        if not isBtn2Disabled:
            if lvl2_button.hovered and isBtn1Disabled:
                lvl2_button.toggle_bg(colors.BUTTON_DISABLED)
                if mouse_down:
                    lvl2_button.toggle_bg(colors.BUTTON_ENABLED)
                    isBtn2Disabled = True
                    return introduce_level.introduce(2)
            else:
                lvl2_button.toggle_bg(colors.BUTTON_ENABLED)
            if not isBtn1Disabled:
                lvl2_button.toggle_bg(colors.BUTTON_DISABLED)
        else:
            lvl2_button.toggle_bg(colors.GREEN_COLOR)

        if not isBtn3Disabled:
            if lvl3_button.hovered and isBtn2Disabled:
                lvl3_button.toggle_bg(colors.BUTTON_DISABLED)
                if mouse_down:
                    lvl3_button.toggle_bg(colors.BUTTON_ENABLED)
                    isBtn3Disabled = True
                    return introduce_level.introduce(3)
            else:
                lvl3_button.toggle_bg(colors.BUTTON_ENABLED)
            if not isBtn2Disabled:
                lvl3_button.toggle_bg(colors.BUTTON_DISABLED)
        else:
            lvl3_button.toggle_bg(colors.GREEN_COLOR)

        if isBtn3Disabled:
            print("WIN GAME")

        # update all the things in game
        pygame.display.update()
        consts.CLOCK.tick(consts.TICK_RATE)
