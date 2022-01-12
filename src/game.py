import os

import pygame as pg

from classes.base.Coordinate import Coordinate, CoordinateSystem
from classes.base.Director import Director
from classes.components.NavButton import NavButton
from classes.components.QuitButton import QuitButton
from classes.components.Screen import Screen
from classes.directors.ScreenDirector import ScreenDirector

main_dir = os.path.split(os.path.abspath(__file__))[0]


def setup():
    pg.init()

    screen = pg.display.set_mode(flags=pg.FULLSCREEN)
    CoordinateSystem.scale_x = 100 / screen.get_width()
    CoordinateSystem.scale_y = 100 / screen.get_height()

    font = pg.font.Font(os.path.join(
        main_dir, 'graphics/fonts/kongtext/kongtext.ttf'), 24)
    new = NavButton(font, 'New Game', Coordinate(50, 45),
                    pg.event.Event(ScreenDirector.screen_event, active='new'))
    quit = QuitButton(font, Coordinate(50, 55))
    mainScreen = Screen('main', (new, quit), True)
    newScreen = Screen('new', (quit,))

    directors = ScreenDirector([mainScreen, newScreen]),

    return directors


def update(directors: tuple[Director]):
    if pg.event.peek(pg.QUIT):
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
