import pygame as pg
pg.init()
pg.display.set_mode((0,0), pg.FULLSCREEN)
while True:
    pg.display.get_surface().fill((255,255,255))
    pg.display.flip()
    pg.time.Clock().tick(30)
    pg.display.get_surface().fill((0,0,0))
    pg.display.flip()
    pg.time.Clock().tick(30)