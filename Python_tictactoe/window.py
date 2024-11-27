from tkinter import *
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 200
BUTTON_WIDTH = 150
BUTTON_HEIGHT = 50
BUTTON_MARGIN = 20
FONT = pygame.font.Font(None, 30)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Window setup
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Choose your desired algorithm")

# Button positions
button_1_rect = pygame.Rect((WINDOW_WIDTH // 2 - BUTTON_WIDTH - BUTTON_MARGIN, WINDOW_HEIGHT // 2 - BUTTON_HEIGHT // 2), 
                            (BUTTON_WIDTH, BUTTON_HEIGHT))
button_2_rect = pygame.Rect((WINDOW_WIDTH // 2 + BUTTON_MARGIN, WINDOW_HEIGHT // 2 - BUTTON_HEIGHT // 2), 
                            (BUTTON_WIDTH, BUTTON_HEIGHT))

# Selected solver (None initially)
selected_solver = None

# Main loop
running = True
while running:
    screen.fill(WHITE)

    # Draw buttons
    pygame.draw.rect(screen, BLUE if selected_solver == "Minimax" else BLACK, button_1_rect, 2)
    pygame.draw.rect(screen, RED if selected_solver == "AlphaBeta" else BLACK, button_2_rect, 2)

    # Button text
    text_1 = FONT.render("Minimax", True, BLACK)
    text_2 = FONT.render("AlphaBeta", True, BLACK)
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
    pygame.display.flip()

pygame.quit()
sys.exit()
