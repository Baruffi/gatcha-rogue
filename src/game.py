import os

import pygame as pg

from classes.base.Coordinate import Coordinate, CoordinateSystem
from classes.base.Director import Director
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

    Director.screen = screen
    directors = Director(updatables=[new, quit], drawables=[new, quit]),

    return directors


def update(directors: tuple[Director]):
    if pg.event.get(pg.QUIT):
        return False

    for director in directors:
        director.update()

    return True


def draw(directors: tuple[Director]):
    for director in directors:
        director.draw()

    pg.display.update()


def main():
    directors = setup()

    while update(directors):
        draw(directors)


if __name__ == "__main__":
    main()
