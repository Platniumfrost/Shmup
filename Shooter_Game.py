import pygame as pg
import random as r
import math
from os import *


# Game object classes
####################################################################

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.sheild = 100
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.centerx = (WIDTH / 2)
        self.rect.bottom = (HEIGHT - (HEIGHT * .05))
        self.speedx = 0
        #self.shoot_delay
        self.last_shot = pg.time.get_ticks()
        self.lives = 3
        self.hide_timer = pg.time.get_ticks()
        self.hidden = False
        self.power_level = 1
        self.powTimer = pg.time.get_ticks()

    def gun_pow_up(self):
        self.power_level+=1
        self.powTimer = pg.time.get_ticks()

    def sheilds_up(self,num):
        player.sheild += r.randint(15, 50)
        if player.sheild >= 100:
            player.sheild = 100

    def update(self):
        #time out power ups
        if self.power_level >= 2 and pg.time.get_ticks() - self.powTimer > POWERUP_TIME:
            self.power_level -= 1
            self.powTimer = pg.time.get_ticks()

        # basic movement side to side
        self.speedx = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_RIGHT] or keystate[pg.K_d]:
            self.speedx = 5
        if keystate[pg.K_LEFT] or keystate[pg.K_a]:
            self.speedx = -5
        # if keystate[pg.K_SPACE]:
        #     self.shoot()

        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH

        self.rect.x += self.speedx

    def shoot(self):
        now = pg.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            if self.power_level == 1:
                b = Bullet(self.rect.centerx,self.rect.top+1)
                all_sprites.add(b)
                bullet_group.add(b)
                shoot_snd.play()

            elif self.power_level >= 2:
                b1 = Bullet(self.rect.left, self.rect.centery)
                b2 = Bullet(self.rect.right, self.rect.centery)
                all_sprites.add(b1)
                bullet_group.add(b1)
                all_sprites.add(b2)
                bullet_group.add(b2)
                shoot_snd.play()

            elif self.power_level >= 3:
                b = Bullet(self.rect.centerx, self.rect.top + 1)
                b1 = Bullet(self.rect.left, self.rect.centery)
                b1.inc_spred(-3)
                b2 = Bullet(self.rect.right, self.rect.centery)
                b.inc_spred(3)
                all_sprites.add(b1)
                bullet_group.add(b1)
                all_sprites.add(b2)
                bullet_group.add(b2)
                all_sprites.add(b)
                bullet_group.add(b)
                shoot_snd.play()



class Bullet(pg.sprite.Sprite):
    def __init__(self, x,y):
        super(Bullet,self).__init__()
        #self.image = pg.Surface((5, 10))
        #self.image.fill(BLUE)
        self.image = bullet_img
        self.image = pg.transform.scale(self.image, (15, 30))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speed = -10
        self.spread = 0

    def inc_spred(self,num):
        self.spread = num

    def update(self):
        self.rect.y += self.speed
        self.rect.x += self.spread
        # kill the bullet when bottom < screen
        if self.rect.bottom < 0:
            self.kill()

class Star (pg.sprite.Sprite):
    pass

class NPC(pg.sprite.Sprite):
    def __init__(self):
        super(NPC, self).__init__()
        self.image = pg.Surface((25, 25))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        # self.rect.centerx = (WIDTH / 2)
        # self.rect.top = (0)
        # self.speed = -10
        self.rect.x = r.randrange(WIDTH - self.rect.width)
        self.rect.y = r.randrange(-100, -40)
        self.speedy = r.randrange(1, 8)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10:
            self.rect.x = r.randrange(WIDTH - self.rect.width)
            self.rect.y = r.randrange(-100, -40)
            self.speedy = r.randrange(1, 8)

class Explostion(pg.sprite.Sprite):
    def __init__(self, center, size):
        super(Explostion, self).__init__()
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pg.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pg.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size])
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center= center

class Pow(pg.sprite.Sprite):
    def __init__(self,center):
        super(Pow, self).__init__()
        self.type = r.choice(powerUps_chance)
        self.image = pows_images[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 3

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.kill()




####################################################################


# Game Constants
####################################################################
HEIGHT = 900
WIDTH = 600
FPS = 60

# Colors (R,G,B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

title = "Shmup"
font_name = pg.font.match_font("arial")

powerUps_list = ["gun","sheild"]
powerUps_chance = ["gun","gun","sheild","sheild","sheild","sheild","sheild","sheild","sheild","sheild","sheild"]

POWERUP_TIME = 10000
####################################################################

# initialize pygame and create window
####################################################################
pg.init()
pg.mixer.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(title)
clock = pg.time.Clock()
####################################################################
#folder variables
####################################################################
game_folder = path.dirname(__file__)

pow_folder = path.join(imgs_folder,"pows")
#####################################################################





# load imgs
####################################################################

####################################################################

# create Sprite groups
####################################################################
all_sprites = pg.sprite.Group()
players_group = pg.sprite.Group()
npc_group = pg.sprite.Group()
bullet_group = pg.sprite.Group()
star_group = pg.sprite.Group()
pows_group = pg.sprite.Group()
###################################################################

# Game Loop
###################
# game update Variables
########################################
playing = True
game_over = True
score = 0

########################################
################################################################
while playing:
    if game_over:
        show_go_screen()
        game_over = False
    # create Game Objects
    ###################################################################
    for i in range(25):
        star = Star()
        star_group.add(star)

    player = Player()

    npc = NPC()
    for i in range(10):
        npc = NPC()
        npc_group.add(npc)
    # bullet = Bullet(HEIGHT,WIDTH/2)
    ####################################################################

    # add objects to sprite groups
    ####################################################################
    players_group.add(player)
    # bullet_group.add(Bullet)
    npc_group.add(npc)

    for i in players_group:
        all_sprites.add(i)

    for i in npc_group:
        all_sprites.add(i)
    ####################################################################
    # timing
    ##################################################
    clock.tick(FPS)
    ##################################################

    # collecting Input
    ##################################################

    # Quiting the game when we hit the x
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                player.shoot()
            if event.key == pg.K_ESCAPE:
                playing = False
        if event.type == pg.QUIT:
            playing = False

    ##################################################
    # Updates
    ##################################################
    all_sprites.update()

    # if NPC hits player
    hits = pg.sprite.spritecollide(player,npc_group,False)
    if hits:
        if player.lives < = 0:
            game_over = False
        #npc.spawn()
    # if bullet hits npc
    hits = pg.sprite.groupcollide(npc_group,bullet_group,True,True)
    for hit in hits:
        score += 50 - hit.radius
        exlp = Explostion(hit.rect.center,"lg")
        all_sprites.add(exlp)
        npc.spawn()
        r.choice(expl_sounds).play()
        if r.random() > .85:
            pow = Pow(hit.rect.center)
            all_sprites.add(pow)
            pows_group.add(pow)

    hits = pg.sprite.spritecollide(player, pows_group, True, pg.sprite.collide_circle)
    for hit in hits:
        if hit.type == "sheild":
            num = r.random()
            player.sheilds_up(num)
        elif hit.type == "gun":
            player.gun_pow_up()



    ##################################################
    # Render
    ##################################################

    screen.fill(BLACK)
    all_sprites.draw(screen)

    pg.display.flip()
    ##################################################

pg.quit()
################################################################
#####################
