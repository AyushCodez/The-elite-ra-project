# Copyright (c) 2020 Ayush Gupta, Kartikey Pandey, Pranjal Rastogi
# Author: Pranjal Rastogi

import pygame
from levels import mine
from levels import maze
from levels import quiz
import constants as consts
from utils import widgets, colors


def introduce(level):
    consts.MAIN_DISPLAY.blit(consts.TITLE_SCREEN_BACKGROUND_IMAGE, [0, 0])

    text = ""
    controls = ""
    if level == 1:
        text = "The crystal has fallen into a crater!"
        controls = "Get out of the maze in time! WASD to move through the maze"
    if level == 2:
        text = "An Alien has captured your power crystal!"
        controls = "Solve his Riddles! Hover over the white bar and answer him!"
    if level == 3:
        text = "The last crystal is buried under a pile of space rock!"
        controls = "Mine it out! Avoid obstacles, use A or <- to move Left and D or -> to move right"

    rendered_text = consts.TITLE_FONT.render(text, True, colors.WHITE_COLOR)
    rendered_controls = consts.BUTTON_FONT.render(controls, True, colors.WHITE_COLOR)

    consts.MAIN_DISPLAY.blit(rendered_text, (consts.SCREEN_WIDTH/2 - rendered_text.get_width()/2, 150))

    consts.MAIN_DISPLAY.blit(rendered_controls, (consts.SCREEN_WIDTH/2 - rendered_controls.get_width()/2, 200))

    play_button = widgets.TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 100,
                                                                       consts.SCREEN_HEIGHT / 2 + 20),
                                     width=200, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.BUTTON_ENABLED,
                                     font=consts.BOLD_FONT, text='Start Level')

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
            play_button.toggle_bg(colors.BUTTON_DISABLED)
            if mouse_down:
                play_button.toggle_bg(colors.BUTTON_ENABLED)
                if level == 1:
                    return maze.maze_level()
                elif level == 2:
                    return quiz.quiz_level()
                elif level == 3:
                    return mine.mine_level()
        else:
            play_button.toggle_bg(colors.BUTTON_ENABLED)

        # update all the things in game
        pygame.display.update()
        consts.CLOCK.tick(consts.TICK_RATE)
