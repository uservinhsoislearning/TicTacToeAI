import constants as CONST
import Game.tictactoe as tictactoe

class Minimax:
    def __init__(self, minimax_board, depth, is_max):
        self.minimax_board = minimax_board
        self.depth = depth
        self.is_max = is_max

    def solve(self):
        '''Implementing MiniMax algorithm using recursion.
        
        Base cases:

        - Player 1 (human) wins: return -infinity score.

        - Player 2 (computer) wins: return infinity score.

        - Draws: return 0

        '''
        if tictactoe.check_win(2, self.minimax_board):
            return float('inf')
        elif tictactoe.check_win(1, self.minimax_board):
            return float('-inf')
        elif tictactoe.is_board_full(self.minimax_board):
            return 0

        if self.is_max:
            best_score = CONST.MIN
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
            best_score = CONST.MAX
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
    
    def best_move(self):
        '''Play the best move according to the selected algorithm'''
        best_score = CONST.MIN
        move = (-1,-1)
        for row in range(CONST.BOARD_ROWS):
            for col in range(CONST.BOARD_COLS):
                if tictactoe.board[row][col] == 0:
                    tictactoe.board[row][col] = 2
                    solver = Minimax(tictactoe.board, 0, False)
                    score = solver.solve()
                    tictactoe.board[row][col] = 0
                    if score > best_score:
                        best_score = score
                        move = (row,col)

        if move != (-1,-1):
            tictactoe.mark_square(move[0], move[1], 2)
            return True
        return False