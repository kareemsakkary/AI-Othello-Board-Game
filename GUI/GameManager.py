import pygame

from GUI.screens.GameModeScreen import GameModeScreen
from GUI.screens.MainMenuScreen import MainMenuScreen
from GUI.screens.SettingsScreen import SettingsScreen
from GUI.screens.GameBoardScreen import GameBoardScreen

from GUI.Constants import SCREEN_WIDTH
from GUI.Constants import SCREEN_HEIGHT


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Smart Othello")

    clock = pygame.time.Clock()
    current_screen = MainMenuScreen(screen)

    # Main game loop
    while True:
        events = pygame.event.get()
        # Event handling for the current screen
        screen_result = current_screen.handle_events(events)

        if screen_result == "GameMode":
            current_screen = GameModeScreen(screen)

        if screen_result == "MainMenu":
            current_screen = MainMenuScreen(screen)

        if screen_result == "Settings":
            current_screen = SettingsScreen(screen)

        if screen_result == "GameBoard":
            current_screen = GameBoardScreen(screen)

        # Rendering for the current screen
        current_screen.render()

        # Limit frame rate
        clock.tick(60)


if __name__ == "__main__":
    main()
