import tkinter
import pygame as pg
import random as r

#load imgs
#bottome of load imgs portion

meteor_images = []#insert (copy, paste)asteroid into list
for img in meteor_images.append(pg.image.load(path.join(enemy_img_folder, img)))


#under self.image in npc class
#npc class change all img to image_orig

self.image = self.image_orig.copy()
#bottom of npc class
#rot=rotation
self.rot = 0 #rotation
self.rot_speed = r.randint(-8,8)
self.update = pg.time.get_ticks()

def rotate(self):
    now = pg.time.get_ticks()
    if now - self.last_update > 60:
        self.last_update = now
        # do the rotation
        self.rot = (self.rot+self.rot_speed)%360
        new_image = pg.transform.rotate(self.image_oirig, self.rot)
        old_center = self.rect.center
        self.image = new_image
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.old_center



    def update(self):
        self.rotate()
        self.rect.y += self.speedy
        self.rect.x += self.speedx


#shooter game SCORES
##remember to put score in game loop#
playing =  True
score = 0
score += 10 # put this in #if npc#
print(score)#put this in the render function
#under def spawn
#and under game functions
def draw_text(surf,text,size, x, y, color)
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True,color)
    text_rect = text_surface.get_rect()
    text_rect.midtop(x,y)
    surf.blit(text_surface)
#under game constants
font_name = pg.font.match_font("arial")

#just above render
for hit in hits
score += 50 - hit.radius
npc.spawn()
#under render
draw_text(screen,"Score: "+str(score),18, WIDTH/2,10,WHITE)






#explosion animations




# different size of sprites
#download the zip off of canvas
#copy and paste into "enemies" folder or drag and drop in folder.