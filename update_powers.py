import pygame as pg
#under load explostion imgs and explosion_anim
#under explosion_anime
pows_images = {}
for i in range(len(powerUps_list)):
    fn = "img_{}.png".format(i)
    pows_images[powerUps_list[i]] = pg.image.load(path.join(pow_folder,fn))

#under game functions
def show_go_screen():
    screen.blit(background, background_rect)
    draw_text(scree, "SHMUP!", 64, WIDTH / 2, HEIGHT / 4, WHITE)
    draw_text(screen, "Arrow keys move, space to fire", 22, WIDTH / 2, HEIGHT / 2,WHITE)
    draw_text(screen, "press a key to begin", 18, WIDTH / 2, HEIGHT * 3 / 4,WHITE)
    pg.display.flip()
    waiting = True
    while waiting:
        clock.ticks(FPS)
        for event in pg.event.get():
            if event.tupe == pg.QUIT:
                pg.quit()
            if event.type == pg.KEYUP:
                waiting = False




