# Copyright (c) 2020 Ayush Gupta, Kartikey Pandey, Pranjal Rastogi
# Author: Pranjal Rastogi

import pygame

pygame.init()

from utils import colors
from utils import widgets
import constants as consts
import introduce_game
import platform
from pygame import mixer

if platform.system() == 'Windows':
    icon = pygame.image.load(fr'{consts.ROOT_PATH}\assets\images\icon.png')
    bg_music = fr'{consts.ROOT_PATH}\assets\audio\bg\bg_song.mp3'
    logo_path = fr'{consts.ROOT_PATH}\assets\images\LOGO.jpg'

else:
    icon = pygame.image.load(fr'{consts.ROOT_PATH}/assets/images/icon.png')
    bg_music = fr'{consts.ROOT_PATH}/assets/audio/bg/bg_song.mp3'
    logo_path = fr'{consts.ROOT_PATH}/assets/images/LOGO.jpg'

mixer.music.set_volume(0.4)
mixer.music.load(bg_music)
mixer.music.play(-1)

logo_image = pygame.image.load(logo_path).convert_alpha()


# init window and clock
pygame.display.set_icon(icon)

pygame.display.set_caption(consts.SCREEN_TITLE)
consts.MAIN_DISPLAY.blit(consts.TITLE_SCREEN_BACKGROUND_IMAGE, [0, 0])
consts.MAIN_DISPLAY.blit(logo_image, (100, 10))


def starting_screen():
    play_button = widgets.TextButton(surface=consts.MAIN_DISPLAY, pos=((consts.SCREEN_WIDTH / 2) - 100,
                                                                       (consts.SCREEN_HEIGHT / 2) + 100),
                                     width=200, height=40, fg_color=colors.WHITE_COLOR, bg_color=colors.BUTTON_ENABLED,
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
            play_button.toggle_bg(colors.BUTTON_DISABLED)
            if mouse_down:
                play_button.toggle_bg(colors.BUTTON_ENABLED)
                return introduce_game.intro()
        else:
            play_button.toggle_bg(colors.BUTTON_ENABLED)

        # update all the things in game
        pygame.display.update()
        consts.CLOCK.tick(consts.TICK_RATE)

