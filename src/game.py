import os

import pygame as pg

from classes.base.Coordinate import Coordinate, CoordinateSystem
from classes.base.Drawable import Drawable
from classes.base.Updatable import Updatable
from classes.components.New import New
from classes.components.Quit import Quit

main_dir = os.path.split(os.path.abspath(__file__))[0]


def setup():
    pg.init()

    screen = pg.display.set_mode(flags=pg.FULLSCREEN)
    CoordinateSystem.scale_x = 100 / screen.get_width()
    CoordinateSystem.scale_y = 100 / screen.get_height()

    font = pg.font.Font(os.path.join(
        main_dir, 'graphics/fonts/kongtext/kongtext.ttf'), 24)
    new = New(font, Coordinate(50, 45))
    quit = Quit(font, Coordinate(50, 55))

    return screen, new, quit


def update(*updatables: Updatable):
    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()

        for updatable in updatables:
            updatable.update(e)


def draw(screen: pg.Surface, *drawables: Drawable):
    screen.fill((0, 0, 0))

    for drawable in drawables:
        drawable.draw(screen)

    pg.display.update()


def main():
    screen, new, quit = setup()

    while True:
        update(new, quit)
        draw(screen, new, quit)


if __name__ == "__main__":
    main()
