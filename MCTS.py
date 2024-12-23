import numpy as np
import random
import constants as CONST
import tictactoe
import copy

class Node:
    def __init__(self, state, parent=None, player=1):
        self.state = state  # Current board state
        self.parent = parent  # Parent node
        self.children = []  # Child nodes
        self.visits = 0  # Number of visits to this node
        self.wins = 0  # Wins from this node's perspective
        self.player = player  # Player who made the move to reach this node

    def is_fully_expanded(self):
        return len(self.children) == len(get_available_moves(self.state))

    def best_child(self, exploration_weight=1.41): #around sqrt(2)
        """
        Choose the child node with the best UCT (Upper Confidence Bound for Trees) value.
        """
        return max(
            self.children,
            key=lambda child: (child.wins / child.visits if child.visits > 0 else 0) +
            exploration_weight * np.sqrt(np.log(self.visits + 1) / (child.visits + 1))
        )

def get_available_moves(board):
    """Return a list of available moves as (row, col) tuples."""
    return [(row, col) for row in range(CONST.BOARD_ROWS) for col in range(CONST.BOARD_COLS) if board[row][col] == 0]

def make_move(board, move, player):
    """Simulate a move on the board."""
    new_board = copy.deepcopy(board)
    new_board[move[0]][move[1]] = player
    return new_board

def rollout_policy(board, player):
    """Randomly select a move from available moves."""
    available_moves = get_available_moves(board)
    return random.choice(available_moves)

def simulate_random_game(board, player):
    """Simulate a random game until a terminal state is reached."""
    current_board = copy.deepcopy(board)
    current_player = player
    while not tictactoe.check_win(1, current_board) and not tictactoe.check_win(2, current_board) and not tictactoe.is_board_full(current_board):
        move = rollout_policy(current_board, current_player)
        current_board = make_move(current_board, move, current_player)
        current_player = current_player % 2 + 1
    if tictactoe.check_win(player, current_board):
        return 1
    elif tictactoe.check_win(3 - player, current_board):
        return -1
    else:
        return 0

def backpropagate(node, result):
    """Backpropagate the result of the simulation up the tree."""
    while node is not None:
        node.visits += 1
        if node.player == result:
            node.wins += 1
        node = node.parent

def mcts(root, iterations):
    """
    Perform Monte Carlo Tree Search starting from the root node.
    """
    for _ in range(iterations):
        # Selection
        current_node = root
        while current_node.is_fully_expanded() and current_node.children:
            current_node = current_node.best_child()

        # Expansion
        if not tictactoe.check_win(1, current_node.state) and not tictactoe.check_win(2, current_node.state) and not tictactoe.is_board_full(current_node.state):
            available_moves = get_available_moves(current_node.state)
            for move in available_moves:
                new_state = make_move(current_node.state, move, 3 - current_node.player)
                if all(child.state.tolist() != new_state.tolist() for child in current_node.children):
                    new_node = Node(new_state, parent=current_node, player=3 - current_node.player)
                    current_node.children.append(new_node)
                    current_node = new_node
                    break

        # Simulation
        result = simulate_random_game(current_node.state, current_node.player)

        # Backpropagation
        backpropagate(current_node, result)
    print(root.best_child(0).state)
    return root.best_child(0)  # Return the best move after exploration

class MCTS:
    def __init__(self, iterations=50):
        self.iterations = iterations

    def best_move(self, board=tictactoe.board, player= 2):
        root = Node(board, player= player)
        best_child = mcts(root, self.iterations)
        for move in get_available_moves(board):
            if np.array_equal(make_move(board, move, player), best_child.state):
                tictactoe.mark_square(move[0], move[1], 2)
                return True
        return False
