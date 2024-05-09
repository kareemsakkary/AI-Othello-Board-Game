import pygame
import sys

import GUI.Constants
from GUI.screens.GameModeScreen import BackToMainMenuButton
from GUI.Constants import BLACK
from GUI.Constants import WHITE
from GUI.Constants import SCREEN_HEIGHT
from GUI.Constants import SCREEN_WIDTH

class SettingsScreen:
    def __init__(self, screen):
        self.screen = screen
        self.background_color = (150, 150, 150)
        self.background_image = pygame.image.load("assets/images/game_mode_background.jpg").convert()
        self.background_image = pygame.transform.scale(self.background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.title_font = pygame.font.Font(None, 64)
        self.option_font = pygame.font.Font(None, 36)
        self.click_sound = pygame.mixer.Sound("assets/audio/button_click.mp3")
        # Sound option
        self.sound_option = ToggleOption(screen, 100, 200, "Sound", ["On", "Off"])
        self.sound_option.current_option_index = (GUI.Constants.SOUND is not True)

        # Difficulty option
        self.difficulty_title_text = self.title_font.render("Game Difficulty", True, BLACK)
        self.difficulty_title_rect = self.difficulty_title_text.get_rect(center=(SCREEN_WIDTH // 2, 300))
        self.difficulty_option = RadioOption(screen, 100, 400, ["Easy", "Medium", "Hard"])
        self.difficulty_option.selected_index = GUI.Constants.DIFFICULTY - 1

        self.back_button = BackToMainMenuButton(screen)

    def render(self):
        self.screen.blit(self.background_image, (0, 0))

        # Title
        title_text = self.title_font.render("Settings", True, BLACK)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 100))
        self.screen.blit(title_text, title_rect)

        # Sound option
        self.sound_option.render()

        # Difficulty title
        self.screen.blit(self.difficulty_title_text, self.difficulty_title_rect)

        # Difficulty option
        self.difficulty_option.render()

        # Back button
        self.back_button.render()

        pygame.display.flip()

    def sound_enabled(self):
        return self.sound_option.current_option_index == 0

    def get_difficulty_option(self):
        return self.difficulty_option.selected_index + 1

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:

                if self.sound_option.is_clicked(event.pos):
                    self.sound_option.toggle()
                    GUI.Constants.SOUND = self.sound_enabled()
                elif self.difficulty_option.is_clicked(event.pos):
                    self.difficulty_option.handle_click(event.pos)
                    GUI.Constants.DIFFICULTY = self.get_difficulty_option()

                elif self.back_button.is_clicked(event.pos):
                    if GUI.Constants.SOUND:
                        self.click_sound.play()
                    # Go back to the main menu
                    return "MainMenu"

class ToggleOption:
    def __init__(self, screen, x, y, name, options):
        self.screen = screen
        self.x = x
        self.y = y
        self.name = name
        self.options = options
        self.current_option_index = 0
        self.font = pygame.font.Font(None, 36)

    def render(self):
        text_surface = self.font.render(self.name + ": " + self.options[self.current_option_index], True, WHITE)
        self.screen.blit(text_surface, (self.x, self.y))

    def is_clicked(self, pos):
        text_rect = self.font.render(self.name + ": " + self.options[self.current_option_index], True, WHITE).get_rect(topleft=(self.x, self.y))
        return text_rect.collidepoint(pos)

    def toggle(self):
        self.current_option_index = (self.current_option_index + 1) % len(self.options)


class RadioOption:
    def __init__(self, screen, x, y, options):
        self.screen = screen
        self.x = x
        self.y = y
        self.options = options
        self.selected_index = 0
        self.font = pygame.font.Font(None, 36)

    def render(self):
        for i, option in enumerate(self.options):
            text_surface = self.font.render(option, True, WHITE)
            text_rect = text_surface.get_rect(topleft=(self.x + 50, self.y + i * 40))
            self.screen.blit(text_surface, text_rect)
            pygame.draw.circle(self.screen, (255, 255, 255), (self.x + 10, self.y + i * 40 + 12), 10, 2)
            if i == self.selected_index:
                pygame.draw.circle(self.screen, (255, 255, 255), (self.x + 10, self.y + i * 40 + 12), 5)

    def is_clicked(self, pos):
        for i in range(len(self.options)):
            circle_center = (self.x + 10, self.y + i * 40 + 12)
            if pygame.math.Vector2(circle_center).distance_to(pos) <= 10:
                return True
        return False

    def handle_click(self, pos):
        for i in range(len(self.options)):
            circle_center = (self.x + 10, self.y + i * 40 + 12)
            if pygame.math.Vector2(circle_center).distance_to(pos) <= 10:
                self.selected_index = i


class Button:
    def __init__(self, screen, x, y, width, height, text):
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(None, 30)
        self.default_color = (0, 255, 0)
        self.hover_color = (0, 200, 0)

    def render(self):
        pygame.draw.rect(self.screen, self.default_color, self.rect, border_radius=5)
        text_surface = self.font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


