# Copyright (c) 2020 Ayush Gupta, Kartikey Pandey, Pranjal Rastogi
# Author: Pranjal Rastogi

import pygame
import constants as consts
from utils import colors
import time
import platform
import cutscene
from utils import level_end_sound as les
from pygame import mixer

# load images
if platform.system() == "Windows":
    maze = pygame.image.load(fr'{consts.ROOT_PATH}\assets\images\textures\maze.png')
    player_image = pygame.image.load(fr'{consts.ROOT_PATH}\assets\sprites\astro.png')
    crystal = pygame.image.load(fr'{consts.ROOT_PATH}\assets\images\textures\crystal.png')
else:
    maze = pygame.image.load(fr'{consts.ROOT_PATH}/assets/images/textures/maze.png')
    player_image = pygame.image.load(fr'{consts.ROOT_PATH}/assets/sprites/astro.png')
    crystal = pygame.image.load(fr'{consts.ROOT_PATH}/assets/images/textures/crystal.png')

# resize images
maze = pygame.transform.scale(maze, (590, 590))
player_image = pygame.transform.scale(player_image, (14, 14))


def redraw(x, y, current_time):
    """function to show player at x position AFTER clearing screen"""
    consts.MAIN_DISPLAY.fill(colors.GREY_COLOR)
    consts.MAIN_DISPLAY.blit(maze, (110, 5))
    consts.MAIN_DISPLAY.blit(crystal, (710, 150))
    consts.MAIN_DISPLAY.blit(player_image, (x, y))
    timer_text = consts.BUTTON_FONT.render(current_time, True, colors.WHITE_COLOR)
    consts.MAIN_DISPLAY.blit(timer_text, (770, 10))


def get_color(x, y):
    """gets the color of coordinate (for collision checking)"""
    return tuple(consts.MAIN_DISPLAY.get_at((x, y)))


TIME_LIMIT = 60
SPEED = 4


def maze_level():
    """run the level"""
    # time limit setup
    st = time.time()

    # set initial coordinates
    player_x, player_y = 84, 290
    x_change, y_change = 0, 0

    # initial setup
    consts.MAIN_DISPLAY.fill(colors.GREY_COLOR)
    consts.MAIN_DISPLAY.blit(maze, (110, 5))
    consts.MAIN_DISPLAY.blit(crystal, (710, 150))

    # main loop
    is_game_over = False
    time_up = False
    c = 0
    while not is_game_over:

        if time.time() - st > TIME_LIMIT:
            # time up
            time_up = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # quit game if QUIT is invoked
                is_game_over = True

            # movement of player
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    y_change -= SPEED
                elif event.key == pygame.K_s:
                    y_change += SPEED
                elif event.key == pygame.K_a:
                    x_change -= SPEED
                elif event.key == pygame.K_d:
                    x_change += SPEED
            # end movement if key up
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    y_change = 0
                elif event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0

        # move player
        player_x += x_change
        player_y += y_change

        # check collisions
        try:
            if get_color(player_x, player_y)[0] < 200:
                # top left corner
                player_x = player_x - x_change
                player_y = player_y - y_change
            if get_color(player_x + 14, player_y + 14)[0] < 200:
                # bottom right corner
                player_x = player_x - x_change
                player_y = player_y - y_change
            if get_color(player_x + 14, player_y)[0] < 200:
                # bottom left corner
                player_x = player_x - x_change
                player_y = player_y - y_change
            if get_color(player_x, player_y + 14)[0] < 200:
                # top right corner
                player_x = player_x - x_change
                player_y = player_y - y_change
        except IndexError:
            # edges of screen
            player_x = player_x - x_change
            player_y = player_y - y_change

        if player_x >= 710:
            # game end, win
            mixer.music.pause()     
            les.play()
            mixer.music.unpause()
            return cutscene.cut_scene(1)

        if time_up:
            consts.MAIN_DISPLAY.fill(colors.GREY_COLOR)
            error = consts.TITLE_BOLD.render("Oh no! you ran out of time! Restarting!", True, colors.RED)
            consts.MAIN_DISPLAY.blit(error, (100, 264))
            c += 1
            if c == 180:
                return maze_level()
        else:
            redraw(player_x, player_y, current_time=str(int(TIME_LIMIT - round(time.time() - st, 0))))

        # update all the things in game
        pygame.display.update()
        consts.CLOCK.tick(consts.TICK_RATE)
