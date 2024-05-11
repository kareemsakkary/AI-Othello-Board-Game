from Controller import Controller
import pygame

from GUI.screens.GameModeScreen import GameModeScreen
from GUI.screens.MainMenuScreen import MainMenuScreen
from GUI.screens.SettingsScreen import SettingsScreen
from GUI.screens.GameBoardScreen import GameBoardScreen

from GUI.Constants import SCREEN_WIDTH
from GUI.Constants import SCREEN_HEIGHT


class GUIController(Controller):
    def __init__(self):
        super().__init__()
        pygame.init()
        pygame.display.set_caption("Smart Othello")

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.current_screen = MainMenuScreen(self.screen)
        self.difficulty = 1

    def display_ui(self, player=None):
        events = pygame.event.get()
        # Event handling for the current screen
        screen_result = self.current_screen.handle_events(events)
        if screen_result == "GameMode":
            self.current_screen = GameModeScreen(self.screen)

        if screen_result == "MainMenu":
            self.current_screen = MainMenuScreen(self.screen)

        if screen_result == "Settings":
            self.current_screen = SettingsScreen(self.screen)

        if screen_result == "GameBoard":
            self.current_screen = GameBoardScreen(self.screen, self.board, self.player2)

        # Rendering for the current screen
        self.current_screen.render()

        # Limit frame rate
        self.clock.tick(60)

    def play_game(self):
        while True:
            self.display_ui()


def main():
    gui = GUIController()
    gui.play_game()


if __name__ == "__main__":
    main()