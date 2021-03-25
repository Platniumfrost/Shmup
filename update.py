#update folder variables
player_animation_folder = path.join(Player_expl)
explosion_animate = path.join(imgs_folder)
#under a new npc_animation folder
npc_explosion_animate = path.join(imgs_folder)

#under load imgs
#under for img in meteor list:
#create load explostion animation imgs
explosion_anim = {}
explosion_anim["lg"] =[]
explosion_anim["sm"] = []
expostion_anim["player"] = []
for i in range(9):
    fn = "regularExplosion00.png".format(i)
    img = pg.image.load(path.join(npc_explosion_animate,fn)).convert()
    img_lg = pg.transform.scale(img,100,100)
    img_sm = pg.transform.scale(img, 40, 40)
    explosion_anim["sm"].append(img_sm )
    explosion_anim["lg"].append(img_lg )
    # adding player explosion
    fn = "sonicExplosion{}.png".format(i)
    img = pg.image.load(path.join(player_Player_expl, fn)).convert()
    img.set_colorkey(BLACK)
    explosion_anim["player"].append(img)


#under "if bullet hits npc"
#under score += 50 - hit.radius
expl = Explosion(hit.rect.center,"lg")
all_sprites.add(expl)

#under NPC hits player
#under player.sheild
expl = Explosion(hit.rect.center,"sm")
all_sprites.add(expl)
if player.sheild <= 0:
    death_expl = Explosion(player.rect.center,"player")
    all_sprites.add(death_expl)
    player.hide()

    if player.lives <= 0 and not death_expl.alive():
        playing = False



#under load images
#under player img loaded
#under player_img = pg.image
player_mini_img = pg.transform.acale(player_img,(25,19))
player_mini_img.set_colorkey(BLACK)


# under class Player
#under self.last_shot = pg.time.get_ticks()
    self.lives = 3
    self.hide_timer = pg.time.get_ticks()
    self.hide_timer = False

def hide(self):
    #hide the player temporarily
    self.lives -= 1
    self.hiden = True
    self.hide_time = pg.time.get_ticks()
    self.rect.center = (WIDTH / 2, HEIGHT +200)
    self.sheild = 100

def update(self):
    #unhide if hidden
    if self.hidden and pg.time.get_ticks() - self.hide_timer > 3000:
        self.hidden = False
        self.rect.bottom(HEIGHT - (HEIGHT*.05))
        self.rect.centerx = (SIDTH / 2)




#







# **** kill is self.kill **** #


