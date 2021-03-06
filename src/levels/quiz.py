# Copyright (c) 2020 Ayush Gupta, Kartikey Pandey, Pranjal Rastogi
# Author: Kartikey Pandey

import pygame
import cutscene
import random
import platform
import constants as consts
from utils import colors
from utils import level_end_sound as les
from pygame import mixer
import time


class Alien(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(colors.WHITE_COLOR)
        self.image.set_colorkey(colors.WHITE_COLOR)

        if platform.system() == "Windows":
            self.image = pygame.image.load(fr"{consts.ROOT_PATH}\assets\sprites\ALIEN.png").convert_alpha()
        else:
            self.image = pygame.image.load(f"{consts.ROOT_PATH}/assets/sprites/ALIEN.png").convert_alpha()

        self.rect = self.image.get_rect()


class SP(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(colors.WHITE_COLOR)
        self.image.set_colorkey(colors.WHITE_COLOR)
        if platform.system() == "Windows":
            self.image = pygame.image.load(fr"{consts.ROOT_PATH}\assets\sprites\ch.png").convert_alpha()
        else:
            self.image = pygame.image.load(f"{consts.ROOT_PATH}/assets/sprites/ch.png").convert_alpha()
        self.rect = self.image.get_rect()


def update_text(c):
    q = ["I'm sometimes full, but I never overflow.",
         "What planet has the shortest year?",
         "Largest Planet of the Solar System",
         "I am at the centre of the Solar System"]

    text = consts.BUTTON_FONT.render(q[c], True, colors.WHITE_COLOR)
    textRect = text.get_rect()
    textRect.center = (800 // 2, 400 // 2)
    return text, textRect


def answer(st, c):
    ans = ["moon", "mercury", "jupiter", "sun"]

    if st == ans[c]:
        return True
    else:
        return False


def ut(st):
    gg = consts.BUTTON_FONT.render(st, True, (0, 0, 0))
    ggRect = gg.get_rect()
    ggRect.center = (420, 570)
    return gg, ggRect


def quiz_level():
    screen = consts.MAIN_DISPLAY
    background_image = consts.TITLE_SCREEN_BACKGROUND_IMAGE
    all_sprites_list = pygame.sprite.Group()

    AL = Alien(colors.RED, 20, 30)

    AL.rect.x = 130
    AL.rect.y = 350
    all_sprites_list.add(AL)

    S = SP(colors.RED, 20, 30)
    S.rect.x = 200
    S.rect.y = 120
    all_sprites_list.add(S)
    st = ""
    carryOn = True
    c = 0
    counter = 0
    error = False
    while carryOn:
        gg, ggRect = ut(st)
        x, y = pygame.mouse.get_pos()
        text, textRect = update_text(c)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False

            if 550 <= y <= 600:
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_a:
                        st = st + "a"
                    elif event.key == pygame.K_b:
                        st = st + "b"
                    elif event.key == pygame.K_c:
                        st = st + "c"
                    elif event.key == pygame.K_d:
                        st = st + "d"
                    elif event.key == pygame.K_e:
                        st = st + "e"
                    elif event.key == pygame.K_f:
                        st = st + "f"
                    elif event.key == pygame.K_g:
                        st = st + "g"
                    elif event.key == pygame.K_h:
                        st = st + "h"
                    elif event.key == pygame.K_i:
                        st = st + "i"
                    elif event.key == pygame.K_j:
                        st = st + "j"
                    elif event.key == pygame.K_k:
                        st = st + "k"
                    elif event.key == pygame.K_l:
                        st = st + "l"
                    elif event.key == pygame.K_m:
                        st = st + "m"
                    elif event.key == pygame.K_n:
                        st = st + "n"
                    elif event.key == pygame.K_o:
                        st = st + "o"
                    elif event.key == pygame.K_p:
                        st = st + "p"
                    elif event.key == pygame.K_q:
                        st = st + "q"
                    elif event.key == pygame.K_r:
                        st = st + "r"
                    elif event.key == pygame.K_s:
                        st = st + "s"
                    elif event.key == pygame.K_t:
                        st = st + "t"
                    elif event.key == pygame.K_u:
                        st = st + "u"
                    elif event.key == pygame.K_v:
                        st = st + "v"
                    elif event.key == pygame.K_w:
                        st = st + "w"
                    elif event.key == pygame.K_x:
                        st = st + "x"
                    elif event.key == pygame.K_y:
                        st = st + "y"
                    elif event.key == pygame.K_z:
                        st = st + "z"
                    elif event.key == pygame.K_BACKSPACE:
                        st = st[:-1]
                    elif event.key == pygame.K_RETURN:
                        correct = answer(st, c)
                        if correct:
                            c = c + 1
                            st = ""
                            error = False
                        else:
                            c = 0
                            st = ""
                            error = True

                    gg, ggRect = ut(st)

        all_sprites_list.update()
        screen.blit(background_image, [0, 0])

        if not error:
            all_sprites_list.draw(screen)
            screen.blit(text, textRect)
            pygame.draw.rect(screen, colors.WHITE_COLOR, (0, 550, 800, 40))
            screen.blit(gg, ggRect)
        elif error:
            error = consts.TITLE_BOLD.render("WRONG ANSWER, YOU MUST START AGAIN!", True, colors.RED)
            consts.MAIN_DISPLAY.blit(error, (consts.SCREEN_WIDTH/2-error.get_width()/2, 264))
            counter += 1
            if counter > 120:
                return quiz_level()

        if c == 4:
            mixer.music.pause()
            les.play()
            mixer.music.unpause()
            return cutscene.cut_scene(2)
        pygame.display.flip()
        consts.CLOCK.tick(consts.TICK_RATE)

