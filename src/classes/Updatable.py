import pygame as pg


class EmptyUpdatable():

    def update(self, event: pg.event.Event):
        pass


class Updatable(EmptyUpdatable):

    def __init__(self, children: list[EmptyUpdatable] = []):
        self.children = children

    def update(self, event: pg.event.Event):
        for child in self.children:
            child.update(event)
