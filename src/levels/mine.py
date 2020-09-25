import pygame
import random
from pathlib import Path
import time

pygame.init()

clock = pygame.time.Clock()

game_stat = 'win'

screen = pygame.display.set_mode((800, 600))

background_colour = (0, 255, 255)

ROOT_PATH = str(Path(__file__).parents[2])

pygame.display.set_caption('Mine')

playerImg = pygame.image.load(fr'{ROOT_PATH}\assets\sprites\test_Drill.png')
playerX = 370
playerY = 150
playerX_change = 0

meteorImg = []
meteorX = []
meteorY = []
meteorY_change = []
num_of_meteors = 5

time1 = 0

for i in range(num_of_meteors):
    meteorImg.append(pygame.image.load(fr'{ROOT_PATH}\assets\images\textures\nuclear.png'))
    meteorX.append(random.randint(0, 736))
    meteorY.append(random.randint(600, 800))
    meteorY_change.append(-3)

over_font = pygame.font.Font('freesansbold.ttf', 64)
timer = pygame.font.Font('freesansbold.ttf', 12)

digImg = pygame.image.load(fr'{ROOT_PATH}\assets\images\textures\digmark.png')
digX = [playerX]
digY = [i for i in range(playerY - 31, -64, -3)]

crystal = pygame.image.load(fr'{ROOT_PATH}\assets\images\textures\crystal.png')


def is_collision(x1, y1, x2, y2):
    distance = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** (1 / 2)
    if distance < 27:
        return True
    else:
        return False


buttonImg = pygame.image.load(
    fr'{ROOT_PATH}\assets\images\textures\UI\button.png')

button = pygame.Rect((368, 268), (64, 64))

button_stat = 'free1'

game_stat1 = 'lost'


def player(x, y):
    screen.blit(playerImg, (x, y))


def meteor(x, y, _):
    screen.blit(meteorImg[_], (x, y))


def dig(x, y, _):
    screen.blit(digImg, (x, y))


def display_button():
    screen.blit(buttonImg, (368, 268))


def show_crystal(x, y):
    screen.blit(crystal, (x, y))


def game_over_text(text):
    gameover = over_font.render(text, True, (255, 255, 255))
    screen.blit(gameover, (200, 250))


def display_time(timern):
    time_display = timer.render(timern, True, (255, 255, 255))
    screen.blit(time_display, (770, 10))


running = True

while running:

    screen.fill((150, 80, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3

            if event.key == pygame.K_RIGHT:
                playerX_change = 3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
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

                    collision = is_collision(meteorX[i], meteorY[i], playerX, playerY)

                    if collision:
                        playerY = 2000
                        game_stat = 'lost'

                    meteorY[i] += meteorY_change[i]

                    meteor(meteorX[i], meteorY[i], i)

                    if meteorY[i] < -32:
                        meteorX[i] = random.randint(0, 736)
                        meteorY[i] = random.randint(600, 800)
            else:
                if game_stat1 == 'lost':
                    count = 0
                game_stat1 = 'win'

            if playerX > 736:
                playerX = 736
            elif playerX <= 0:
                playerX = 0

        if game_stat == 'lost':
            game_over_text('GAME OVER')
            display_button()
            if pygame.mouse.get_pressed()[0]:
                a = pygame.mouse.get_pos()[0]
                b = pygame.mouse.get_pos()[1]
                if button.collidepoint(a, b):
                    time1 = time.time()
                    for i in range(num_of_meteors):
                        meteorX[i] = random.randint(0, 736)
                        meteorY[i] = random.randint(600, 800)
                    button_stat = 'pressed'
                    game_stat = 'win'
                    game_stat1 = 'lost'
                    playerY = 150
        playerX += playerX_change
        digX.insert(0, playerX)

        digX = digX[:len(digY)]

        for i in range(len(digX)):
            dig(digX[i], digY[i], i)

        if game_stat1 == 'win':
            count += 3
            pygame.draw.line(screen, (255, 255, 255), (0, 600 - count),
                             (800, 600 - count), 5)
            show_crystal(268, 640 - count)
            if 600 - count < 150:
                game_over_text('YOU GOT THE CRYSTAL')
                #END CODE HERE
        player(playerX, playerY)
    pygame.display.update()
    clock.tick(60)
