import pygame as pg


class Drawable():

    def __init__(self, surface: pg.Surface, position: tuple[int, int]):
        self.surface = surface
        self.position = position

    @property
    def rect(self):
        return pg.Rect(self.x, self.y, self.surface.get_width(), self.surface.get_height())

    @rect.setter
    def rect(self, value: pg.Rect):
        self.position = value.topleft
        self.surface = pg.transform.scale(
            self.surface, (value.width, value.height))

    @property
    def fat_rect(self):
        return pg.Rect(self.x, self.y, self.surface.get_width() + 1, self.surface.get_height() + 1)

    @fat_rect.setter
    def fat_rect(self, value: pg.Rect):
        self.position = value.topleft
        self.surface = pg.transform.scale(
            self.surface, (value.width - 1, value.height - 1))

    @property
    def x(self):
        return self.position[0]

    @x.setter
    def x(self, value: int):
        self.position = value, self.position[1]

    @property
    def y(self):
        return self.position[1]

    @y.setter
    def y(self, value: int):
        self.position = self.position[0], value

    def draw(self, screen: pg.Surface):
        screen.blit(self.surface, self.position)
