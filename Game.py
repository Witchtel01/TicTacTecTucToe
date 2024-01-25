from math import radians

import numpy as np
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
        self.distance = 1
        self.focalLength = 1.0
        self.nearClipping = 0.1
        self.models = []
        self.viewTransform = np.array([
            (1,0,0,0),
            (0,1,0,0),
            (0,0,1,0),
            (0,0,0,1)], dtype= float)
        self.eventhandler = EventHandler()
    
    @staticmethod
    def getRefreshRate() -> int:
        return getattr(win32api.EnumDisplaySettings(win32api.EnumDisplayDevices().DeviceName, -1), "DisplayFrequency")
    
    def addModel(self, obj: 'Object'):
        self.models.append(obj)
    
    def tick(self) -> None:
        self.screen.fill((0,0,0))
        self.render()
        pg.display.flip()
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
                self.viewTransform[1, 3] +=1
            elif event == pg.K_s:
                self.viewTransform[1, 3] -=1
            elif event == pg.K_a:
                for obj in self.models:
                    obj.translate(-1, 0, 0)
            elif event == pg.K_d:
                for obj in self.models:
                    obj.translate(1, 0, 0)
            elif event == pg.K_q:
                self.viewTransform[3, 3] -=1
            elif event == pg.K_e:
                self.viewTransform[3, 3] +=1
            elif event == pg.K_i:
                self.distance +=0.1
            elif event == pg.K_o:
                self.distance -=0.1

    def render(self):
        for obj in self.models:
            obj.draw(self.distance, self.focalLength, self.nearClipping, self.viewTransform)