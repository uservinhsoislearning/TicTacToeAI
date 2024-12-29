import constants as CONST
import numpy as np
import pygame

pygame.init()

screen = pygame.display.set_mode((CONST.GWINDOW_WIDTH, CONST.GWINDOW_HEIGHT))
screen.fill(CONST.WHITE)

board = np.zeros((CONST.BOARD_ROWS,CONST.BOARD_COLS))

def draw_lines(color=CONST.BLACK):
    '''Draw the lines for Tic-Tac-Toe (on a white-filled screen)'''
    for i in range(1, CONST.BOARD_ROWS):
        pygame.draw.line(screen, color, (0,CONST.CELL_SIZE*i), (CONST.GWINDOW_WIDTH, CONST.CELL_SIZE*i),  CONST.LINE_WIDTH)
        pygame.draw.line(screen, color, (CONST.CELL_SIZE*i, 0), (CONST.CELL_SIZE*i, CONST.GWINDOW_HEIGHT),  CONST.LINE_WIDTH)

def draw_figures(color=CONST.BLACK):
    '''
    Draw the symbols (X,O) depends on the player who has marked that position in the state matrix. (1 -> O, 2 -> X)
    '''
    for row in range(CONST.BOARD_ROWS):
        for col in range(CONST.BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, 
                                   color, 
                                   (int(col*CONST.CELL_SIZE + CONST.CELL_SIZE // 2), int(row*CONST.CELL_SIZE + CONST.CELL_SIZE // 2)), 
                                   CONST.O_RADIUS, 
                                   CONST.O_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, 
                                 color, 
                                 (col*CONST.CELL_SIZE + CONST.CELL_SIZE // 4, row*CONST.CELL_SIZE + CONST.CELL_SIZE // 4), 
                                 (col*CONST.CELL_SIZE + 3*CONST.CELL_SIZE // 4, row*CONST.CELL_SIZE + 3*CONST.CELL_SIZE // 4), 
                                 CONST.X_WIDTH)
                
                pygame.draw.line(screen, 
                                 color, 
                                 (col*CONST.CELL_SIZE + CONST.CELL_SIZE // 4, row*CONST.CELL_SIZE + 3*CONST.CELL_SIZE // 4), 
                                 (col*CONST.CELL_SIZE + 3*CONST.CELL_SIZE // 4, row*CONST.CELL_SIZE + CONST.CELL_SIZE // 4), 
                                 CONST.X_WIDTH)

def mark_square(row, col, player):
    '''Mark the (row, col) position in the board with the corresponding player (1 or 2)'''
    board[row][col] = player

def available_square(row, col):
    '''Check if (row, col) position in the board is free or not'''
    return board[row][col] == 0

def is_board_full(check_board=board):
    '''Check if the board is free or not'''
    for row in range(CONST.BOARD_ROWS):
        for col in range(CONST.BOARD_COLS):
            if check_board[row][col] == 0:
                return False
    return True

def check_win(player, check_board=board):
    '''Check if the game has ended (win, draw or loss) by checking if the player has won'''
    for col in range(CONST.BOARD_COLS):
        if check_board[0][col] == player and check_board[1][col] == player and check_board[2][col] == player:
            return True    
    for row in range(CONST.BOARD_ROWS):
        if check_board[row][0] == player and check_board[row][1] == player and check_board[row][2] == player:
            return True    
    if check_board[0][0] == player and check_board[1][1] == player and check_board[2][2] == player:
        return True
    if check_board[2][0] == player and check_board[1][1] == player and check_board[0][2] == player:
        return True
    return False

def restart_game():
    '''Restart the game'''
    screen.fill(CONST.WHITE)
    draw_lines()
    for row in range(CONST.BOARD_ROWS):
        for col in range(CONST.BOARD_COLS): 
            board[row][col] = 0
            