import math

import pygame as pg
import win32api

from Game import Game
    
def sc(theta):
    return math.sin(theta)*math.cos(theta)

def clamp(val, mini, maxi):
    return max(min(maxi, val), mini)


boxX, boxY = 150, 150
boxW, boxH = 100, 100
boxZ, boxD = 100, 100
thetaX = math.radians(45)
thetaY = math.radians(45)

def checkHeld(game: Game):
    global thetaY, holding, thetaX
    if "up" in game.holding:
        thetaY = clamp((thetaY + math.radians(1)), -math.pi/4, math.pi/4)
    if "down" in game.holding:
        thetaY = clamp((thetaY - math.radians(1)), -math.pi/4, math.pi/4)
    if "right" in game.holding:
        thetaX = clamp((thetaX + math.radians(1)), -math.pi/4, math.pi/4)
    if "left" in game.holding:
        thetaX = clamp((thetaX -math.radians(1)), -math.pi/4, math.pi/4)
        # thetaX = (thetaX - math.radians(1))%math.pi
    if "enter" in game.holding:
        print(thetaX, thetaY)

def loop(game: Game):
    while game.eventhandler.isRunning():
        ptlist = [
            (boxX-int(boxW/2), boxY-int(boxH/2)),
            (boxX-int(boxW/2)+boxD*sc(thetaX), boxY-int(boxH/2)-boxD*sc(thetaY)),
            
        ]
        game.eventhandler.updateEvents()
        checkHeld(game)
        
        pg.draw.aalines(game.screen,
                    "white",
                    False,
                    [(boxX-int(boxW/2), boxY-int(boxH/2)),
                        (boxX-int(boxW/2) + boxD*sc(thetaX), boxY-int(boxH/2)-boxD*sc(thetaY)),
                    (boxX+int(boxW/2) + boxD*sc(thetaX), boxY-int(boxH/2)-boxD*sc(thetaY)),
                    (boxX+int(boxW/2), boxY-int(boxH/2)),
                    (boxX-int(boxW/2), boxY-int(boxH/2)),
                    (boxX-int(boxW/2), boxY+int(boxH/2)),
                    (boxX+int(boxW/2), boxY+int(boxH/2)),
                    (boxX+int(boxW/2)+boxD*sc(thetaX), boxY+int(boxH/2)-boxD*sc(thetaY)),
                    (boxX-int(boxW/2)+boxD*sc(thetaX), boxY+int(boxH/2)-boxD*sc(thetaY)),
                    (boxX-int(boxW/2), boxY+int(boxH/2))])
        pg.draw.aaline(game.screen,
                    "white",
                    (boxX-int(boxW/2)+boxD*sc(thetaX), boxY-int(boxH/2)-boxD*sc(thetaY)),
                    (boxX-int(boxW/2)+boxD*sc(thetaX), boxY+int(boxH/2)-boxD*sc(thetaY)))
        pg.draw.aaline(game.screen,
                    "white",
                    (boxX+int(boxW/2), boxY-int(boxH/2)),
                    (boxX+int(boxW/2), boxY+int(boxH/2)))
        pg.draw.aaline(
            game.screen,
            "white",
            (boxX+int(boxW/2)+boxD*sc(thetaX), boxY-int(boxH/2)-boxD*sc(thetaY)),
            (boxX+int(boxW/2)+boxD*sc(thetaX), boxY+int(boxH/2)-boxD*sc(thetaY))
        )
        game.tick()

def main():
    width, height = 300, 300
    refresh_rate = getattr(win32api.EnumDisplaySettings(win32api.EnumDisplayDevices().DeviceName, -1), "DisplayFrequency")
    game = Game(width, height, refresh_rate)
    vertList = [(2, 3, 1),
            (2, 3, -1),
            (2, -3, 1),
            (2, -3, -1),
            (-2, 3, 1),
            (-2, 3, -1),
            (-2, -3, 1),
            (-2, -3, -1)]
    connectList = [(0, 1), (1, 3), (3, 2), (2, 0),
                   (4, 5), (5, 7), (7, 6), (6, 4),
                   (0, 4), (1, 5), (2, 6), (3, 7)]
    
    clock = pg.time.Clock()
    loop(game)

if __name__ == "__main__":
    main()
    pg.quit()