import math

import pygame
import random
import os


#setup folder assests
game_folder = os.path.dirname(__file__)
mimmikyu_folder = os.path.join(game_folder, "imgs")
snd_folder = os.path.join(game_folder,"snds")


HEIGHT = 360
WIDTH = 480
FPS = 30
title = "Template"
mouse_buttn_held=False

# Define Colors (r, g, b)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
ORANGE = (255, 127, 0)
MAGENTA = (255, 0, 127)
PURPLE = (127, 0, 255)

# game classes
class NPC(pygame.sprite.Sprite):
    def __init__(self):
        super(NPC, self).__init__()
        self.image = pygame.Surface((25,25))
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.ang = 0
        self.speedx = 5
        self.speedy = 5
        self.do_Circle = False

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right >= WIDTH-1 or self.rect.left <= 1:
            self.speedx = self.speedx*-1
        if self.rect.top <=1 or self.rect.bottom >= HEIGHT-1:
            self.speedy = self.speedy*-1


        # movement
        # self.rect.x += self.speedx
        # self.rect.y += self.speedy
        #
        # if self.rect.right >= WIDTH-1:
        #     self.speedx = 0
        #     self.speedy = -5
        # if self.rect.top <= 1:
        #     self.speedx = -5
        #     self.speedy = 0
        # if self.rect.left <= 1:
        #     self.speedx = 0
        #     self.speedy = 5
        # if self.rect.bottom >= HEIGHT-1:
        #     self.speedx = 5
        #     self.speedy = 0


        # # enemy movement
        # if self.rect.centerx >= WIDTH/2 and self.ang < 360:
        #     self.do_Circle = True
        #     if self.do_Circle:
        #         if self.ang < 360:
        #             rad = self.ang * math.pi / 180
        #             self.rect.centery += -math.sin(rad) * 50 + self.rect.centery
        #             self.rect.centerx += math.cos(rad) * 50 + self.rect.centerx
        #             self.ang += 20
        #         else:
        #             self.do_Circle = False
        #     self.speedx = 5
        #     self.speedy = -5
        # if self.rect.bottomleft[0]>WIDTH and self.rect.bottomleft[1]<=0:
        #     self.rect.bottomright = (0,0)
        #     self.speedx = 5
        #     self.speedy = 5
        #     self.ang = 0





class Player (pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.image = player_img
        #self.image = pygame.Surface((50,50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speedx = 0
        self.speedy = 0
        self.keypressed = False

    def update(self):
        if mouse_buttn_held:
            mousex,mousey = pygame.mouse.get_pos()
            # self.rect.center = (mousex,mousey)






        # self.speedx = 0
        # self.speedy = 0
        # keystate = pygame.key.get_pressed()
        # if keystate[pygame.K_LEFT] or keystate[pygame.K_a]:
        #     self.speedx = -5
        # if keystate[pygame.K_RIGHT] or keystate[pygame.K_d]:
        #     self.speedx = 5
        # if keystate[pygame.K_UP] or keystate[pygame.K_w]:
        #     self.speedy = -5
        # if keystate[pygame.K_DOWN] or keystate[pygame.K_s]:
        #     self.speedy = 5
        #
        self.rect.x += self.speedx
        self.rect.y += self.speedy


        # Grid movement functions
        # keystate = pygame.key.get_pressed()
        # if (keystate[pygame.K_LEFT] or keystate[pygame.K_a] ) and self.keypressed == False:
        #     self.keypressed = True
        #     self.rect.centerx += -50
        # if keystate[pygame.K_RIGHT] or keystate[pygame.K_d]:
        #     self.rect.centerx += 50
        # if keystate[pygame.UP] or keystate[pygame.K_w]:
        #     self.rect.centery += -50
        # if keystate[pygame.K_DOWN] or keystate[pygame.K_s]:
        #     self.rect.centery += 50
        # keyrelease = pygame.KEYUP
        # if keyrelease==pygame.K_LEFT:
        #     self.keypressed = False



        if self.rect.left <=0:
            self.rect.left = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
    def toggle_pressed(self):
        self.keypressed = False

def spw_new_player(x,y):
    newplayer = Player()
    newplayer.rect.center = (x,y)
    newplayer.speedx = random.randint(-10,10)
    newplayer.speedy = random.randint(-10, 10)
    all_sprites.add(newplayer)
    players_group.add(newplayer)


# initialize pygame and create window
pygame.init()
pygame.mixer.init()

#load in game imgs
player_img = pygame.image.load(os.path.join(mimmikyu_folder,"img.png")).convert()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(title)

clock = pygame.time.Clock()

# sprite groups
all_sprites = pygame.sprite.Group()
players_group = pygame.sprite.Group()
mobs_group = pygame.sprite.Group()

# create game objects
npc = NPC()
player = Player()

#add objects to sprite groups
all_sprites.add(npc)
mobs_group.add(npc)
all_sprites.add(player)
players_group.add(player)


# game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # input section
    ######################################################################
    mousex,mousey = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and player.rect.collidepoint(pygame.mouse.get_pos()):
            mouse_buttn_held = True
            print("clicked on player")

        if event.type == pygame.MOUSEBUTTONUP and mouse_buttn_held == True:
            mouse_buttn_held = False
            spw_new_player(mousex, mousey)

    # process input
    # for event in pygame.event.get():
    #     if event.type == pygame.KEYDOWN:
    #         if event.key == pygame.K_LEFT or event.key == pygame.K_a:
    #             player.rect.x += -50
    #     if event.type == pygame.KEYUP:
    #         if event.key == pygame.K_LEFT or event.key == pygame.K_a:
    #             player.speedx=0
    #     if event.type == pygame.KEYDOWN:
    #         if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
    #             player.rect.x += 50
    #     if event.type == pygame.KEYUP:
    #         if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
    #             player.speedx=0
    #     if event.type == pygame.KEYDOWN:
    #         if event.key == pygame.K_DOWN or event.key == pygame.K_s:
    #             player.rect.y += 50
    #     if event.type == pygame.KEYUP:
    #         if event.key == pygame.K_DOWN or event.key == pygame.K_s:
    #             player.speedx=0
    #     if event.type == pygame.KEYDOWN:
    #         if event.key == pygame.K_UP or event.key == pygame.K_w:
    #             player.rect.y += -50
    #     if event.type == pygame.KEYUP:
    #         if event.key == pygame.K_UP or event.key == pygame.K_w:
    #             player.speedx=0
    #     if event.type == pygame.KEYDOWN:
    #         if event.key == pygame.K_ESCAPE:
    #             running = False
    #     check for closing window
        if event.type == pygame.QUIT:
            running = False
    # update every thing
    all_sprites.update()

   # Render all changes
    screen.fill(BLACK)
    all_sprites.draw(screen)


    pygame.display.flip()


pygame.quit()
