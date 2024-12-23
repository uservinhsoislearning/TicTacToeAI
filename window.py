import pygame
import sys
import time
import numpy as np
import constants as CONST

pygame.init()

FONT = pygame.font.Font(None, 30)

def GUI():
    screen = pygame.display.set_mode((CONST.WINDOW_WIDTH, CONST.WINDOW_HEIGHT))
    pygame.display.set_caption("Choose your desired algorithm")

    # Button positions
    button_1_rect = pygame.Rect((CONST.WINDOW_WIDTH // 2 - CONST.BUTTON_WIDTH - CONST.BUTTON_MARGIN, CONST.WINDOW_HEIGHT // 2 - CONST.BUTTON_HEIGHT // 2), 
                            (CONST.BUTTON_WIDTH, CONST.BUTTON_HEIGHT))
    button_2_rect = pygame.Rect((CONST.WINDOW_WIDTH // 2 + CONST.BUTTON_MARGIN, CONST.WINDOW_HEIGHT // 2 - CONST.BUTTON_HEIGHT // 2), 
                            (CONST.BUTTON_WIDTH, CONST.BUTTON_HEIGHT))
    
    button_1_rect = pygame.Rect(
        (CONST.WINDOW_WIDTH // 2 - CONST.BUTTON_WIDTH // 2, CONST.WINDOW_HEIGHT // 2 - 1.5 * CONST.BUTTON_HEIGHT - CONST.BUTTON_MARGIN),
        (CONST.BUTTON_WIDTH, CONST.BUTTON_HEIGHT))
    
    button_2_rect = pygame.Rect(
        (CONST.WINDOW_WIDTH // 2 - CONST.BUTTON_WIDTH // 2, CONST.WINDOW_HEIGHT // 2 - 0.5 * CONST.BUTTON_HEIGHT),
        (CONST.BUTTON_WIDTH, CONST.BUTTON_HEIGHT))
    
    button_3_rect = pygame.Rect(
        (CONST.WINDOW_WIDTH // 2 - CONST.BUTTON_WIDTH // 2, CONST.WINDOW_HEIGHT // 2 + 0.5 * CONST.BUTTON_HEIGHT + CONST.BUTTON_MARGIN),
        (CONST.BUTTON_WIDTH, CONST.BUTTON_HEIGHT))
    
    selected_solver = None
    running = True
    message = ""
    while running:
        screen.fill(CONST.WHITE)

        # Draw buttons
        pygame.draw.rect(screen, CONST.BLUE if selected_solver == "Minimax" else CONST.BLACK, button_1_rect, 2)
        pygame.draw.rect(screen, CONST.RED if selected_solver == "AlphaBeta" else CONST.BLACK, button_2_rect, 2)
        pygame.draw.rect(screen, CONST.GREEN if selected_solver == "MCTS" else CONST.BLACK, button_3_rect, 2)

        # Button text
        text_1 = FONT.render("Minimax", True, CONST.BLACK)
        text_2 = FONT.render("AlphaBeta", True, CONST.BLACK)
        text_3 = FONT.render("MCTS", True, CONST.BLACK)

        screen.blit(text_1, (button_1_rect.centerx - text_1.get_width() // 2, button_1_rect.centery - text_1.get_height() // 2))
        screen.blit(text_2, (button_2_rect.centerx - text_2.get_width() // 2, button_2_rect.centery - text_2.get_height() // 2))
        screen.blit(text_3, (button_3_rect.centerx - text_3.get_width() // 2, button_3_rect.centery - text_3.get_height() // 2))

        if message:
            message_text = FONT.render(message, True, CONST.BLACK)
            screen.blit(
                message_text,
                (CONST.WINDOW_WIDTH // 2 - message_text.get_width() // 2, CONST.WINDOW_HEIGHT // 2 + 2.5*CONST.BUTTON_HEIGHT),
            )
            pygame.display.update()

            time.sleep(1)
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_1_rect.collidepoint(event.pos):
                    selected_solver = "Minimax"
                    message = "Minimax solver selected."
                elif button_2_rect.collidepoint(event.pos):
                    selected_solver = "AlphaBeta"
                    message = "AlphaBeta solver selected."
                elif button_3_rect.collidepoint(event.pos):
                    selected_solver = "MCTS"
                    message = "MCTS solver selected."

        # Update display
        pygame.display.update()
    screen = pygame.display.set_mode((CONST.GWINDOW_WIDTH, CONST.GWINDOW_HEIGHT))
    pygame.display.set_caption(f'{selected_solver}-TicTacToeAI')
    screen.fill(CONST.WHITE)
    return selected_solver