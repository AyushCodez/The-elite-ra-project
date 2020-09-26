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


# set initial coordinates
player_x, player_y = 84, 280
x_change, y_change = 0, 0


def clear_screen_show_player(x, y):
    """function to show player at x position AFTER clearing screen"""
    consts.MAIN_DISPLAY.fill(colors.GREY_COLOR)
    consts.MAIN_DISPLAY.blit(maze, (110, 5))
    consts.MAIN_DISPLAY.blit(crystal, (710, 150))
    consts.MAIN_DISPLAY.blit(player_image, (x, y))


def get_color(x, y):
    """gets the color of coordinate (for collision checking)"""
    return tuple(consts.MAIN_DISPLAY.get_at((x, y)))


def maze_level():
    """run the level"""
    global x_change, y_change, player_x, player_y
    # initial setup
    consts.MAIN_DISPLAY.fill(colors.GREY_COLOR)
    consts.MAIN_DISPLAY.blit(maze, (110, 5))
    consts.MAIN_DISPLAY.blit(crystal, (710, 150))

    # main loop
    is_game_over = False
    while not is_game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # quit game if QUIT is invoked
                is_game_over = True

            # movement of player
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    y_change -= 2
                elif event.key == pygame.K_s:
                    y_change += 2
                elif event.key == pygame.K_a:
                    x_change -= 2
                elif event.key == pygame.K_d:
                    x_change += 2
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
            time.sleep(0.5)
            return cutscene.cut_scene(1)

        clear_screen_show_player(player_x, player_y)
        
        # update all the things in game
        pygame.display.update()
        consts.CLOCK.tick(consts.TICK_RATE)
