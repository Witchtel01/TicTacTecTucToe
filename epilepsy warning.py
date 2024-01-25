import pygame as pg

pg.init()
screen = pg.display.set_mode((0,0), pg.FULLSCREEN)
clock = pg.time.Clock()
pg.display.set_caption("Epilepsy Warning")

running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill((255,255,255))
    pg.display.flip()
    clock.tick(30)
    screen.fill((0,0,0))
    pg.display.flip()
    clock.tick(30)

pg.quit()