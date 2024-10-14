import tictactoe
import constants as CONST

class Minimax:
    def __init__(self, minimax_board, depth, is_max):
        self.minimax_board = minimax_board
        self.depth = depth
        self.is_max = is_max

    def solve(self):
        if tictactoe.check_win(2, self.minimax_board):
            return float('inf')
        elif tictactoe.check_win(1, self.minimax_board):
            return float('-inf')
        elif tictactoe.is_board_full(self.minimax_board):
            return 0

        if self.is_max: # If best what should com do ?
            best_score = -1000
            for row in range(CONST.BOARD_ROWS):
                for col in range(CONST.BOARD_COLS):
                    if self.minimax_board[row][col] == 0:
                        self.minimax_board[row][col] = 2
                        self.depth += 1
                        self.is_max = False
                        score = self.solve()
                        self.minimax_board[row][col] = 0
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = 1000
            for row in range(CONST.BOARD_ROWS):
                for col in range(CONST.BOARD_COLS):
                    if self.minimax_board[row][col] == 0:
                        self.minimax_board[row][col] = 1
                        self.depth += 1
                        self.is_max = True
                        score = self.solve()
                        self.minimax_board[row][col] = 0
                        best_score = min(score, best_score)
            return best_score