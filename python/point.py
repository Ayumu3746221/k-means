import math
import random

class Point:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def distance(self, other):
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(self.coordinates, other.coordinates)))

    @classmethod
    def random(cls, dims, lower=0, upper= 100):
        return cls([random.uniform(lower, upper) for _ in range(dims)])

    def __repr__(self):
        return f"Point({self.coordinates})"