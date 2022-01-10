import os

import pygame as pg

from classes.base.Drawable import Drawable
from classes.base.Updatable import Updatable
from classes.components.Quit import Quit

main_dir = os.path.split(os.path.abspath(__file__))[0]


def setup():
    pg.init()

    screen = pg.display.set_mode(flags=pg.FULLSCREEN)

    font = pg.font.Font(os.path.join(
        main_dir, 'graphics/fonts/kongtext/kongtext.ttf'), 24)
    quit = Quit(font)

    return screen, quit


def update(*updatables: Updatable):
    for e in pg.event.get(pg.QUIT):
        if e.type == pg.QUIT:
            pg.quit()

    for updatable in updatables:
        updatable.update()


def draw(screen: pg.Surface, *drawables: Drawable):
    screen.fill((0, 0, 0))

    for drawable in drawables:
        drawable.draw(screen)

    pg.display.update()


def main():
    screen, quit = setup()

    while True:
        update(quit)
        draw(screen, quit)


if __name__ == "__main__":
    main()
