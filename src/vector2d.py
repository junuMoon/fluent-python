import math
from typing import Union

class Vector:

    def __init__(self, x:Union[int, float]=0, y:Union[int, float]=0) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Vector({self.x!r}, {self.y!r})"

    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(self.x or self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scaler):
        return Vector(self.x * scaler, self.y * scaler)

