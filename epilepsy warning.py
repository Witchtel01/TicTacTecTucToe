import pygame as pg

print("Epilepsy Warning! Continue? (Y/n)")
response = input()
if response == "n" or response == "N":
    exit()
pg.init()
screen = pg.display.set_mode((300,300), pg.RESIZABLE)
clock = pg.time.Clock()
pg.display.set_caption("Epilepsy Warning")

running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.VIDEORESIZE:
            pg.display.set_mode((event.w, event.h), pg.RESIZABLE)
    screen.fill((255,255,255))
    pg.display.flip()
    clock.tick(30)
    screen.fill((0,0,0))
    pg.display.flip()
    clock.tick(30)

pg.quit()