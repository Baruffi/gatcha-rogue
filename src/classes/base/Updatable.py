import pygame as pg


class Updatable():

    def __init__(self, *event_types: int):
        self.event_types = event_types

    def action(self, e: pg.event.Event):
        pass

    def update(self):
        for e in pg.event.get(self.event_types):
            self.action(e)
