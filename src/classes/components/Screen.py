import pygame as pg
from classes.base.GameObject import GameObject
from classes.directors.ScreenDirector import ScreenDirector


class Screen(GameObject):

    def __init__(self, name: str, screenItems: list[GameObject], active: bool = False):
        super().__init__(pg.Surface(pg.display.get_surface().get_size()),
                         (0, 0), ScreenDirector.screen_event)

        self.name = name
        self.active = active
        self.screenItems = screenItems

    def action(self, e: pg.event.Event):
        self.active = e.active == self.name

    def update(self, e: pg.event.Event):
        super().update(e)

        if self.active:
            for screenItem in self.screenItems:
                screenItem.update(e)

    def draw(self, screen: pg.Surface):
        if self.active:
            for screenItem in self.screenItems:
                screenItem.draw(screen)
