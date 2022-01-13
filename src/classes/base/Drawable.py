import pygame as pg
from classes.base.Coordinate import Coordinate

CONTOUR = 3


class Drawable():

    def __init__(self, surface: pg.Surface, coordinate: Coordinate):
        self.surface = surface
        self.coordinate = coordinate

    @property
    def rect(self):
        return pg.Rect(self.coordinate.real_x, self.coordinate.real_y, self.surface.get_width(), self.surface.get_height())

    @rect.setter
    def rect(self, value: pg.Rect):
        self.coordinate.real_position = value.topleft
        self.surface = pg.transform.scale(
            self.surface, (value.width, value.height))

    @property
    def fat_rect(self):
        return pg.Rect(self.coordinate.real_x - CONTOUR, self.coordinate.real_y - CONTOUR, self.surface.get_width() + 2 * CONTOUR, self.surface.get_height() + 2 * CONTOUR)

    @fat_rect.setter
    def fat_rect(self, value: pg.Rect):
        self.coordinate.real_position = value.left + CONTOUR, value.top + CONTOUR
        self.surface = pg.transform.scale(
            self.surface, (value.width - CONTOUR, value.height - CONTOUR))

    def draw(self, surface: pg.Surface):
        surface.blit(self.surface, self.coordinate.real_position)
