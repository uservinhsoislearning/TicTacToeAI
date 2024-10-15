import tictactoe
import constants as CONST

class AlphaBeta:
    def __init__(self, AB_board, depth, is_max, alpha, beta):
        self.AB_board = AB_board
        self.depth = depth
        self.is_max = is_max
        self.alpha = alpha
        self.beta = beta

    def solve(self):
        if tictactoe.check_win(2, self.AB_board):
            return float('inf')
        elif tictactoe.check_win(1, self.AB_board):
            return float('-inf')
        elif tictactoe.is_board_full(self.AB_board):
            return 0
        
        if self.is_max:
            best_score = -1000
            for row in range(CONST.BOARD_ROWS):
                for col in range(CONST.BOARD_COLS):
                    if self.AB_board[row][col] == 0:
                        self.AB_board[row][col] = 2
                        self.depth += 1
                        self.is_max = False
                        score = self.solve()
                        best_score = max(score, best_score)
                        self.alpha = max(self.alpha, score)
                        if self.beta <= self.alpha:
                            break
            return best_score
        
        else:
            best_score = 1000
            for row in range(CONST.BOARD_ROWS):
                for col in range(CONST.BOARD_COLS):
                    if self.AB_board[row][col] == 0:
                        self.AB_board[row][col] = 1
                        self.depth += 1
                        self.is_max = True
                        score = self.solve()
                        best_score = min(score, best_score)
                        self.beta = min(self.alpha, score)
                        if self.beta <= self.alpha:
                            break
            return best_score
        
    def best_move(self):
        best_score = -1000
        move = (-1,-1)
        for row in range(CONST.BOARD_ROWS):
            for col in range(CONST.BOARD_COLS):
                if tictactoe.board[row][col] == 0:
                    tictactoe.board[row][col] = 2
                    solver = AlphaBeta(tictactoe.board, 0, False, self.alpha, self.beta)
                    score = solver.solve()
                    tictactoe.board[row][col] = 0
                    if score > best_score:
                        best_score = score
                        move = (row,col)
                    self.alpha = max(self.alpha, score)
        
        if move != (-1,-1):
            tictactoe.mark_square(move[0], move[1], 2)
            return True
        return False