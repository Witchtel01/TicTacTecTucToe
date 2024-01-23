from math import cos, sin
from typing import Tuple

import numpy as np


class Point(np.ndarray):
    def __new__(cls, x: float, y: float, z: float) -> 'Point':
        obj = super(Point, cls).__new__(cls, (4,1), dtype=float)
        obj[0, 0] = x
        obj[1, 0] = y
        obj[2, 0] = z
        obj[3, 0] = 1.0
        return obj
    
    @classmethod
    def from_tuple(cls, coordinates: Tuple[float, float, float]) ->'Point':
        x, y, z = coordinates
        return cls(x,y,z)
    
    @property
    def x(self):
        return self[0, 0]
    @property
    def y(self):
        return self[1, 0]
    @property
    def z(self):
        return self[2, 0]
    @property
    def a(self):
        return self[3, 0]
    
    def translate(self, x: float = 0, y: float = 0, z: float = 0) -> 'Point':
        transarray = np.array([
            (1, 0, 0, x),
            (0, 1, 0, y),
            (0, 0, 1, y),
            (0, 0, 0, 1)
        ])
        self = transarray.dot(self)
        return self
    
    def scale(self, sx: float = 0, sy: float = 0, sz: float = 0) -> 'Point':
        scalearray = np.array({
            (sx, 0, 0, 0),
            (0, sy, 0, 0),
            (0, 0, sz, 0),
            (0, 0, 0, 1)
        })
        self = scalearray.dot(self)
        return self

    def rX(self, t: float) -> 'Point':
        rotarray = np.array([(1, 0, 0, 0),
                    (0, cos(t), -sin(t), 0),
                    (0, sin(t), cos(t), 0),
                    (0, 0, 0, 1)], dtype=float)
        return rotarray.dot(self)
    
    def rY(self, t: float) -> 'Point':
        rotarray = np.array([(cos(t), 0, sin(t), 0),
            (0, 1, 0, 0),
            (-sin(t), 0, cos(t), 0),
            (0, 0, 0, 1)])
        self = rotarray.dot(self)
        return self
    
    def rZ(self, t: float) -> 'Point':
        rotarray = np.array([(cos(t), -sin(t), 0, 0),
                    (sin(t), cos(t), 0, 0),
                    (0, 0, 1, 0),
                    (0, 0, 0, 1)])
        self = rotarray.dot(self)
        return self
    
    def __repr__(self) -> str:
        return f"Point(x={self.x},y={self.y},z={self.z},a={self.a})"
        