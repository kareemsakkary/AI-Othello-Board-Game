import pygame
import sys

import GUI.Constants
from GUI.Constants import BLACK
from GUI.Constants import WHITE
from GUI.Constants import SCREEN_WIDTH
from GUI.Constants import SCREEN_HEIGHT


class MainMenuScreen:
    def __init__(self, screen):
        self.screen = screen
        self.background_image = pygame.image.load("assets/images/background.jpeg").convert()
        self.background_image = pygame.transform.scale(self.background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # Load the font for the title
        self.title_font = pygame.font.Font(None, 64)
        self.button_font = pygame.font.Font(None, 36)

        # Load button click sound
        self.click_sound = pygame.mixer.Sound("assets/audio/button_click.mp3")

        # Define button rectangles
        self.button_width = 200
        self.button_height = 50
        self.button_margin = 10
        self.play_rect = pygame.Rect((SCREEN_WIDTH // 2 - self.button_width // 2,
                                      SCREEN_HEIGHT // 2 - self.button_height - self.button_margin, self.button_width,
                                      self.button_height))
        self.settings_rect = pygame.Rect(
            (SCREEN_WIDTH // 2 - self.button_width // 2, SCREEN_HEIGHT // 2, self.button_width, self.button_height))
        self.exit_rect = pygame.Rect((SCREEN_WIDTH // 2 - self.button_width // 2,
                                      SCREEN_HEIGHT // 2 + self.button_height + self.button_margin, self.button_width,
                                      self.button_height))

        # Button colors
        self.default_button_color = (0, 255, 0)
        self.hover_button_color = (0, 200, 0)

    def render(self):
        # Draw background image
        self.screen.blit(self.background_image, (0, 0))

        # Draw title
        title_text = self.title_font.render("SMART OTHELLO", True, WHITE)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        self.screen.blit(title_text, title_rect)

        # Draw buttons with hover effect
        self.draw_rounded_rect(self.screen, self.get_button_color(self.play_rect), self.play_rect,
                               20)  # Increased radius to 20
        self.draw_rounded_rect(self.screen, self.get_button_color(self.settings_rect), self.settings_rect,
                               20)  # Increased radius to 20
        self.draw_rounded_rect(self.screen, self.get_button_color(self.exit_rect), self.exit_rect,
                               20)  # Increased radius to 20

        self.draw_text_in_center("Play", self.play_rect, BLACK)
        self.draw_text_in_center("Settings", self.settings_rect, BLACK)
        self.draw_text_in_center("Exit", self.exit_rect, BLACK)

        pygame.display.flip()

    def get_button_color(self, rect):
        # Check if mouse is over the button
        if rect.collidepoint(pygame.mouse.get_pos()):
            return self.hover_button_color
        else:
            return self.default_button_color

    def draw_rounded_rect(self, surface, color, rect, radius):
        pygame.draw.rect(surface, color, rect, border_radius=radius)

    def draw_text_in_center(self, text, rect, color):
        text_surface = self.button_font.render(text, True, color)
        text_rect = text_surface.get_rect(center=rect.center)
        self.screen.blit(text_surface, text_rect)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # Check if the mouse click is within the button rects
                if self.play_rect.collidepoint(mouse_pos):
                    if GUI.Constants.SOUND:
                        self.click_sound.play()
                    return "GameMode"
                elif self.settings_rect.collidepoint(mouse_pos):
                    if GUI.Constants.SOUND:
                        self.click_sound.play()
                    return "Settings"
                elif self.exit_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()
        return None


# Main function to run the game
# def main():
#     pygame.init()
#     screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#     pygame.display.set_caption("Main Menu Example")
#
#     clock = pygame.time.Clock()
#
#     main_menu_screen = MainMenuScreen(screen)
#
#     # Main game loop
#     while True:
#         events = pygame.event.get()
#
#         # Event handling for the main menu screen
#         main_menu_screen.handle_events(events)
#
#         # Rendering for the main menu screen
#         main_menu_screen.render()
#
#         # Limit frame rate
#         clock.tick(60)
#
#
# if __name__ == "__main__":
#     main()
