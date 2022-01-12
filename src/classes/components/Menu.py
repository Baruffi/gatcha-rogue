import pygame as pg
from classes.base.Director import Director
from classes.base.Drawable import Drawable
from classes.base.Updatable import Updatable


class Menu(Director):

    menu_event = pg.event.custom_type()

    def __init__(self, name: str, active: bool = False, updatables: list[Updatable] = [], drawables: list[Drawable] = []):
        super().__init__(updatables=updatables, drawables=drawables)

        self.name = name
        self.active = active

    def check_active(self):
        for e in pg.event.get(self.menu_event):
            self.active = e.active == self.name

    def should_update(self):
        self.check_active()

        return self.active

    def should_draw(self):
        return self.active

    def pre_draw(self):
        Director.screen.fill((0, 0, 0))
