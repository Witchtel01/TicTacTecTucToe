from math import cos, sin
from typing import Tuple

import numpy as np


class Point3(np.ndarray):
    # Point3 with x, y, z parameters
    def __new__(cls, x: float, y: float, z: float) -> 'Point3':
        obj = super(Point3, cls).__new__(cls, (4,1), dtype=float)
        obj[0, 0] = x
        obj[1, 0] = y
        obj[2, 0] = z
        obj[3, 0] = 1.0
        return obj
    
    # Duh
    @classmethod
    def from_tuple(cls, coordinates: Tuple[float, float, float]) ->'Point3':
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
    
    # Translation by translation matrix
    def translate(self, x: float = 0, y: float = 0, z: float = 0) -> 'Point3':
        transarray = np.array([
            (1, 0, 0, x),
            (0, 1, 0, y),
            (0, 0, 1, y),
            (0, 0, 0, 1)
        ])
        self = transarray.dot(self)
        return self
    
    # Scaling from scale matrix
    def scale(self, sx: float = 0, sy: float = 0, sz: float = 0) -> 'Point3':
        scalearray = np.array({
            (sx, 0, 0, 0),
            (0, sy, 0, 0),
            (0, 0, sz, 0),
            (0, 0, 0, 1)
        })
        self = scalearray.dot(self)
        return self

    # Rotation around X axis
    def rX(self, t: float) -> 'Point3':
        rotarray = np.array([(1, 0, 0, 0),
                    (0, cos(t), -sin(t), 0),
                    (0, sin(t), cos(t), 0),
                    (0, 0, 0, 1)], dtype=float)
        return rotarray.dot(self)
    
    # Rotation around y axis
    def rY(self, t: float) -> 'Point3':
        rotarray = np.array([(cos(t), 0, sin(t), 0),
            (0, 1, 0, 0),
            (-sin(t), 0, cos(t), 0),
            (0, 0, 0, 1)])
        self = rotarray.dot(self)
        return self
    
    # Rotation around Z axis
    def rZ(self, t: float) -> 'Point3':
        rotarray = np.array([(cos(t), -sin(t), 0, 0),
                    (sin(t), cos(t), 0, 0),
                    (0, 0, 1, 0),
                    (0, 0, 0, 1)])
        self = rotarray.dot(self)
        return self
    
    # To string representation
    def __repr__(self) -> str:
        return f"Point3(x={self.x},y={self.y},z={self.z},a={self.a})"


class Point2(np.ndarray):
    # Point2 with x, y and homogeneous value
    def __new__(cls, x: float, y: float) -> 'Point2':
        obj = super(Point2, cls).__new__(cls, (3, 1), dtype=float)
        obj[0, 0] = x
        obj[1, 0] = y
        obj[2, 0] = 1.0
        return obj
    
    # Duh
    @classmethod
    def from_tuple(cls, coordinates: Tuple[float, float]) -> 'Point2':
        x, y = coordinates
        return cls(x, y)
    @property
    def x(self):
        return self[0, 0]
    @property
    def y(self):
        return self[1, 0]
    @property
    def a(self):
        return self[2, 0]
    
    # To string representation
    def __repr__(self) -> str:
        return f"Point2(x={self.x}),y={self.y},a={self.a}"