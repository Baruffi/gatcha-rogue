import pygame as pg
from classes.base.Drawable import Drawable
from classes.base.Updatable import Updatable


class GameObject(Drawable, Updatable):

    def __init__(self, surface: pg.Surface, position: tuple[int, int], *event_types: int):
        self.surface = surface
        self.position = position
        self.event_types = event_types
