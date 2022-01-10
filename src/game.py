import os

import pygame as pg

from classes.Drawable import Drawable
from classes.Game import Game

main_dir = os.path.split(os.path.abspath(__file__))[0]


def setup():
    pg.init()

    screen = pg.display.set_mode(flags=pg.FULLSCREEN)

    font = pg.font.Font(os.path.join(
        main_dir, 'graphics/fonts/kongtext/kongtext.ttf'), 24)
    game = Game(drawables=[Drawable(font.render(
        'SAMPLE TEXT', False, (255, 255, 255), (0, 0, 0)), (0, 0))])

    return screen, game


def update(game: Game):
    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()

        if e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE:
            # TODO: confirm escape
            pg.quit()

        game.update(e)


def draw(screen: pg.Surface, game: Game):
    screen.fill((0, 0, 0))

    game.draw(screen)

    pg.display.update()


def main():
    screen, game = setup()

    while True:
        update(game)
        draw(screen, game)


if __name__ == "__main__":
    main()
