import pygame
from pygame.draw import rect

class Cube:
    rows = 9
    cols = 9
    def __init__(self, val, row, col, width, height):
        self.value = val
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def draw_value(self, game):
        fnt = pygame.font.SysFont("calibri", 25)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        if self.temp != 0 and self.value == 0:
            text = fnt.render(str(self.temp), 1, (128,128,128))
            # pre_answered value (grey color)

            game.blit(text, (x+5, y+5))
            #display value on top-corner of cube
        elif not (self.value == 0):
            text = fnt.render(str(self.value), 1, (0,0,0)) 
            # true answer value (black one)
            game.blit(
                text, 
                (
                    x + ((gap - text.get_width())/2), 
                    y + ((gap - text.get_height())/2)
                )
            )
            # display value on corner of cube
        
        if self.selected:
            rect(game, (250, 0, 0), (x,y, gap, gap), 3)
            #hightlight red around the cube
    
    def set_val(self, val):
        self.value = val

    def set_temp(self, val):
        self.temp = val