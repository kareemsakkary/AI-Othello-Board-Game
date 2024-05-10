import pygame
import sys

import GUI.Constants
from AI import AI
from GUI.Constants import BLACK
from GUI.Constants import WHITE
from GUI.Constants import SCREEN_WIDTH
from GUI.Constants import SCREEN_HEIGHT
from Human import Human


class GameModeScreen:
    def __init__(self, screen):
        self.screen = screen
        self.background_image = pygame.image.load("GUI/assets/images/game_mode_background.jpg").convert()
        self.background_image = pygame.transform.scale(self.background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.back_button = BackToMainMenuButton(screen)
        self.click_sound = pygame.mixer.Sound("GUI/assets/audio/button_click.mp3")
        self.game_start_sound = pygame.mixer.Sound("GUI/assets/audio/board_start.mp3")
        self.title_font = pygame.font.Font(None, 64)
        player1 = Human("Human", "B")

        # Create square buttons
        button_width = 150
        button_height = 150
        button_x = (SCREEN_WIDTH - button_width * 2) // 3
        button_y = (SCREEN_HEIGHT - button_height) // 2
        self.human_button = SquareButton(screen, button_x, button_y, button_width, button_height,
                                         "GUI/assets/images/man.png", "Human")
        self.ai_button = SquareButton(screen, button_x * 2 + button_width, button_y, button_width, button_height,
                                      "GUI/assets/images/ai.png", "AI")

    def render(self):
        # Draw background image
        self.screen.blit(self.background_image, (0, 0))

        # Draw title
        title_text = self.title_font.render("Game Mode Selection", True, WHITE)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        self.screen.blit(title_text, title_rect)

        # Draw buttons
        self.human_button.render()
        self.ai_button.render()

        # Draw back button
        self.back_button.render()

        pygame.display.flip()

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.human_button.is_clicked(mouse_pos):
                    if GUI.Constants.SOUND:
                        self.game_start_sound.play()

                    self.player2 = Human("Human", "W")
                    GUI.Constants.GAME_MODE = 1
                    return "GameBoard"
                elif self.ai_button.is_clicked(mouse_pos):
                    if GUI.Constants.SOUND:
                        self.game_start_sound.play()

                    self.player2 = AI("AI", "W", GUI.Constants.DIFFICULTY)
                    print("Setting player 2 to", self.player2)
                    GUI.Constants.GAME_MODE = 2
                    return "GameBoard"
                elif self.back_button.is_clicked(mouse_pos):
                    if GUI.Constants.SOUND:
                        self.click_sound.play()
                    return "MainMenu"


class SquareButton:
    def __init__(self, screen, x, y, width, height, image_path, text):
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.text = text

    def render(self):
        # Draw image
        image_rect = self.image.get_rect(center=self.rect.center)
        self.screen.blit(self.image, image_rect)

        # Draw text
        font = pygame.font.Font(None, 24)
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=(self.rect.centerx, self.rect.bottom + 20))
        self.screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


class BackToMainMenuButton:
    def __init__(self, screen):
        self.screen = screen
        self.rect = pygame.Rect(10, SCREEN_HEIGHT - 60, 220, 50)
        self.default_button_color = (0, 255, 0)
        self.hover_button_color = (0, 200, 0)
        self.font = pygame.font.Font(None, 24)
        self.text = "Back to Main Menu"

        # Load the arrow image
        self.arrow_image = pygame.image.load("GUI/assets/images/arrow.png").convert_alpha()
        self.arrow_image = pygame.transform.scale(self.arrow_image, (30, 30))  # Adjust size as needed

    def render(self):
        # Draw button rectangle
        pygame.draw.rect(self.screen, self.get_button_color(), self.rect, border_radius=20)

        # Draw arrow image
        arrow_rect = self.arrow_image.get_rect(left=self.rect.left + 10, centery=self.rect.centery)
        self.screen.blit(self.arrow_image, arrow_rect)

        # Draw text
        text_surface = self.font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(left=arrow_rect.right + 5, centery=self.rect.centery)
        self.screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def get_button_color(self):
        # Check if mouse is over the button
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return self.hover_button_color
        else:
            return self.default_button_color
