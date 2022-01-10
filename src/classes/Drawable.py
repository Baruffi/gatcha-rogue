
import pygame as pg


class Drawable():

    def __init__(self, surface: pg.Surface, position: tuple[int, int]):
        self.surface = surface
        self.position = position
