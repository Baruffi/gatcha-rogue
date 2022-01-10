import pygame as pg
from classes.components.Button import Button


class Quit(Button):

    def __init__(self, font: pg.font.Font):
        super().__init__(font, 'X', (1000, 0))

    def click(self):
        pg.quit()
