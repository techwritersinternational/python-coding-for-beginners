import pygame
import random

import constants

CLOUD_MIN_SIZE = 20
CLOUD_MAX_SIZE = 40
CLOUD_SPEED = 3
CLOUD_COLOR = (64, 156, 255)  # Light blue color

class GasCloud:
    def __init__(self):
        self.size = random.randint(CLOUD_MIN_SIZE, CLOUD_MAX_SIZE)
        self.x = constants.WINDOW_WIDTH + self.size
        self.y = random.randint(constants.GAME_MARGIN, constants.WINDOW_HEIGHT - constants.GAME_MARGIN)
        self.speed = random.uniform(2, CLOUD_SPEED)
        
        # Create a surface for the cloud with alpha channel
        self.surface = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        self.create_cloud_appearance()
        
        # Create a hitbox for collision detection
        self.rect = pygame.Rect(self.x, self.y, 
                              self.size * 0.8, self.size * 0.8)

    def create_cloud_appearance(self):
        """Create a swirling cloud effect"""
        center = self.size // 2
        # Draw multiple overlapping circles with different alpha values
        for radius in range(self.size // 2, 0, -2):
            alpha = min(255, radius * 8)
            color = (*CLOUD_COLOR, alpha)
            pygame.draw.circle(self.surface, color, 
                            (center, center), radius)

    def update(self):
        """Move the cloud from right to left"""
        self.x -= self.speed
        # Update hitbox position
        self.rect.x = self.x + self.size * 0.1  # Adjust hitbox to be smaller
        self.rect.y = self.y + self.size * 0.1

    def draw(self, screen):
        """Draw the gas cloud"""
        screen.blit(self.surface, (self.x, self.y))

