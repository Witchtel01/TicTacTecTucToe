from math import pi
from typing import List, Tuple

import numpy as np

from matrixshit import Point3
import pygame as pg


class Object:
    def __init__(self, verts: List[Tuple[float, float, float]], connects: List[Tuple[int, int]]):
        self.verts = [Point3.from_tuple((x, y, z)) for x, y, z in verts]
        self.connections = np.array(connects)
        self.screen = pg.display.get_surface()
    
    @classmethod
    def from_points(cls, pointList: List['Point3'], connects: List[Tuple[int, int]]):
        return cls([(point.x, point.y, point.z) for point in pointList], connects)
    
    # rot around X axis
    def rX(self, t: float) -> None:
        for i, vert in enumerate(self.verts):
            self.verts[i] = vert.rX(t)

    # rot around Y axis
    def rY(self, t: float) ->None:
        for i, vert in enumerate(self.verts):
            self.verts[i] = vert.rY(t)

    # rot around Z axis
    def rZ(self, t: float) ->None:
        for i, vert in enumerate(self.verts):
            self.verts[i] = vert.rZ(t)
    
    # Scale
    def scale(self, sx: float = 1, sy: float = 1, sz: float = 1) -> None:
        for i, vert in enumerate(self.verts):
            self.verts[i] = vert.scale(sx, sy, sz)
            
    # Translate
    def translate(self, x: float = 0, y: float = 0, z: float = 0) -> None:
        for i, vert in enumerate(self.verts):
            self.verts[i] = vert.translate(x, y, z)

    # Duh
    def printout(self):
        print("Verts: ")
        for vert in self.verts:
            print(vert)
        print("\nConnections:")
        print(self.connections)
    
    @staticmethod
    def getDefaultPrism() -> 'Object':
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
        return Object(vertList, connectList)

    def draw(self, distance, focal, near, viewTransform):
        for con in self.connections:
            pt1 = Point3.matrixproject(self.verts[con[0]], distance, focal, near, viewTransform)
            pt2 = Point3.matrixproject(self.verts[con[1]], distance, focal, near, viewTransform)
            pg.draw.line(self.screen, (0, 255, 0),
                         (pt1.x/pt1.w+int(self.screen.get_width()/2), pt1.y/pt1.w+int(self.screen.get_height()/2)),
                         (pt2.x/pt2.w+int(self.screen.get_width()/2), pt2.y/pt2.w+int(self.screen.get_height()/2)), 2)
    
    def orthodraw(self):
        for con in self.connections:
            pt1 = self.verts[con[0]] + int(self.screen.get_width()/2)
            pt2 = self.verts[con[1]] + int(self.screen.get_width()/2)
            pg.draw.line(self.screen, (0, 255, 0), (pt1.x, pt1.y), (pt2.x, pt2.y), 2)


if __name__ == "__main__":

    obj = Object.getDefaultPrism()
    obj.printout()
    print(obj.rX(pi/4))