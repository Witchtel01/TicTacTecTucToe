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
    defaultCube.rZ(math.radians(45))
    defaultCube.scale(10, 10, 4)
    g.addModel(defaultCube)
    g.loop()
    
if __name__ == "__main__":
    main()
    