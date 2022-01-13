import pygame as pg
from classes.base.GameObject import GameObject


class Screen(GameObject):

    screen_event = pg.event.custom_type()

    def __init__(self, name: str, screenItems: list[GameObject], active: bool = False):
        super().__init__(pg.Surface(pg.display.get_surface().get_size()), (0, 0), self.screen_event)

        self.name = name
        self.active = active
        self.screenItems = screenItems

    def action(self, event: pg.event.Event):
        self.active = event.active == self.name

    def update(self, event: pg.event.Event):
        super().update(event)

        if self.active:
            for screenItem in self.screenItems:
                screenItem.update(event)

    def draw(self, surface: pg.Surface):
        if self.active:
            for screenItem in self.screenItems:
                screenItem.draw(surface)
