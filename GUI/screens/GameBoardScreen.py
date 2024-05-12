import pygame
import sys

import GUI.Constants
from GUI.Constants import SCREEN_WIDTH, WHITE, BLACK, SCREEN_HEIGHT, GREEN
from GUI.screens.AlertScreen import AlertScreen
from Human import Human
from AI import AI



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
    def __init__(self, screen, board, players):
        self.screen = screen
        self.board = board
        self.board_size = 8
        self.square_size = 50  # Size of each square in pixels
        self.board_width = self.board_size * self.square_size
        self.board_height = self.board_size * self.square_size
        self.sidebar_width = 200
        self.button_height = 50
        self.click_sound = pygame.mixer.Sound("GUI/assets/audio/button_click.mp3")
        self.enemy = ""
        self.players = [None, None]
        self.current_player = 0
        self.alert_screen = None
        self.board.reset()

        if GUI.Constants.GAME_MODE == 1:
            self.players[0] = Human("Human", "B")
            self.players[1] = Human("Enemy", "W")
            self.enemy = "GUI/assets/images/man.png"
        else:
            if GUI.Constants.START_COLOR == 1:
                self.players[0] = Human("Human", "B")
                self.players[1] = AI("Enemy", "W", GUI.Constants.DIFFICULTY)

            else:
                self.players[0] = AI("Enemy", "B", GUI.Constants.DIFFICULTY)
                self.players[1] = Human("Human", "W")
            self.enemy = "GUI/assets/images/ai.png"

        # Load and resize images for sidebar
        self.sidebar_top_image = pygame.image.load("GUI/assets/images/man.png").convert_alpha()
        self.sidebar_bottom_image = pygame.image.load(self.enemy).convert_alpha()
        self.sidebar_top_image = pygame.transform.scale(self.sidebar_top_image, (150, 150))
        self.sidebar_bottom_image = pygame.transform.scale(self.sidebar_bottom_image, (150, 150))

        # Create button
        self.leave_button = Button(screen, (SCREEN_WIDTH - self.sidebar_width) // 2,
                                   SCREEN_HEIGHT - self.button_height - 20,
                                   self.sidebar_width, self.button_height, "Leave")

    def render(self):
        # Load and scale background image
        background_image = pygame.image.load("GUI/assets/images/game_mode_background.jpg").convert()
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



        if self.alert_screen:
            self.alert_screen.render()



        pygame.display.flip()

    def draw_board(self):
        # Draw squares of the board and Othello chips
        valid_moves = self.board.valid_moves(self.players[self.current_player])

        for row in range(self.board_size):
            for col in range(self.board_size):
                rect = pygame.Rect(col * self.square_size, row * self.square_size, self.square_size, self.square_size)
                pygame.draw.rect(self.screen, (0, 128, 0), rect)
                pygame.draw.rect(self.screen, BLACK, rect, 1)  # Draw black border around each cell

                if self.board.board[row][col].color == "W":  # White piece
                    pygame.draw.circle(self.screen, WHITE, rect.center, self.square_size // 2 - 5)
                elif self.board.board[row][col].color == "B":  # Black piece
                    pygame.draw.circle(self.screen, BLACK, rect.center, self.square_size // 2 - 5)
                elif self.board.board[row][col] in valid_moves and isinstance(self.players[self.current_player], Human):
                    pygame.draw.circle(self.screen, GREEN, rect.center, self.square_size // 2 - 5)

    def draw_sidebar(self):
        # Draw top image

        black_chip_text_y = 192
        black_chip_circle_y = 200

        white_chip_text_y = 340
        while_chip_circle_y = 350

        if GUI.Constants.START_COLOR == 2:
            black_chip_text_y, white_chip_text_y = white_chip_text_y, black_chip_text_y
            black_chip_circle_y, while_chip_circle_y = while_chip_circle_y, black_chip_circle_y


        self.screen.blit(self.sidebar_top_image, (SCREEN_WIDTH - self.sidebar_width, 0))

        # Draw bottom image
        self.screen.blit(self.sidebar_bottom_image,
                         (SCREEN_WIDTH - self.sidebar_width, SCREEN_HEIGHT - self.sidebar_width))

        # Draw black chip
        pygame.draw.circle(self.screen, BLACK, (SCREEN_WIDTH - self.sidebar_width + 20, black_chip_circle_y), 20)

        # Draw black chip count
        black_chip_text = self.leave_button.font.render(str(self.board.countBlack), True, BLACK)
        black_chip_rect = black_chip_text.get_rect(topright=(SCREEN_WIDTH - self.sidebar_width + 80, black_chip_text_y))
        self.screen.blit(black_chip_text, black_chip_rect)

        # Draw WHITE chip
        pygame.draw.circle(self.screen, WHITE, (SCREEN_WIDTH - self.sidebar_width + 20, while_chip_circle_y), 20)

        # Draw WHITE chip count
        white_chip_text = self.leave_button.font.render(str(self.board.countWhite), True, WHITE)
        white_chip_rect = white_chip_text.get_rect(topright=(SCREEN_WIDTH - self.sidebar_width + 80, white_chip_text_y))
        self.screen.blit(white_chip_text, white_chip_rect)

    def force_switch(self):
        return len(self.board.valid_moves(self.players[self.current_player])) == 0

    def game_over(self):
        valid1 = self.board.valid_moves(self.players[0])
        valid2 = self.board.valid_moves(self.players[1])
        return len(valid1) == 0 and len(valid2) == 0

    def handle_events(self, events):
        if self.alert_screen:  # Handle events for alert screen if exists
            if self.alert_screen.handle_events(events):
                self.alert_screen = None
                self.render()
            else:
                return


        if self.game_over():
            message = "Game Over Black Wins" if self.board.countBlack > self.board.countWhite else "Game Over White Wins"
            self.alert_screen = AlertScreen(self.screen, message)  # Create alert screen for game over
            self.board.reset()
            self.current_player = 0
            return

        if self.force_switch():
            message = "Player 1 plays again" if self.current_player == 1 else "Player 2 plays again"
            self.alert_screen = AlertScreen(self.screen, message)  # Create alert screen for switching player
            self.current_player = (self.current_player + 1) % 2
            return

        if GUI.Constants.GAME_MODE == 2:
            if self.current_player != GUI.Constants.START_COLOR - 1:
                move = self.players[self.current_player].play_move(self.board)
                if move:
                    # Mark the spot chosen by AI with blue color
                    pygame.draw.circle(self.screen, (0, 0, 255), (move.y * self.square_size + self.square_size // 2,
                                                                  move.x * self.square_size + self.square_size // 2),
                                       self.square_size // 2 - 5)

                    pygame.display.flip()
                    pygame.time.wait(2000)  # Add a delay of 2 seconds
                    self.board.make_move(self.players[self.current_player], move)
                self.current_player = (self.current_player + 1) % 2



        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEMOTION:
                self.leave_button.check_hover(event.pos)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.leave_button.is_hovered:
                    if GUI.Constants.SOUND:
                        self.click_sound.play()
                    return "GameMode"

                # Check if mouse clicked on any board cell
                if event.button == 1:  # Left mouse button clicked
                    mouse_pos = pygame.mouse.get_pos()
                    # Calculate clicked cell coordinates
                    row = mouse_pos[1] // self.square_size
                    col = mouse_pos[0] // self.square_size
                    valid_moves = self.board.valid_moves(self.players[self.current_player])
                    if not self.board.valid(row, col) or self.board.board[row][col] not in valid_moves:
                        return

                    self.board.make_move(self.players[self.current_player], self.board.board[row][col])
                    self.current_player = (self.current_player + 1) % 2
