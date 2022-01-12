from __future__ import annotations

from typing import TYPE_CHECKING

import pygame as pg
from classes.base.Director import Director

if TYPE_CHECKING:
    from classes.components.Screen import Screen


class ScreenDirector(Director):

    screen_event = pg.event.custom_type()

    def __init__(self, screens: list[Screen], surface: pg.Surface = None):
        super().__init__(surface, screens, screens)

    def pre_draw(self):
        self.surface.fill((0, 0, 0))
