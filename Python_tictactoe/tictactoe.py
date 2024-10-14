import pygame
import numpy as np
import constants as CONST

pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 225)
RED = (255, 0, 0)
GREEN = (0, 225, 0)

# CONST
WIDTH = 300
HEIGHT = 300
LINE_WIDTH = 5
BOARD_ROWS = 3
BOARD_COLS = 3
CELL_SIZE = WIDTH // BOARD_COLS
O_RADIUS = CELL_SIZE // 3
O_WIDTH = 15
X_WIDTH = 25

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(WHITE)

board = np.zeros((BOARD_ROWS,BOARD_COLS))

def draw_lines(color=BLACK):
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, color, (0,CELL_SIZE*i), (WIDTH, CELL_SIZE*i),  LINE_WIDTH)
        pygame.draw.line(screen, color, (CELL_SIZE*i, 0), (CELL_SIZE*i, HEIGHT),  LINE_WIDTH)

def draw_figures(color=BLACK):
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, color, (int(col*CELL_SIZE + CELL_SIZE // 2), int(row*CELL_SIZE + CELL_SIZE // 2)), O_RADIUS, O_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, color, (col*CELL_SIZE + CELL_SIZE // 4, row*CELL_SIZE + CELL_SIZE // 4)
                                 , (col*CELL_SIZE + 3*CELL_SIZE // 4, row*CELL_SIZE + 3*CELL_SIZE // 4), X_WIDTH)
                pygame.draw.line(screen, color, (col*CELL_SIZE + CELL_SIZE // 4, row*CELL_SIZE + 3*CELL_SIZE // 4)
                                 , (col*CELL_SIZE + 3*CELL_SIZE // 4, row*CELL_SIZE + CELL_SIZE // 4), X_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0

def is_board_full(check_board=board):
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if check_board[row][col] == 0:
                return False
            
    return True

def check_win(player, check_board=board):
    for col in range(BOARD_COLS):
        if check_board[0][col] == player and check_board[1][col] == player and check_board[2][col] == player:
            return True
        
    for row in range(BOARD_ROWS):
        if check_board[row][0] == player and check_board[row][1] == player and check_board[row][2] == player:
            return True
        
    if check_board[0][0] == player and check_board[1][1] == player and check_board[2][2] == player:
        return True
    
    if check_board[2][0] == player and check_board[1][1] == player and check_board[0][2] == player:
        return True

    return False

def minimax(minimax_board, depth, is_max):
    if check_win(2, minimax_board):
        return float('inf')
    elif check_win(1, minimax_board):
        return float('-inf')
    elif is_board_full(minimax_board):
        return 0
    
    if is_max: # If best what should com do ?
        best_score = -1000
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if minimax_board[row][col] == 0:
                    minimax_board[row][col] = 2
                    score = minimax(minimax_board, depth+1, False)
                    minimax_board[row][col] = 0
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = 1000
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if minimax_board[row][col] == 0:
                    minimax_board[row][col] = 1
                    score = minimax(minimax_board, depth+1, True)
                    minimax_board[row][col] = 0
                    best_score = min(score, best_score)
        return best_score
    
def best_move():
    best_score = -1000
    move = (-1,-1)
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                board[row][col] = 2
                score = minimax(board, 0, False)
                board[row][col] = 0
                if score > best_score:
                    best_score = score
                    move = (row,col)

    if move != (-1,-1):
        mark_square(move[0], move[1], 2)
        return True
    return False

def restart_game():
    screen.fill(WHITE)
    draw_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS): 
            board[row][col] = 0