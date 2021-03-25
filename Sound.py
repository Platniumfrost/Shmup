#Sound Effects#
#### Set up ####
shoot_snd = pg.mixer.Sound(path.join(snds_folder,"pew (1).wav"))
expl_sounds = []
for snd in ['expl3 (1).wav', 'expl (1).wav']:
    expl_sounds.append(pg.mixer.Sound(path.join(snds_folder, snd)))


### put in game loop ####
r.choice(expl_sounds).play()

### if bullet hits npc ###
r.choice(expl_sounds).play()


###############################################################################
## Sound for exploding meteor ##









## Sound for the gun shooting ##








## Sound for Player dying ##





################################################################################
## Backgroud Music ##
##under set up###
pg.mixer.music.load(path.join(snds_folder,"tgfcoder-FrozenJam-Seamlessloop (1).ogg"))
pg.mixer.music.set_volume(o.4)
pg.mixer.music.play(loops=-1)