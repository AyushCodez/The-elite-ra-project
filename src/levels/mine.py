# Copyright (c) 2020 Ayush Gupta, Kartikey Pandey, Pranjal Rastogi
# Author: Ayush Gupta

import pygame
import random
import time
import platform
import constants as consts
from utils import colors
import cutscene

game_stat = 'win'

if platform.system() == "Windows":
    playerImg = pygame.image.load(fr'{consts.ROOT_PATH}\assets\sprites\test_Drill.png')
    digImg = pygame.image.load(fr'{consts.ROOT_PATH}\assets\images\textures\digmark.png')
    crystal = pygame.image.load(fr'{consts.ROOT_PATH}\assets\images\textures\crystal.png')
    buttonImg = pygame.image.load(fr'{consts.ROOT_PATH}\assets\images\textures\UI\button.png')
    single_meteor_img = pygame.image.load(fr'{consts.ROOT_PATH}\assets\images\textures\nuclear.png')
    single_rock_img = pygame.image.load(fr'{consts.ROOT_PATH}\assets\images\textures\stone.png')
    single_oil_img = pygame.image.load(fr'{consts.ROOT_PATH}\assets\images\textures\oil.png')

else:
    playerImg = pygame.image.load(fr'{consts.ROOT_PATH}/assets/sprites/test_Drill.png')
    digImg = pygame.image.load(fr'{consts.ROOT_PATH}/assets/images/textures/digmark.png')
    crystal = pygame.image.load(fr'{consts.ROOT_PATH}/assets/images/textures/crystal.png')
    buttonImg = pygame.image.load(fr'{consts.ROOT_PATH}/assets/images/textures/UI/button.png')
    single_meteor_img = pygame.image.load(fr'{consts.ROOT_PATH}/assets/images/textures/nuclear.png')
    single_rock_img = pygame.image.load(fr'{consts.ROOT_PATH}/assets/images/textures/stone.png')
    single_oil_img = pygame.image.load(fr'{consts.ROOT_PATH}/assets/images/textures/oil.png')

time1 = 0
count = 0
speed = 5
obstacle_num = 4

playerX = 370
playerY = 80
playerX_change = 0

meteorImg = []
meteorX = []
meteorY = []
meteorY_change = []
num_of_meteors = obstacle_num

for i in range(num_of_meteors):
    meteorImg.append(single_meteor_img)
    meteorX.append(random.randint(0, 736))
    meteorY.append(random.randint(600, 1200))
    meteorY_change.append(-speed)

rockImg = []
rockX = []
rockY = []
rockY_change = []
num_of_rocks = obstacle_num

for i in range(num_of_rocks):
    rockImg.append(single_rock_img)
    rockX.append(random.randint(0, 736))
    rockY.append(random.randint(600, 1200))
    rockY_change.append(-speed)

oilImg = []
oilX = []
oilY = []
oilY_change = []
num_of_oils = obstacle_num

for i in range(num_of_oils):
    oilImg.append(single_oil_img)
    oilX.append(random.randint(0, 736))
    oilY.append(random.randint(600, 1200))
    oilY_change.append(-speed)

digX = [playerX]
digY = [i for i in range(playerY + 21, -64, -speed)]


def is_collision(x1, y1, x2, y2):
    distance = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** (1 / 2)
    if distance < 27:
        return True
    else:
        return False

def is_collision_rock(x1, y1, x2, y2):
    distance = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** (1 / 2)
    if distance < 37:
        return True
    else:
        return False


button = pygame.Rect((368, 268), (64, 64))

button_stat = 'free1'

game_stat1 = 'lost'


def player(x, y):
    consts.MAIN_DISPLAY.blit(playerImg, (x, y))


def meteor(x, y, _):
    consts.MAIN_DISPLAY.blit(meteorImg[_], (x, y))


def rock(x, y, _):
    consts.MAIN_DISPLAY.blit(rockImg[_], (x, y))


def oil(x, y, _):
    consts.MAIN_DISPLAY.blit(oilImg[_], (x, y))


def dig(x, y, _):
    consts.MAIN_DISPLAY.blit(digImg, (x, y))


def display_button():
    consts.MAIN_DISPLAY.blit(buttonImg, (368, 268))


def show_crystal(x, y):
    consts.MAIN_DISPLAY.blit(crystal, (x, y))


def game_over_text(text, x, y):
    gameover = consts.TITLE_FONT2.render(text, True, colors.WHITE_COLOR)
    consts.MAIN_DISPLAY.blit(gameover, (x, y))


def display_time(timern):
    time_display = consts.BUTTON_FONT.render(timern, True, colors.WHITE_COLOR)
    consts.MAIN_DISPLAY.blit(time_display, (770, 10))


def mine_level():
    running = True
    global playerX_change, button_stat, time1, game_stat1, game_stat, playerY, playerX, digX, digY, count
    while running:

        consts.MAIN_DISPLAY.fill(colors.DARK_GREY_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if game_stat == 'win':
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        playerX_change = -1

                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        playerX_change = 1
                else:
                    playerX_change = 0

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                    playerX_change = 0

        if button_stat == 'free' or button_stat == 'free1':
            display_button()
            if pygame.mouse.get_pressed()[0]:
                a = pygame.mouse.get_pos()[0]
                b = pygame.mouse.get_pos()[1]
                if button.collidepoint(a, b):
                    time1 = time.time()
                    button_stat = 'pressed'

        else:
            if game_stat == 'win':
                time_taken = round(time.time() - time1, 1)
                display_time(str(time_taken))
                if time_taken < 30:
                    for i in range(num_of_meteors):
                        collision = is_collision(meteorX[i], meteorY[i], playerX + 32, playerY + 62)

                        if collision:
                            playerY = 2000
                            game_stat = 'lost'

                        meteorY[i] += meteorY_change[i]

                        meteor(meteorX[i], meteorY[i], i)

                        if meteorY[i] < -32:
                            meteorX[i] = random.randint(0, 736)
                            meteorY[i] = random.randint(600, 1200)

                    for i in range(num_of_rocks):
                        collision = is_collision_rock(rockX[i] + 32, rockY[i] - 32, playerX + 32, playerY + 62)

                        if collision:
                            playerY = 2000
                            game_stat = 'lost'

                        rockY[i] += rockY_change[i]

                        rock(rockX[i], rockY[i], i)

                        if rockY[i] < -64:
                            rockX[i] = random.randint(0, 736)
                            rockY[i] = random.randint(600, 1200)

                    for i in range(num_of_oils):
                        collision = is_collision(oilX[i], oilY[i], playerX + 32, playerY + 62)

                        if collision:
                            playerY = 2000
                            game_stat = 'lost'

                        oilY[i] += oilY_change[i]

                        oil(oilX[i], oilY[i], i)

                        if oilY[i] < -32:
                            oilX[i] = random.randint(0, 736)
                            oilY[i] = random.randint(600, 1200)
                else:
                    if game_stat1 == 'lost':
                        count = 0
                    game_stat1 = 'win'

                if playerX > 736:
                    playerX = 736
                elif playerX <= 0:
                    playerX = 0

            if game_stat == 'lost':
                game_over_text('GAME OVER', 200, 250)
                display_button()
                if pygame.mouse.get_pressed()[0]:
                    a = pygame.mouse.get_pos()[0]
                    b = pygame.mouse.get_pos()[1]
                    if button.collidepoint(a, b):
                        time1 = time.time()
                        for i in range(num_of_meteors):
                            meteorX[i] = random.randint(0, 736)
                            meteorY[i] = random.randint(600, 1200)
                        for i in range(num_of_rocks):
                            rockX[i] = random.randint(0, 736)
                            rockY[i] = random.randint(600, 1200)

                        for i in range(num_of_oils):
                            oilX[i] = random.randint(0, 736)
                            oilY[i] = random.randint(600, 1200)
                        button_stat = 'pressed'
                        game_stat = 'win'
                        game_stat1 = 'lost'
                        playerY = 80
            playerX += playerX_change
            digX.insert(0, playerX)

            digX = digX[:len(digY)]

            for i in range(len(digX)):
                dig(digX[i], digY[i], i)

            if game_stat1 == 'win':
                count += 3
                pygame.draw.line(consts.MAIN_DISPLAY, (255, 255, 255), (0, 600 - count),
                                 (800, 600 - count), 5)
                show_crystal(368, 640 - count)
                if 600 - count < 150:
                    game_over_text('YOU GOT THE CRYSTAL', 10, 250)
                    return cutscene.cut_scene()
            player(playerX, playerY)
        pygame.display.update()
        consts.CLOCK.tick(60)
