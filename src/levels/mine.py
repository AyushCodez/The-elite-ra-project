import pygame
import random
from pathlib import Path
import time
import platform

pygame.init()

clock = pygame.time.Clock()

game_stat = 'win'

screen = pygame.display.set_mode((800, 600))

background_colour = (0, 255, 255)

ROOT_PATH = str(Path(__file__).parents[2])

pygame.display.set_caption('Mine')

if platform.system() == "Windows":
    playerImg = pygame.image.load(fr'{ROOT_PATH}\assets\sprites\test_Drill.png')
    digImg = pygame.image.load(fr'{ROOT_PATH}\assets\images\textures\digmark.png')
    crystal = pygame.image.load(fr'{ROOT_PATH}\assets\images\textures\crystal.png')
    buttonImg = pygame.image.load(fr'{ROOT_PATH}\assets\images\textures\UI\button.png')
    single_meteor_img = pygame.image.load(fr'{ROOT_PATH}\assets\images\textures\nuclear.png')
    single_rock_img = pygame.image.load(fr'{ROOT_PATH}\assets\images\textures\stone.png')

else:
    playerImg = pygame.image.load(fr'{ROOT_PATH}/assets/sprites/test_Drill.png')
    digImg = pygame.image.load(fr'{ROOT_PATH}/assets/images/textures/digmark.png')
    crystal = pygame.image.load(fr'{ROOT_PATH}/assets/images/textures/crystal.png')
    buttonImg = pygame.image.load(fr'{ROOT_PATH}/assets/images/textures/UI/button.png')
    single_meteor_img = pygame.image.load(fr'{ROOT_PATH}/assets/images/textures/nuclear.png')
    single_rock_img = pygame.image.load(fr'{ROOT_PATH}/assets/images/textures/stone.png')

time1 = 0

playerX = 370
playerY = 150
playerX_change = 0

meteorImg = []
meteorX = []
meteorY = []
meteorY_change = []
num_of_meteors = 10

for i in range(num_of_meteors):
    meteorImg.append(single_meteor_img)
    meteorX.append(random.randint(0, 736))
    meteorY.append(random.randint(600, 1200))
    meteorY_change.append(-3)

rockImg = []
rockX = []
rockY = []
rockY_change = []
num_of_rocks = 10

for i in range(num_of_rocks):
    rockImg.append(single_rock_img)
    rockX.append(random.randint(0, 736))
    rockY.append(random.randint(600, 1200))
    rockY_change.append(-3)

over_font = pygame.font.Font('freesansbold.ttf', 64)
timer = pygame.font.Font('freesansbold.ttf', 12)

digX = [playerX]
digY = [i for i in range(playerY - 31, -64, -3)]


def is_collision(x1, y1, x2, y2):
    distance = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** (1 / 2)
    if distance < 27:
        return True
    else:
        return False


button = pygame.Rect((368, 268), (64, 64))

button_stat = 'free1'

game_stat1 = 'lost'


def player(x, y):
    screen.blit(playerImg, (x, y))


def meteor(x, y, _):
    screen.blit(meteorImg[_], (x, y))


def rock(x, y, _):
    screen.blit(rockImg[_], (x, y))


def dig(x, y, _):
    screen.blit(digImg, (x, y))


def display_button():
    screen.blit(buttonImg, (368, 268))


def show_crystal(x, y):
    screen.blit(crystal, (x, y))


def game_over_text(text, x, y):
    gameover = over_font.render(text, True, (255, 255, 255))
    screen.blit(gameover, (x, y))


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
                        meteorY[i] = random.randint(600, 1200)

                for i in range(num_of_rocks):

                    collision = is_collision(rockX[i], rockY[i], playerX, playerY)

                    if collision:
                        playerY = 2000
                        game_stat = 'lost'

                    rockY[i] += rockY_change[i]

                    rock(rockX[i], rockY[i], i)

                    if rockY[i] < -32:
                        rockX[i] = random.randint(0, 736)
                        rockY[i] = random.randint(600, 1200)
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
                game_over_text('YOU GOT THE CRYSTAL', 10, 250)
                # END CODE HERE
        player(playerX, playerY)
    pygame.display.update()
    clock.tick(60)
