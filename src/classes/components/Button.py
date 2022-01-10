import pygame as pg
from classes.base.GameObject import GameObject


class Button(GameObject):

    def __init__(self, font: pg.font.Font, button_label: str, button_pos: tuple[int, int]):
        surface = font.render(button_label, False, (255, 255, 255), (0, 0, 0))
        super().__init__(surface, button_pos, pg.MOUSEBUTTONDOWN)

    def click(self):
        pass

    def action(self, e: pg.event.Event):
        if e.type == pg.MOUSEBUTTONDOWN and e.button == 1:
            mouse_x, mouse_y = pg.mouse.get_pos()

            if self.rect.collidepoint(mouse_x, mouse_y):
                self.click()

    def draw(self, screen: pg.Surface):
        pg.draw.rect(screen, (255, 255, 255), self.fat_rect, 10)
        super().draw(screen)
