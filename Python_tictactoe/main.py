import constants as CONST
import tictactoe
import minimax_solver as ms
import alp_beta_solver as abs
import pygame
import sys

tictactoe.draw_lines()

player = 1
game_over = False
minimaxSolver = ms.Minimax(tictactoe.board, 0 , False)
alphaBetaSolver = abs.AlphaBeta(tictactoe.board, 0, False, CONST.MIN, CONST.MAX)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0] // CONST.CELL_SIZE
            mouseY = event.pos[1] // CONST.CELL_SIZE

            if tictactoe.available_square(mouseY, mouseX):
                tictactoe.mark_square(mouseY, mouseX, player)
                if tictactoe.check_win(player):
                    game_over = True
                player = player % 2 + 1

                if not game_over:
                    if alphaBetaSolver.best_move():
                        if tictactoe.check_win(2):
                            game_over = True
                        player = player % 2 + 1

                if not game_over:
                    if tictactoe.is_board_full():
                        game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                tictactoe.restart_game()
                game_over = False
                player = 1

    if not game_over:
        tictactoe.draw_figures()
    else:
        if tictactoe.check_win(1):
            tictactoe.draw_figures(CONST.GREEN)
            tictactoe.draw_lines(CONST.GREEN)
        elif tictactoe.check_win(2):
            tictactoe.draw_figures(CONST.RED)
            tictactoe.draw_lines(CONST.RED)
        else:
            tictactoe.draw_figures(CONST.BLUE)
            tictactoe.draw_figures(CONST.BLUE)

    pygame.display.update()