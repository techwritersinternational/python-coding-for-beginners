import pygame

import constants

# Add to your constants
DEBUG_MODE = False  # Set to True when testing

class DebugTools:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font(size=24)
        self.show_hitboxes = False
        self.show_fps = True

    def toggle_hitboxes(self):
        """Toggle hitbox visibility"""
        self.show_hitboxes = not self.show_hitboxes
    
    def draw_hitboxes(self):
        """Draw hitboxes for game objects"""
        if not self.show_hitboxes:
            return
            
        # Draw ship hitbox
        pygame.draw.rect(self.game.screen, (255, 0, 0), 
                        self.game.player.rect, 1)
        
        # Draw cloud hitboxes
        for cloud in self.game.clouds:
            pygame.draw.rect(self.game.screen, (0, 255, 0), 
                           cloud.rect, 1)

    def draw_debug_info(self):
        """Draw debug information"""
        debug_info = [
            f"FPS: {int(self.game.clock.get_fps())}",
            f"Clouds: {len(self.game.clouds)}",
            f"Player pos: ({int(self.game.player.x)}, {int(self.game.player.y)})",
            f"Game State: {self.game.state.name}"
        ]
            
        for i, text in enumerate(debug_info):
            surface = self.font.render(text, True, (255, 255, 0))
            self.game.screen.blit(surface, (10, constants.WINDOW_HEIGHT - 30 * (len(debug_info) - i)))

