import pygame as pg
from classes.components.Screen import Screen
from classes.directors.Director import Director


class ScreenDirector(Director):

    def __init__(self, screens: list[Screen], surface: pg.Surface = None):
        super().__init__(surface=surface, updatables=screens, drawables=screens)

    def pre_draw(self):
        self.surface.fill((0, 0, 0))
