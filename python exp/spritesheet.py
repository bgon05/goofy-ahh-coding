import pygame

class SpriteSheet:
    def __init__(self, image):
        self.sheet = image

    def get_image(self, sheet, frame, width, height, scale, color):
        # Extract a single frame from the sprite sheet
        x = frame * width
        y = 0
        frame_image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        frame_image.blit(sheet, (0, 0), (x, y, width, height))
        frame_image = pygame.transform.scale(frame_image, (int(width * scale), int(height * scale)))
        frame_image.set_colorkey(color)
        return frame_image