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
    def rX(self, t: float) -> List[np.ndarray]:
        rotverts = []
        for vert in obj.verts:
            rotverts.append(vert.rX(t))
        self.verts = rotverts
        return rotverts

    # rot around Y axis
    def rY(self, t: float) ->List[np.ndarray]:
        rotverts = []
        for vert in self.verts:
            rotverts.append(vert.rY(t))
        self.verts = rotverts
        return rotverts

    # rot around Z axis
    def rZ(self, t: float) ->List[np.ndarray]:
        rotverts = []
        for vert in self.verts:
            rotverts.append(vert.rZ(t))
        self.verts = rotverts
        return rotverts
    
    # Scale
    def scale(self, sx: float = 1, sy: float = 1, sz: float = 1) -> List[np.ndarray]:
        scaledverts = []
        for vert in self.verts:
            scaledverts.append(vert.scale(sx, sy, sz))
        self.verts = scaledverts
        return scaledverts

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

    def draw(self, distance):
        for con in self.connections:
            pt1 = self.verts[con[0]].project(distance) + int(self.screen.get_width()/2)
            pt2 = self.verts[con[1]].project(distance) + int(self.screen.get_width()/2)
            pg.draw.line(self.screen, (255, 255, 255), (pt1.x, pt1.y), (pt2.x, pt2.y), 2)


if __name__ == "__main__":
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
    obj = Object(vertList, connectList)
    obj.printout()
    print(Object.rX(obj,pi/4))