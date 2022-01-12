import pygame as pg
from classes.base.Coordinate import Coordinate
from classes.components.Button import Button


class Quit(Button):

    def __init__(self, font: pg.font.Font, coordinate: Coordinate):
        super().__init__(font, 'Quit', coordinate, (255, 0, 0))

    def click(self):
        pg.event.post(pg.event.Event(pg.QUIT))
