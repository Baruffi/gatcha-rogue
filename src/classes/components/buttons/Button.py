import pygame as pg
from classes.base.Coordinate import Coordinate
from classes.base.Drawable import CONTOUR
from classes.components.Hoverable import Hoverable


class Button(Hoverable):

    def __init__(self, font: pg.font.Font, button_label: str, coordinate: Coordinate, accent_color: tuple[int, int, int] = (0, 255, 0)):
        surface = font.render(button_label, False, (255, 255, 255), (0, 0, 0))
        surface.set_colorkey((0, 0, 0))

        super().__init__(surface, coordinate.center_on(
            surface), accent_color, pg.MOUSEBUTTONDOWN)

    def click(self):
        pass

    def action(self, event: pg.event.Event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and self.hovered:
            self.click()

    def draw(self, screen: pg.Surface):
        pg.draw.rect(screen, self.surface.get_palette()
                     [1], self.fat_rect, CONTOUR)
        super().draw(screen)
