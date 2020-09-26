# Copyright (c) 2020 Ayush Gupta, Kartikey Pandey, Pranjal Rastogi
# Author: Pranjal Rastogi

import pygame
import constants as consts
from utils import colors
from utils import widgets
import platform
import sys

text = "You have escaped!"
rendered_text = consts.TITLE_FONT2.render(text, True, colors.WHITE_COLOR)


if platform.system() == "Windows":
    rocket = pygame.image.load(fr'{consts.ROOT_PATH}\assets\sprites\rocket.png')
else:
    rocket = pygame.image.load(fr'{consts.ROOT_PATH}/assets/sprites/rocket.png')
rocket = pygame.transform.scale(rocket, (70, 167))


def redraw(x, y):
    consts.MAIN_DISPLAY.blit(consts.TITLE_SCREEN_BACKGROUND_IMAGE, [0, 0])
    consts.MAIN_DISPLAY.blit(rocket, (x, y))


rocket_x = consts.SCREEN_WIDTH/2-50
rocket_y = 603


def win_animation():
    global rocket_y
    consts.MAIN_DISPLAY.blit(consts.TITLE_SCREEN_BACKGROUND_IMAGE, [0, 0])
    consts.MAIN_DISPLAY.blit(rocket, (rocket_x, rocket_y))

    # the main game loop, looped every frame, looped every clock.tick(TICK_RATE)
    is_game_over = False
    while not is_game_over:
        # gets all the events occurring every frame, which can be mouse movement, mouse click, etc.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # quit game if QUIT is invoked
                is_game_over = True

        if rocket_y > -170:
            rocket_y -= 5
            redraw(rocket_x, rocket_y)
        else:
            return last_screen()

        # update all the things in game
        pygame.display.update()
        consts.CLOCK.tick(consts.TICK_RATE)


def last_screen():

    consts.MAIN_DISPLAY.blit(rendered_text, (140, 100))
    end_btn = widgets.TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 100,
                                                                    (consts.SCREEN_HEIGHT / 2) + 100),
                                 width=200, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.BUTTON_ENABLED,
                                 font=consts.BOLD_FONT, text='Exit')

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
        if end_btn.hovered:
            end_btn.toggle_bg(colors.BUTTON_DISABLED)
            if mouse_down:
                sys.exit()
        else:
            end_btn.toggle_bg(colors.BUTTON_ENABLED)

        # update all the things in game
        pygame.display.update()
        consts.CLOCK.tick(consts.TICK_RATE)
