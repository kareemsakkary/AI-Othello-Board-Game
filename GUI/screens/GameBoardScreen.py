import pygame
import sys

import GUI.Constants
from AI import AI
from GUI.Constants import SCREEN_WIDTH, WHITE, BLACK, SCREEN_HEIGHT, GAME_MODE, SOUND
from Human import Human


class Button:
    def __init__(self, screen, x, y, width, height, text):
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(None, 30)
        self.default_color = (0, 255, 0)
        self.hover_color = (0, 200, 0)
        self.is_hovered = False

    def render(self):
        if self.is_hovered:
            color = self.hover_color
        else:
            color = self.default_color

        pygame.draw.rect(self.screen, color, self.rect, border_radius=5)
        text_surface = self.font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.screen.blit(text_surface, text_rect)

    def check_hover(self, pos):
        self.is_hovered = self.rect.collidepoint(pos)


class GameBoardScreen:
    def __init__(self, screen, board, player_one, player_two):
        self.screen = screen
        self.board = board
        self.player_one = player_one
        self.player_two = player_two
        self.board_size = 8
        self.square_size = 50  # Size of each square in pixels
        self.board_width = self.board_size * self.square_size
        self.board_height = self.board_size * self.square_size
        self.sidebar_width = 200
        self.button_height = 50
        self.click_sound = pygame.mixer.Sound("assets/audio/button_click.mp3")
        self.enemy = ""

        if GUI.Constants.GAME_MODE == 1:
            self.player_two = Human("Enemy", "W")
            self.enemy = "assets/images/man.png"
            print(GUI.Constants.GAME_MODE)
        else:
            self.player_two = AI("Enemy", "W")
            self.enemy = "assets/images/ai.png"

        self.current_player = 1
        self.board.reset()

        # Load and resize images for sidebar
        self.sidebar_top_image = pygame.image.load("assets/images/man.png").convert_alpha()
        self.sidebar_bottom_image = pygame.image.load(self.enemy).convert_alpha()
        self.sidebar_top_image = pygame.transform.scale(self.sidebar_top_image, (150, 150))
        self.sidebar_bottom_image = pygame.transform.scale(self.sidebar_bottom_image, (150, 150))

        # Create button
        self.leave_button = Button(screen, (SCREEN_WIDTH - self.sidebar_width) // 2, SCREEN_HEIGHT - self.button_height - 20,
                                   self.sidebar_width, self.button_height, "Leave")

    def render(self):
        # Load and scale background image
        background_image = pygame.image.load("assets/images/game_mode_background.jpg").convert()
        background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # Draw background image
        self.screen.blit(background_image, (0, 0))

        self.leave_button.render()

        # Draw green background for the board area
        board_background = pygame.Surface((self.board_width, self.board_height))
        board_background.fill((0, 128, 0))
        self.screen.blit(board_background, (0, 0))

        self.draw_board()
        # Draw sidebar
        self.draw_sidebar()

        pygame.display.flip()

    def draw_board(self):
        # Draw squares of the board and Othello chips
        for row in range(self.board_size):
            for col in range(self.board_size):
                rect = pygame.Rect(col * self.square_size, row * self.square_size, self.square_size, self.square_size)
                pygame.draw.rect(self.screen, (0, 128, 0), rect)
                pygame.draw.rect(self.screen, BLACK, rect, 1)  # Draw black border around each cell

                if self.board.boards[row][col].color == "W":  # White piece
                    pygame.draw.circle(self.screen, WHITE, rect.center, self.square_size // 2 - 5)
                elif self.board.boards[row][col].color == "B":  # Black piece
                    pygame.draw.circle(self.screen, BLACK, rect.center, self.square_size // 2 - 5)

    def draw_sidebar(self):
        # Draw top image
        self.screen.blit(self.sidebar_top_image, (SCREEN_WIDTH - self.sidebar_width, 0))

        # Draw bottom image
        self.screen.blit(self.sidebar_bottom_image, (SCREEN_WIDTH - self.sidebar_width, SCREEN_HEIGHT - self.sidebar_width))

        # Draw black chip
        pygame.draw.circle(self.screen, BLACK, (SCREEN_WIDTH - self.sidebar_width + 20, 200), 20)

        # Draw black chip count
        black_chip_text = self.leave_button.font.render(str(self.board.countBlack), True, BLACK)
        black_chip_rect = black_chip_text.get_rect(topright=(SCREEN_WIDTH - self.sidebar_width + 80, 192))
        self.screen.blit(black_chip_text, black_chip_rect)

        # Draw black chip
        pygame.draw.circle(self.screen, WHITE, (SCREEN_WIDTH - self.sidebar_width + 20, 350), 20)

        # Draw black chip count
        black_chip_text = self.leave_button.font.render(str(self.board.countWhite), True, WHITE)
        black_chip_rect = black_chip_text.get_rect(topright=(SCREEN_WIDTH - self.sidebar_width + 80, 340))
        self.screen.blit(black_chip_text, black_chip_rect)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEMOTION:
                self.leave_button.check_hover(event.pos)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.leave_button.is_hovered:
                    if SOUND:
                        self.click_sound.play()
                    return "GameMode"
