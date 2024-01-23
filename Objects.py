from math import cos, pi, sin
from typing import List, Tuple

import numpy as np

from matrixshit import Point


class Object:
    def __init__(self, verts: List[Tuple[float, float, float]], connects: List[Tuple[int, int]]):
        self.verts = [Point.from_tuple((x, y, z)) for x, y, z in verts]
        self.connections = np.array(connects)
    
    @classmethod
    def from_points(cls, pointList: List['Point'], connects: List[Tuple[int, int]]):
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
        for vert in obj.verts:
            rotverts.append(vert.rY(t))
        self.verts = rotverts
        return rotverts

    # rot around Z axis
    def rZ(self, t: float) ->List[np.ndarray]:
        rotverts = []
        for vert in obj.verts:
            rotverts.append(vert.rZ(t))
        self.verts = rotverts
        return rotverts

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

    def draw(self):
        pass


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