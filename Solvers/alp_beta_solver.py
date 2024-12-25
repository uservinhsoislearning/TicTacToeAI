import constants as CONST
import Game.tictactoe as tictactoe
import copy 

class AlphaBeta:
    def __init__(self, AB_board, depth, is_max, alpha, beta):
        self.AB_board = AB_board
        self.depth = depth
        self.is_max = is_max
        self.alpha = alpha
        self.beta = beta

    def solve(self):
        '''Implementing Alpha-Beta pruning algorithm using recursion.
        
        Base cases:

        - Player 1 (human) wins: return -infinity score.

        - Player 2 (computer) wins: return infinity score.

        - Draws: return 0

        '''
        if tictactoe.check_win(2, self.AB_board):
            return float('inf')
        elif tictactoe.check_win(1, self.AB_board):
            return float('-inf')
        elif tictactoe.is_board_full(self.AB_board):
            return 0
        
        if self.is_max:
            best_score = CONST.MIN
            for row in range(CONST.BOARD_ROWS):
                for col in range(CONST.BOARD_COLS):
                    if self.AB_board[row][col] == 0:
                        new_board = copy.deepcopy(self.AB_board)
                        new_board[row][col] = 2
                        score = AlphaBeta(new_board, self.depth + 1, False, self.alpha, self.beta).solve()
                        new_board[row][col] = 0
                        best_score = max(score, best_score)
                        self.alpha = max(self.alpha, best_score)
                        if self.beta <= self.alpha:
                            break
            return best_score
        
        else:
            best_score = CONST.MAX
            for row in range(CONST.BOARD_ROWS):
                for col in range(CONST.BOARD_COLS):
                    if self.AB_board[row][col] == 0:
                        new_board = copy.deepcopy(self.AB_board)
                        new_board[row][col] = 1
                        score = AlphaBeta(new_board, self.depth + 1, True, self.alpha, self.beta).solve()
                        new_board[row][col] = 0
                        best_score = min(score, best_score)
                        self.beta = min(self.beta, best_score)
                        if self.beta <= self.alpha:
                            break
            return best_score
        
    def best_move(self):
        '''Play the best move according to the selected algorithm'''
        best_score = CONST.MIN
        self.alpha = CONST.MIN
        self.beta = CONST.MAX
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