from math import cos, sin
from typing import Tuple

import numpy as np


class Point3(np.ndarray):
    # Point3 with x, y, z parameters and a homongeneous coordinate
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
    def x(self) -> float:
        return self[0, 0]
    @property
    def y(self) -> float:
        return self[1, 0]
    @property
    def z(self) -> float:
        return self[2, 0]
    @property
    def w(self) -> float:
        return self[3, 0]
    
    
    def translate(self, x: float = 0, y: float = 0, z: float = 0) -> 'Point3':
        """Translates a point

        Args:
            x (float, optional): Change in X. Defaults to 0.
            y (float, optional): Change in Y. Defaults to 0.
            z (float, optional): Change in Z. Defaults to 0.

        Returns:
            Point3: _description_
        """        
        transarray = np.array([
            (1, 0, 0, x),
            (0, 1, 0, y),
            (0, 0, 1, z),
            (0, 0, 0, 1)
        ])
        transformed = transarray.dot(self)
        self[:, 0] = transformed[:, 0]
        return self
    
    
    def scale(self, sx: float = 1, sy: float = 1, sz: float = 1) -> 'Point3':
        """Scales a point

        Args:
            sx (float, optional): Scale of X. Defaults to 1.
            sy (float, optional): Scale of Y. Defaults to 1.
            sz (float, optional): Scale of Z. Defaults to 1.

        Returns:
            Point3: Scaled point
        """        
        scalearray = np.array([
            (sx, 0, 0, 0),
            (0, sy, 0, 0),
            (0, 0, sz, 0),
            (0, 0, 0, 1)
        ])
        transformed = scalearray.dot(self)
        self[:, 0] = transformed[:, 0]
        return self
    
    def rX(self, t: float) -> 'Point3':
        """Rotates a point around the X axis

        Args:
            t (float): Angle to rotate by

        Returns:
            Point3: Rotated Point
        """        
        rotarray = np.array([(1, 0, 0, 0),
                    (0, cos(t), -sin(t), 0),
                    (0, sin(t), cos(t), 0),
                    (0, 0, 0, 1)], dtype=float)
        transformed = rotarray.dot(self)
        self[:, 0] = transformed[:, 0]
        return self
    
    def rY(self, t: float) -> 'Point3':
        """Rotates a point around the Y axis

        Args:
            t (float): Angle to rotate by

        Returns:
            Point3: Rotated point
        """        
        rotarray = np.array([(cos(t), 0, sin(t), 0),
            (0, 1, 0, 0),
            (-sin(t), 0, cos(t), 0),
            (0, 0, 0, 1)])
        transformed = rotarray.dot(self)
        self[:, 0] = transformed[:, 0]
        return self
    
    
    def rZ(self, t: float) -> 'Point3':
        """Rotates a point around the Z axis

        Args:
            t (float): Angle to rotate by

        Returns:
            Point3: Rotated point
        """        
        rotarray = np.array([(cos(t), -sin(t), 0, 0),
                    (sin(t), cos(t), 0, 0),
                    (0, 0, 1, 0),
                    (0, 0, 0, 1)])
        transformed = rotarray.dot(self)
        self[:, 0] = transformed[:, 0]       
        return self
    
    
    @staticmethod
    def matrixproject(point: 'Point3', distance, focal: float, near: float, viewTransform: np.ndarray) -> 'Point2':
        """Project a Point3 object into 2D using a projection matrix

        Args:
            point (Point3): The point to project
            distance (float): Distance from camera to point (I think)
            focal (float): Camera focal length
            near (float): Some sort of special graphics value
            viewTransform (np.array): Transform by camera

        Returns:
            Point2: A new Point2 object representing the projected point
        """
        # Advanced projectmatrix
        # projectmatrix = np.array([
        #     [focal/distance, 0, 0, 0],
        #     [0, focal/distance, 0, 0],
        #     [0, 0, -(focal+near)/(focal-near), -2*(focal*near)/(focal-near)],
        #     [0, 0, -1, 0]
        # ])
        
        # Simple projectmatrix
        projectmatrix = np.array([
            (1, 0, 0, 0),
            (0, 1, 0, 0),
            (0, 0, 1, distance),
            (0, 0, 0, 1)
        ])
        transform = projectmatrix@viewTransform@point
        newpoint = Point2(transform[0, 0]/transform[3, 0], transform[1, 0]/transform[3, 0])
        return newpoint
    

    def __repr__(self) -> str:
        """Custom str(obj) definition

        Returns:
            str: Representation of the point as a string
        """        
        return f"Point3(x={self.x:f0.2},y={self.y:f0.2},z={self.z:f0.2},w={self.w:f0.2})"


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
    def x(self) -> float:
        return self[0, 0]
    @property
    def y(self) -> float:
        return self[1, 0]
    @property
    def w(self) -> float:
        return self[2, 0]
    
    def __repr__(self) -> str:
        """Custom str(obj) definition

        Returns:
            str: Representation of the point as a string
        """        
        return f"Point2(x={self.x:f0.2}),y={self.y:f0.2},w={self.w:f0.2}"