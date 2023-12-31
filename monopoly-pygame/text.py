import string
import pygame
class Text:
    def __init__(self, text, x=0, y=0, color=(255, 255, 255), size=25):
        font = pygame.font.Font(None, size)
        self.surface = font.render(text, True, color)
        self.text_string = text
        self.x = x
        self.y = y

    def draw(self, WIN):
        WIN.blit(self.surface, (self.x, self.y))