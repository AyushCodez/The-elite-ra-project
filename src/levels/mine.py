import pygame
import random

pygame.init()

game_stat = 'win'

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Mine')

background = pygame.image.load(r'C:\Users\Ayush\Documents\GitHub\The-elite-ra-project\assets\images\bg\mine.png')

playerImg = pygame.image.load(r'C:\Users\Ayush\Documents\GitHub\The-elite-ra-project\assets\sprites\test_Drill.png')
playerX = 370
playerY = 30
playerX_change = 0

meteorImg = []
meteorX = []
meteorY = []
meteorY_change = []
num_of_meteors = 5

for i in range(num_of_meteors):
    meteorImg.append(
        pygame.image.load(
            r'C:\Users\Ayush\Documents\GitHub\The-elite-ra-project\assets\images\textures\nuclear.png'))
    meteorX.append(random.randint(0, 736))
    meteorY.append(random.randint(600, 800))
    meteorY_change.append(-3)

over_font = pygame.font.Font('freesansbold.ttf', 64)


def is_collision(x1, y1, x2, y2):
    distance = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** (1 / 2)
    if distance < 27:
        return True
    else:
        return False


buttonImg = pygame.image.load(
    r'C:\Users\Ayush\Documents\GitHub\The-elite-ra-project\assets\images\textures\UI\button.png')

button = pygame.Rect((368, 268), (64, 64))

button_stat = 'free1'


def player(x, y):
    screen.blit(playerImg, (x, y))


def meteor(x, y, _):
    screen.blit(meteorImg[_], (x, y))


def display_button():
    screen.blit(buttonImg, (368, 268))


def game_over_text():
    gameover = over_font.render('GAME OVER', True, (255, 255, 255))
    screen.blit(gameover, (200, 250))


running = True
while running:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

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
                button_stat = 'pressed'

    else:
        if game_stat == 'win':
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

            if playerX > 736:
                playerX = 0
            elif playerX < 0:
                playerX = 736

        if game_stat == 'lost':
            game_over_text()
            display_button()
            if pygame.mouse.get_pressed()[0]:
                a = pygame.mouse.get_pos()[0]
                b = pygame.mouse.get_pos()[1]
                if button.collidepoint(a, b):
                    for i in range(num_of_meteors):
                        meteorX[i] = random.randint(0, 736)
                        meteorY[i] = random.randint(600, 800)
                    button_stat = 'pressed'
                    game_stat = 'win'
                    playerY = 30
        playerX += playerX_change
        player(playerX, playerY)
    pygame.display.update()
