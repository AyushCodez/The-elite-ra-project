import pygame
import cutscene
import random
import constants as cs
    
class Alien(pygame.sprite.Sprite):   
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.image = pygame.image.load("assets/sprites/ALIEN.png").convert_alpha()
        self.rect = self.image.get_rect()

class SP(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.image = pygame.image.load("ch.png").convert_alpha()
        self.rect = self.image.get_rect()
def UpdateText(c):
    q = ["I'm sometimes full, but I never overflow." , 
         "What planet has the shortest year?" ,
         "Largest Planet of the Solar System",
         "I am at the centre of the Solar System"]
    font = pygame.font.Font('freesansbold.ttf', 16) 
    text = font.render( q[c] , True , WHITE) 
    textRect = text.get_rect()  
    textRect.center = (800 // 2, 400 // 2) 
    return text , textRect 
def Answer(st , c):
    ans = ["moon" , "mercury" ,"jupiter" , "sun"]
    if( st == ans[c]):
        return True
    else : 
        return False
def UT(st):
    font = pygame.font.Font('freesansbold.ttf', 16) 
    gg = font.render( st , True , (0,0,0)) 
    ggRect = gg.get_rect()  
    ggRect.center = (420, 570) 
    return gg , ggRect
def Main():
    size = (cs.SCREEN_WIDTH, cs.SCREEN_HEIGHT)
    screen = cs.MAIN_DISPLAY
    pygame.display.set_caption(sc.SCREEN_TITLE)
    background_image = cs.TITLE_SCREEN_BACKGROUND_IMAGE
    all_sprites_list = pygame.sprite.Group()

    AL = Alien(RED, 20, 30)
    AL.rect.x = 130
    AL.rect.y = 350
    all_sprites_list.add(AL)

    S = SP(RED, 20, 30)
    S.rect.x = 200
    S.rect.y = 120
    all_sprites_list.add(S)
    st = ""
    carryOn = True
    clock=pygame.time.Clock()
    c = 0
    while carryOn:
            gg , ggRect = UT(st)
            x, y = pygame.mouse.get_pos()
            text , textRect = UpdateText(c)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    carryOn=False
                if (y >=550 and y<=600 ) :
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
                            k = Answer(st , c)
                            if k == True : 
                                c = c+1
                                st = ""
                            else :
                                c = 0
                                st = ""
                                Main()
                        gg , ggRect = UT(st)
                        
            all_sprites_list.update()
            screen.blit(background_image, [0, 0])
            all_sprites_list.draw(screen)
            screen.blit(text, textRect) 
            pygame.draw.rect(screen,WHITE,(0,550,800,40))
            screen.blit(gg, ggRect)
            if ( c == 4 ):
                return cutscene.cut_scene()
            pygame.display.flip()
            clock.tick(60)

    pygame.quit()
