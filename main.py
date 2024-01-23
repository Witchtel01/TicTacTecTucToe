# import math
import colorsys
import random
import win32api

import pygame as pg

pg.init()
screen = pg.display.set_mode((300,300), pg.RESIZABLE)
refresh_rate = getattr(win32api.EnumDisplaySettings(win32api.EnumDisplayDevices().DeviceName, -1), 'DisplayFrequency')


clock = pg.time.Clock()

running = True
ellipsex = 10
ellipsey = 10
dx = random.random()*10
dy = random.random()*10


def clamp( num, mini, maxi):
    return max(min(num, maxi), mini)

screen.fill((255,255,255))
hue = 0

while running:
    # screen.fill((0,0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.VIDEORESIZE:
            screen = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)
        elif event.type == pg.KEYUP:
            if event.key == pg.K_ESCAPE:
                running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            hue = (hue+0.2)%1
    ellipsey+=dy
    ellipsex+=dx
    if ellipsex >=screen.get_size()[0] or ellipsex <=0:
        dx = -dx
        ellipsex = clamp(ellipsex, 0, 300)
    if ellipsey >= screen.get_size()[1] or ellipsey <=0:
        dy = -dy
        ellipsey = clamp(ellipsey, 0, 300)
    pg.draw.circle(screen, tuple(int(val*255) for val in colorsys.hsv_to_rgb(hue, 1, 1)), (ellipsex,ellipsey), 5)
    hue = (hue+0.005)%1
    # pg.draw.ellipse(screen, (255,255,255), (ellipsex, ellipsey, 10, 10),2)
    pg.display.flip()
    clock.tick(refresh_rate)
    pg.display.set_caption(
        f"fps: {round(clock.get_fps(), 2)}"
    )

pg.quit()