import pygame
import sys
import random

# Add to your constants
from enum import Enum

from spaceship import Spaceship 
from gas_cloud import GasCloud, CLOUD_COLOR
from high_score_manager import HighScoreManager
from debug_tools import DebugTools

pygame.init()

DEBUG_MODE = True  # Set to True when testing

# Define constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Add these to your constants at the top of the file
STAR_COUNT = 50
STAR_SPEED = 2
STAR_SIZE = 2

CLOUD_SPAWN_RATE = 60  # New cloud every 60 frames

class GameState(Enum):
    START = 1
    PLAYING = 2
    GAME_OVER = 3

# Add these constants
GAME_DURATION = 10  # Game length in seconds
TITLE_FONT_SIZE = 64
MENU_FONT_SIZE = 32

# Create game class
class GasMiner:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Gas Miner")
        self.clock = pygame.time.Clock()
        self.running = True
        self.stars = self.create_stars()
        
        # Create the player's spaceship
        start_x = WINDOW_WIDTH // 4
        start_y = WINDOW_HEIGHT // 2
        self.player = Spaceship(start_x, start_y)

        self.clouds = []
        self.cloud_spawn_timer = 0
        self.score = 0

        self.state = GameState.START
        self.game_time = 0
        self.time_remaining = GAME_DURATION
        
        # Initialize fonts
        self.title_font = pygame.font.Font(size=TITLE_FONT_SIZE)
        self.menu_font = pygame.font.Font(size=MENU_FONT_SIZE)

        self.high_score_manager = HighScoreManager()
        self.is_new_high_score = False

        self.debug = DebugTools(self)

    def handle_debug_keys(self):
        """Handle debug keyboard shortcuts"""
        if not DEBUG_MODE:
            return
            
        keys = pygame.key.get_pressed()

        if keys[pygame.K_h]:  # Toggle hitboxes
            self.debug.toggle_hitboxes()
        elif keys[pygame.K_l]:  # Add 10 seconds
            self.time_remaining += 10
    
    def reset_game(self):
        """Reset the game to initial state"""
        self.score = 0
        self.clouds = []
        self.collection_particles = []
        self.cloud_spawn_timer = 0
        self.time_remaining = GAME_DURATION
        self.player.y = WINDOW_HEIGHT // 2
        self.player.velocity = 0
        self.is_new_high_score = False

    def end_game(self):
        """Handle end of game logic"""
        self.state = GameState.GAME_OVER
        self.is_new_high_score = self.high_score_manager.add_score(self.score)


    def check_collisions(self):
        """Check for collisions between ship and clouds"""
        for cloud in self.clouds[:]:
            if self.player.rect.colliderect(cloud.rect):
                # Calculate score based on cloud size
                points = int(cloud.size / 2)
                self.score += points
                
                # Remove collected cloud
                self.clouds.remove(cloud)

    def spawn_cloud(self):
        """Create a new gas cloud"""
        self.clouds.append(GasCloud())

    def update_clouds(self):
        """Update all clouds and remove ones that are off screen"""
        # Spawn new clouds
        self.cloud_spawn_timer += 1
        if self.cloud_spawn_timer >= CLOUD_SPAWN_RATE:
            self.spawn_cloud()
            self.cloud_spawn_timer = 0

        # Update existing clouds
        for cloud in self.clouds[:]:
            cloud.update()
            # Remove clouds that have moved off screen
            if cloud.x + cloud.size < 0:
                self.clouds.remove(cloud)

    def handle_input(self):
        """Handle input based on game state"""
        keys = pygame.key.get_pressed()
        
        if self.state == GameState.PLAYING:
            # Normal gameplay controls
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                self.player.move(-1)
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.player.move(1)

    def draw_start_screen(self):
        """Draw the start screen"""
        # Draw title
        title_text = self.title_font.render("Gas Miner", True, WHITE)
        title_rect = title_text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//3))
        
        # Draw instructions
        instruction_text = self.menu_font.render(
            f"Collect gas clouds in {GAME_DURATION} seconds!", True, WHITE)
        instruction_rect = instruction_text.get_rect(
            center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2))
        
        start_text = self.menu_font.render(
            "Press SPACE to start", True, WHITE)
        start_rect = start_text.get_rect(
            center=(WINDOW_WIDTH//2, WINDOW_HEIGHT*2//3))
        
        # Draw everything
        self.screen.blit(title_text, title_rect)
        self.screen.blit(instruction_text, instruction_rect)
        
        # Make the "Press SPACE" text pulse
        if pygame.time.get_ticks() % 1000 < 500:
            self.screen.blit(start_text, start_rect)

    def draw_game_over_screen(self):
        """Draw the game over screen"""
        # Draw "Game Over"
        title_text = self.title_font.render("Game Over!", True, WHITE)
        title_rect = title_text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//4))

        # Draw final score
        score_text = self.menu_font.render(
            f"Final Score: {self.score}", True, WHITE)
        
        score_rect = score_text.get_rect(
            center=(WINDOW_WIDTH//2, title_rect.bottom + 10))

        self.draw_high_scores(score_rect.bottom + 10)

        # Draw restart instruction
        restart_text = self.menu_font.render(
            "Press SPACE to play again", True, WHITE)
        restart_rect = restart_text.get_rect(
            center=(WINDOW_WIDTH//2, WINDOW_HEIGHT*2//3))
        
        # Draw everything
        self.screen.blit(title_text, title_rect)
        self.screen.blit(score_text, score_rect)
        
        # Make the "Press SPACE" text pulse
        if pygame.time.get_ticks() % 1000 < 500:
            self.screen.blit(restart_text, restart_rect)

    def update_game_state(self):
        """Update game state based on time and events"""
        if self.state == GameState.PLAYING:
            self.time_remaining -= 1/FPS
            if self.time_remaining <= 0:
                self.end_game()

    def draw_high_scores(self, top_y):
        """Draw the high score list"""
        title_text = self.menu_font.render("High Scores:", True, CLOUD_COLOR)
        title_rect = title_text.get_rect(
            center=(WINDOW_WIDTH//2, top_y))
        self.screen.blit(title_text, title_rect)

        for i, score_data in enumerate(self.high_score_manager.high_scores):
            score_text = self.menu_font.render(
                f"{i+1}. {score_data['score']} - {score_data['date']}", 
                True, WHITE)
            score_rect = score_text.get_rect(
                center=(WINDOW_WIDTH//2, top_y + (i+1) * 30))
            self.screen.blit(score_text, score_rect)


    def draw_hud(self):
        """Draw the in-game HUD with score and time"""
        # Draw score
        score_text = self.menu_font.render(
            f'Gas Collected: {self.score}', True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        # Draw time remaining
        time_text = self.menu_font.render(
            f'Time: {int(self.time_remaining)}s', True, WHITE)
        time_rect = time_text.get_rect(topright=(WINDOW_WIDTH - 10, 10))
        self.screen.blit(time_text, time_rect)


    def create_stars(self):
        """Create a list of star positions for the background"""
        stars = []
        for _ in range(STAR_COUNT):
            x = random.randint(0, WINDOW_WIDTH)
            y = random.randint(0, WINDOW_HEIGHT)
            speed = random.uniform(0.5, STAR_SPEED)
            stars.append({'x': x, 'y': y, 'speed': speed})
        return stars

    def update_stars(self):
        """Update star positions for the parallax effect"""
        for star in self.stars:
            # Move stars from right to left
            star['x'] -= star['speed']
            # If star moves off screen, reset it to the right
            if star['x'] < 0:
                star['x'] = WINDOW_WIDTH
                star['y'] = random.randint(0, WINDOW_HEIGHT)

    def draw_stars(self):
        """Draw stars on the screen"""
        for star in self.stars:
            pygame.draw.circle(
                self.screen, 
                WHITE, 
                (int(star['x']), int(star['y'])), 
                STAR_SIZE
            )
       
    def run(self):
        while self.running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.state == GameState.START:
                            self.state = GameState.PLAYING
                            self.reset_game()
                        elif self.state == GameState.GAME_OVER:
                            self.state = GameState.START

            # Clear screen and draw stars (for all states)
            self.screen.fill(BLACK)
            self.update_stars()
            self.draw_stars()

            # State-specific updates and drawing
            if self.state == GameState.PLAYING:
                # Game updates
                self.handle_input()
                if DEBUG_MODE:
                    self.handle_debug_keys()
                    self.debug.draw_hitboxes()
                    self.debug.draw_debug_info()

                self.player.update()
                self.update_clouds()
                self.check_collisions()
                self.update_game_state()

                # Game drawing
                for cloud in self.clouds:
                    cloud.draw(self.screen)
                self.player.draw(self.screen)
                self.draw_hud()

            elif self.state == GameState.START:
                self.draw_start_screen()

            elif self.state == GameState.GAME_OVER:
                self.draw_game_over_screen()

            pygame.display.flip()
            self.clock.tick(FPS)


# Create and run game
if __name__ == "__main__":
    game = GasMiner()
    game.run()
    pygame.quit()
    sys.exit()