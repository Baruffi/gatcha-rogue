import pygame as pg


class CoordinateSystem():
    scale_x = 1
    scale_y = 1

    @classmethod
    def get_grid_coords(cls, x: int = None, y: int = None):
        if x and y:
            return x * cls.scale_x, y * cls.scale_y
        elif x:
            return x * cls.scale_x
        elif y:
            return y * cls.scale_y

    @classmethod
    def get_real_coords(cls, x: int = None, y: int = None):
        if x and y:
            return x // cls.scale_x, y // cls.scale_y
        elif x:
            return x // cls.scale_x
        elif y:
            return y // cls.scale_y


class Coordinate():

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @property
    def position(self):
        return self.x, self.y

    @position.setter
    def position(self, value: tuple[int, int]):
        self.x, self.y = value

    def __iter__(self):
        yield from self.position

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Coordinate):
            return self.x == __o.x and self.y == __o.y
        elif type(__o) is tuple:
            x, y = __o
            if type(x) is int and type(y) is int:
                return self.x == x and self.y == y
            raise TypeError
        raise TypeError

    @property
    def real_x(self) -> int:
        return CoordinateSystem.get_real_coords(x=self.x)

    @real_x.setter
    def real_x(self, value):
        self.x: int = CoordinateSystem.get_grid_coords(x=value)

    @property
    def real_y(self) -> int:
        return CoordinateSystem.get_real_coords(y=self.y)

    @real_y.setter
    def real_y(self, value):
        self.y: int = CoordinateSystem.get_grid_coords(y=value)

    @property
    def real_position(self) -> tuple[int, int]:
        return CoordinateSystem.get_real_coords(*self.position)

    @real_position.setter
    def real_position(self, value):
        self.position: tuple[int,
                             int] = CoordinateSystem.get_grid_coords(*value)

    def center_on(self, surface: pg.Surface):
        half_width = CoordinateSystem.get_grid_coords(
            x=surface.get_width() // 2)
        half_height = CoordinateSystem.get_grid_coords(
            y=surface.get_height() // 2)

        self.x = self.x - half_width
        self.y = self.y - half_height

        return self
