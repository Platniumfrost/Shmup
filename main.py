import pygame
import random

HEIGHT = 360
WIDTH = 480
FPS = 30
title = "Template"

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
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.Surface((25,25))
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect()
        self.rect.center =  (WIDTH/2, HEIGHT/2)
        self.speed = [5,0]
    def update(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

        if self.rect.left > WIDTH:
            self.rect.top = HEIGHT
            self.rect.centerx=WIDTH/2
            self.speed[1] = -5
            self.speed[0] = 0
        if self.rect.right > WIDTH:
            self.rect.bottom = HEIGHT
            self.rect.centerx = WIDTH / 2
            self.speed[1] = -5
            self.speed[0] = 0
        if self.rect.top > HEIGHT:
            self.rect.left = WIDTH
            self.rect.y += 5
            self.rect.x += 0
        # if self.rect.bottom > HEIGHT:
        #     self.rect.top = (HEIGHT, WIDTH / 2)
        #     self.rect.y += -5
        #     self.rect.x += 0


# initialize pygame and create window
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(title)

clock = pygame.time.Clock()

# sprite groups
all_sprites = pygame.sprite.Group()
players_group = pygame.sprite.Group()
mobs_group = pygame.sprite.Group()

# create game objects
player = Player()

#add objects to sprite groups
all_sprites.add(player)
players_group.add(player)


# game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # process input
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # update every thing
    all_sprites.update()


    # Render all changes
    screen.fill(BLACK)
    all_sprites.draw(screen)

    pygame.display.flip()


