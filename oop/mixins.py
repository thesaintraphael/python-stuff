from multiple_inheritance import Square, Triangle


class SurfaceAreaMixin:

    def surface_area(self):
        return sum(surface.area(self) for surface in self.surfaces)


class Cube(Square, SurfaceAreaMixin):

    def __init__(self, length):
        super().__init__(length)
        self.surfaces = [Square, Square, Square, Square, Square, Square]


class RightPyramid(Square, Triangle, SurfaceAreaMixin):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height
        self.height = slant_height
        self.length = base
        self.width = base

        self.surfaces = [Square, Triangle, Triangle, Triangle, Triangle]


cube = Cube(3)
print(cube.surface_area())  # 54
