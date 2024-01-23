from math import radians

import pygame as pg
import win32api

from EventHandler import EventHandler
from Objects import Object


class Game:
    def __init__(self, w: int, h: int, refresh_rate: int) -> None:
        self.holding = []
        pg.init()
        self.screen = pg.display.set_mode((w, h), pg.RESIZABLE)
        self.clock = pg.time.Clock()
        self.refresh_rate = refresh_rate
        self.models = []
        self.eventhandler = EventHandler()
    
    @staticmethod
    def getRefreshRate() -> int:
        return getattr(win32api.EnumDisplaySettings(win32api.EnumDisplayDevices().DeviceName, -1), "DisplayFrequency")
    
    def addModel(self, obj: 'Object'):
        self.models.append(obj)
    
    def tick(self) -> None:
        self.render()
        pg.display.flip()
        self.screen.fill((0,0,0))
        self.clock.tick(self.refresh_rate)
        pg.display.set_caption(
            f"FPS: {round(self.clock.get_fps(), 2)}"
        )
    
    def loop(self):
        while self.eventhandler.isRunning():
            self.eventhandler.updateEvents()
            self.handleEvents()
            self.tick()
    
    def handleEvents(self):
        for event in self.eventhandler.getKeys():
            if event == pg.K_UP:
                for obj in self.models:
                    obj.rX(radians(1))
            elif event == pg.K_DOWN:
                for obj in self.models:
                    obj.rX(radians(-1))
            elif event == pg.K_LEFT:
                for obj in self.models:
                    obj.rY(radians(-2))
            elif event == pg.K_RIGHT:
                for obj in self.models:
                    obj.rY(radians(2))
            elif event == pg.K_LEFTBRACKET:
                for obj in self.models:
                    obj.scale(0.9, 0.9, 0.9)
            elif event == pg.K_RIGHTBRACKET:
                for obj in self.models:
                    obj.scale(1.1, 1.1, 1.1)
            elif event == pg.K_w:
                for obj in self.models:
                    obj.translate(0, -1, 0)
            elif event == pg.K_s:
                for obj in self.models:
                    obj.translate(0, 1, 0)
            elif event == pg.K_a:
                for obj in self.models:
                    obj.translate(-1, 0, 0)
            elif event == pg.K_d:
                for obj in self.models:
                    obj.translate(1, 0, 0)
    
    def render(self):
        for obj in self.models:
            obj.orthodraw()