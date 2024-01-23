import pygame as pg

from Game import Game
from Objects import Object

def main():
    width, height = 300, 300
    refresh_rate = Game.getRefreshRate()
    g = Game(width, height, refresh_rate)
    

if __name__ == "__main__":
    main()
    