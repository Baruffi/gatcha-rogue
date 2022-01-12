import pygame as pg
from classes.base.Coordinate import Coordinate
from classes.components.Button import Button
from classes.directors.ScreenDirector import ScreenDirector


class NavButton(Button):

    def __init__(self, font: pg.font.Font, button_label: str, coordinate: Coordinate, event: pg.event.Event):
        super().__init__(font, button_label, coordinate, (0, 255, 0))

        self.event = event

    def click(self):
        pg.event.post(self.event)
