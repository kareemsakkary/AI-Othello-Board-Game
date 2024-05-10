import pygame
import sys


class AlertScreen:
    def __init__(self, screen, message):
        self.screen = screen
        self.message = message
        self.font = pygame.font.Font(None, 36)
        self.alert_rect = pygame.Rect(100, 200, 600, 200)
        self.button_rect = pygame.Rect(300, 400, 200, 50)
        self.button_text = self.font.render("OK", True, (255, 255, 255))
        self.button_text_rect = self.button_text.get_rect(center=self.button_rect.center)

    def render(self):
        pygame.draw.rect(self.screen, (255, 255, 255), self.alert_rect)
        pygame.draw.rect(self.screen, (0, 0, 0), self.alert_rect, 3)
        text = self.font.render(self.message, True, (0, 0, 0))
        text_rect = text.get_rect(center=self.alert_rect.center)
        self.screen.blit(text, text_rect)
        pygame.draw.rect(self.screen, (0, 0, 0), self.button_rect)
        self.screen.blit(self.button_text, self.button_text_rect)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.button_rect.collidepoint(event.pos):
                    return True
        return False
