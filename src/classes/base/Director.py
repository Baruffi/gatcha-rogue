import pygame as pg
from classes.base.Drawable import Drawable
from classes.base.Updatable import Updatable


class Director():

    screen: pg.Surface | None = None

    def __init__(self, surface: pg.Surface = None, updatables: list[Updatable] = [], drawables: list[Drawable] = [], *event_types: int):
        if event_types:
            self.get_config = {'eventtype': event_types}
        else:
            self.get_config = {'exclude': (pg.QUIT, pg.USEREVENT)}

        self.surface = surface
        self.updatables = updatables
        self.drawables = drawables

    def should_update(self):
        return True

    def pre_update(self):
        pass

    def post_update(self):
        pass

    def should_draw(self):
        return True

    def pre_draw(self):
        pass

    def post_draw(self):
        pass

    def update(self):
        if self.should_update():
            self.pre_update()

            for e in pg.event.get(**self.get_config):
                for updatable in self.updatables:
                    updatable.update(e)

            self.post_update()

    def draw(self):
        if self.should_draw():
            self.pre_draw()

            for drawable in self.drawables:
                drawable.draw(self.surface or self.screen)

            self.post_draw()
