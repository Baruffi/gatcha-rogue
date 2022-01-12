import pygame as pg
from classes.base.Coordinate import Coordinate
from classes.base.GameObject import GameObject


class Hoverable(GameObject):

    def __init__(self, surface: pg.Surface, coordinate: Coordinate, accent_color: tuple[int, int, int], *event_types: int):
        super().__init__(surface, coordinate, pg.MOUSEMOTION, *event_types)

        self.accent_color = accent_color
        self.hovered = False

    def update(self, e: pg.event.Event):
        mouse_x, mouse_y = pg.mouse.get_pos()

        self.hovered = self.rect.collidepoint(mouse_x, mouse_y)

        super().update(e)

    def draw(self, screen: pg.Surface):
        if self.hovered:
            color = self.accent_color
        else:
            color = (255, 255, 255)

        self.surface.set_palette([(0, 0, 0), color])

        super().draw(screen)
