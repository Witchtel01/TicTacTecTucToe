import pygame as pg

class EventHandler:
    def __init__(self) -> None:
        self.holding = []
        self.running = True
    def updateEvents(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.VIDEORESIZE:
                pg.display.set_mode((event.w, event.h), pg.RESIZABLE)
            elif event.type == pg.MOUSEBUTTONDOWN:
                self.holding.append(event.button)
            elif event.type == pg.KEYDOWN:
                self.holding.append(event.key)
            elif event.type == pg.KEYUP:
                self.holding.remove(event.key)
    def getKeys(self):
        return self.holding
    def isRunning(self):
        return self.running