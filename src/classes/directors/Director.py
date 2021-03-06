import pygame as pg
from classes.base.Drawable import Drawable
from classes.base.Updatable import Updatable


class Director():

    def __init__(self, *event_types: int, surface: pg.Surface = None, updatables: list[Updatable] = [], drawables: list[Drawable] = []):
        if event_types:
            self.get_config = {'eventtype': event_types}
        else:
            self.get_config = {'exclude': (pg.QUIT, pg.USEREVENT)}

        self.surface = surface or pg.display.get_surface()
        self.updatables = updatables
        self.drawables = drawables

    def pre_update(self):
        pass

    def post_update(self):
        pass

    def pre_draw(self):
        pass

    def post_draw(self):
        pass

    def update(self):
        self.pre_update()

        if self.updatables and (events := pg.event.get(**self.get_config)):
            for event in events:
                for updatable in self.updatables:
                    updatable.update(event)

            self.post_update()

    def draw(self):
        self.pre_draw()

        if self.drawables:
            for drawable in self.drawables:
                drawable.draw(self.surface)

            self.post_draw()
