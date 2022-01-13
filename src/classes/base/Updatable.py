import pygame as pg


class Updatable():

    def __init__(self, *event_types: int):
        self.event_types = event_types

    def action(self, event: pg.event.Event):
        pass

    def update(self, event: pg.event.Event):
        if event.type in self.event_types:
            self.action(event)
