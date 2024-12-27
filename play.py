import constants as CONST
import Game.tictactoe as tictactoe
import Game.window as window
import Solvers.minimax_solver as ms
import Solvers.alp_beta_solver as abs
import Solvers.MCTS_solver as mts
import pandas as pd
import pygame
import sys
import time

value = window.GUI()

tictactoe.draw_lines()

played_time = 1
move_number = 1
database = {'Play' : [], 'Move No.' : [], 'Selected Algorithm' : [], 'Time per move' : [], 'Move played': [], 'Board state' : []}
player = 1
game_over = False
if value == "Minimax":
    Solver = ms.Minimax(tictactoe.board, 0 , False)
elif value == "AlphaBeta":
    Solver = abs.AlphaBeta(tictactoe.board, 0, False, CONST.MIN, CONST.MAX)
elif value == "MCTS":
    Solver = mts.VanilaMCTS(n_iterations=1500, depth=15, exploration_constant=100, game_board=tictactoe.board, player=2)
else:
    pass

while True and played_time <= 10:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
            sys.exit()

      if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0] // CONST.CELL_SIZE
            mouseY = event.pos[1] // CONST.CELL_SIZE

            if tictactoe.available_square(mouseY, mouseX):
               tictactoe.mark_square(mouseY, mouseX, player)
               if tictactoe.check_win(player):
                  game_over = True
               player = player % 2 + 1

               if not game_over:
                  if value != "PvP Local":
                     database['Play'].append(played_time)
                     t1 = time.time()
                     is_moveable, move = Solver.best_move()
                     t2 = time.time()
                     database['Move No.'].append(move_number)
                     move_number += 1
                     database['Selected Algorithm'].append(value)
                     database['Time per move'].append(1000*(t2-t1))
                     database['Move played'].append(move)
                     database['Board state'].append(tictactoe.board.astype(int))
                     print(tictactoe.board)
                     if is_moveable:
                           if value == "MCTS":
                              Solver = mts.VanilaMCTS(n_iterations=1500, depth=15, exploration_constant=100, game_board=tictactoe.board, player=player)
                           if tictactoe.check_win(2):
                              game_over = True
                           player = player % 2 + 1
               if not game_over:
                  if tictactoe.is_board_full():
                        game_over = True

      if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
               tictactoe.restart_game()
               move_number = 1
               played_time += 1
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

database = pd.DataFrame(database)
print(database)
database.to_csv('Data/AlphaBeta.csv', index=False)