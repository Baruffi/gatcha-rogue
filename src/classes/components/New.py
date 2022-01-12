import pygame as pg
from classes.base.Coordinate import Coordinate
from classes.components.Button import Button
from classes.components.Menu import Menu


class New(Button):

    def __init__(self, font: pg.font.Font, coordinate: Coordinate):
        super().__init__(font, 'New Game', coordinate, (0, 255, 0))

    def click(self):
        pg.event.post(pg.event.Event(Menu.menu_event, active='new'))
