import math
from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = '1'
import pygame as pg

from Game import Game
from Objects import Object

def main():
    width, height = 300, 300
    refresh_rate = Game.getRefreshRate()
    g = Game(width, height, refresh_rate)
    defaultCube = Object.getDefaultPrism()
    # defaultCube.scale(10, 10, 10)
    defaultCube.rX(math.radians(45))
    defaultCube.rY(math.radians(20))
    g.addModel(defaultCube)
    print("WASDQE = Translation\nArrows = Rotation\n\"[\" and \"]\" for Zooming in/out")
    g.loop()
    
if __name__ == "__main__":
    main()
