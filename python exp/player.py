import pygame

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 467

class Player(pygame.Surface):

    def __init__(self, size, color=(0, 0, 0), flags=0):
        # Call the parent class constructor
        super().__init__(size, flags)
        self.color = color  # Store the default fill color
        self.fill(self.color) 
        self.x = 100
        self.y = 390

    def update(self):
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0
        if self.x + self.width > SCREEN_WIDTH:
            self.x = SCREEN_WIDTH - self.width
        if self.y + self.height > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - self.height
            