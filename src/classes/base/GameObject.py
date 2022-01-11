import pygame as pg
from classes.base.Coordinate import Coordinate
from classes.base.Drawable import Drawable
from classes.base.Updatable import Updatable


class GameObject(Drawable, Updatable):

    def __init__(self, surface: pg.Surface, coordinate: Coordinate, *event_types: int):
        self.surface = surface
        self.coordinate = coordinate
        self.event_types = event_types
