import pygame as pg

from classes.Drawable import Drawable
from classes.Updatable import Updatable


class Game():

    def __init__(self, updatables: list[Updatable] = [], drawables: list[Drawable] = []):
        self.updatables = updatables
        self.drawables = drawables

    def update(self, event: pg.event.Event):
        for updatable in self.updatables:
            updatable.update(event)

    def draw(self, screen: pg.Surface):
        for drawable in self.drawables:
            screen.blit(drawable.surface, drawable.position)
