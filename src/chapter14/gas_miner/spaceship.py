import pygame

import constants

SHIP_WIDTH = 60
SHIP_HEIGHT = 40
SHIP_SPEED = 5

class Spaceship:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 0
        self.acceleration = 0.5
        self.max_velocity = 8
        self.drag = 0.92  # This will create smooth deceleration
        
        # Create a simple spaceship shape
        self.shape = pygame.Surface((SHIP_WIDTH, SHIP_HEIGHT), pygame.SRCALPHA)
        
        # Draw a triangle for the ship
        pygame.draw.polygon(self.shape, constants.WHITE, [
            (0, SHIP_HEIGHT//2),              # Nose of the ship
            (SHIP_WIDTH, SHIP_HEIGHT//4),     # Top back corner
            (SHIP_WIDTH, SHIP_HEIGHT*3//4),   # Bottom back corner
        ])

        self.rect = pygame.Rect(x, y, SHIP_WIDTH * 0.8, SHIP_HEIGHT * 0.8)


    def move(self, direction):
        """Apply movement based on direction (-1 for up, 1 for down)"""
        self.velocity += self.acceleration * direction
        # Limit maximum velocity
        self.velocity = max(min(self.velocity, self.max_velocity), 
                        -self.max_velocity)

    def update(self):
        self.y += self.velocity
        self.velocity *= self.drag
        
        # Keep ship within screen bounds
        self.y = max(constants.GAME_MARGIN, 
                    min(self.y, constants.WINDOW_HEIGHT - constants.GAME_MARGIN - SHIP_HEIGHT))
        
        # Update collision rectangle position
        self.rect.y = self.y + SHIP_HEIGHT * 0.1
        self.rect.x = self.x + SHIP_WIDTH * 0.1

    def draw(self, screen):
        """Draw the ship on the screen"""
        screen.blit(self.shape, (self.x, self.y))

