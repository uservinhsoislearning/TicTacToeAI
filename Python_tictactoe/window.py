import pygame
import numpy as np
import constants as CONST

pygame.init()

screen = pygame.display.set_mode((CONST.WINDOW_WIDTH, CONST.WINDOW_HEIGHT))
pygame.display.set_caption("Choose your desired algorithm")

# Button positions
button_1_rect = pygame.Rect((CONST.WINDOW_WIDTH // 2 - CONST.BUTTON_WIDTH - CONST.BUTTON_MARGIN, CONST.WINDOW_HEIGHT // 2 - CONST.BUTTON_HEIGHT // 2), 
                            (CONST.BUTTON_WIDTH, CONST.BUTTON_HEIGHT))
button_2_rect = pygame.Rect((CONST.WINDOW_WIDTH // 2 + CONST.BUTTON_MARGIN, CONST.WINDOW_HEIGHT // 2 - CONST.BUTTON_HEIGHT // 2), 
                            (CONST.BUTTON_WIDTH, CONST.BUTTON_HEIGHT))

# Selected solver (None initially)
selected_solver = None

# Main loop
running = True
while running:
    screen.fill(CONST.WHITE)

    # Draw buttons
    pygame.draw.rect(screen, CONST.BLUE if selected_solver == "Minimax" else CONST.BLACK, button_1_rect, 2)
    pygame.draw.rect(screen, CONST.RED if selected_solver == "AlphaBeta" else CONST.BLACK, button_2_rect, 2)

    # Button text
    text_1 = CONST.FONT.render("Minimax", True, CONST.BLACK)
    text_2 = CONST.FONT.render("AlphaBeta", True, CONST.BLACK)
    screen.blit(text_1, (button_1_rect.centerx - text_1.get_width() // 2, button_1_rect.centery - text_1.get_height() // 2))
    screen.blit(text_2, (button_2_rect.centerx - text_2.get_width() // 2, button_2_rect.centery - text_2.get_height() // 2))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_1_rect.collidepoint(event.pos):
                selected_solver = "Minimax"
                print("Minimax solver selected.")
            elif button_2_rect.collidepoint(event.pos):
                selected_solver = "AlphaBeta"
                print("AlphaBeta solver selected.")

    # Update display
    pygame.display.update()