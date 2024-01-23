from os import environ
from turtle import update

import win32api

# Hacky disable support prompt
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = '1'


import pygame as pg

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
            self.tick()
    
    def render(self):
        pass