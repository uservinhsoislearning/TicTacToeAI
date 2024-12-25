import constants as CONST
import Game.tictactoe as tictactoe
import copy
import numpy as np

class policy():
    def __init__(self):
        self.tree = {}
        pass


class VanilaMCTS():
    def __init__(self, n_iterations=50, depth=15, exploration_constant=5.0, tree = None, game_board=None, player=None):
        self.n_iterations = n_iterations
        self.depth = depth
        self.exploration_constant = exploration_constant
        self.total_n = 0

        self.leaf_node_id = None

        n_rows = len(game_board)
        self.n_rows = n_rows

        if tree == None:
            self.tree = self._set_tictactoe(game_board, player)
        else:
            self.tree = tree

    def _set_tictactoe(self, game_board, player):
        root_id = (0,)
        tree = {root_id: {'state': game_board,
                          'player': player,
                          'child': [],
                          'parent': None,
                          'n': 0,
                          'w': 0,
                          'q': None}}
        return tree

    def selection(self):
        '''Find the best child node in the tree (maximum UCT value)'''
        leaf_node_found = False
        leaf_node_id = (0,) # root node id

        while not leaf_node_found:
            node_id = leaf_node_id
            n_child = len(self.tree[node_id]['child'])

            if n_child == 0:
                leaf_node_id = node_id
                leaf_node_found = True
            else:
                maximum_uct_value = CONST.MIN
                for i in range(n_child):
                    action = self.tree[node_id]['child'][i]

                    child_id = node_id + (action,)
                    w = self.tree[child_id]['w']
                    n = self.tree[child_id]['n']
                    total_n = self.total_n

                    if n == 0:
                        n = 1e-4
                    exploitation_value = w / n
                    exploration_value  = np.sqrt(np.log(total_n)/n)
                    uct_value = exploitation_value + self.exploration_constant * exploration_value

                    if uct_value > maximum_uct_value:
                        maximum_uct_value = uct_value
                        leaf_node_id = child_id

        depth = len(leaf_node_id)

        return leaf_node_id, depth

    def expansion(self, leaf_node_id):
        '''Create all posible outcomes from leaf nodes'''
        leaf_state = self.tree[leaf_node_id]['state']
        winner = self._is_terminal(leaf_state)
        possible_actions = self._get_valid_actions(leaf_state)

        child_node_id = leaf_node_id
        if winner is None:
            childs = []
            for action_set in possible_actions:
                action, action_idx = action_set
                state = copy.deepcopy(self.tree[leaf_node_id]['state'])
                current_player = self.tree[leaf_node_id]['player']

                if current_player == 1:
                    next_turn = 2
                    state[action] = 1
                else:
                    next_turn = 1
                    state[action] = 2

                child_id = leaf_node_id + (action_idx, )
                childs.append(child_id)
                self.tree[child_id] = {'state': state,
                                       'player': next_turn,
                                       'child': [],
                                       'parent': leaf_node_id,
                                       'n': 0, 'w': 0, 'q':0}
                self.tree[leaf_node_id]['child'].append(action_idx)
            rand_idx = np.random.randint(low=0, high=len(childs), size=1)

            child_node_id = childs[rand_idx[0]]
        return child_node_id

    def _is_terminal(self, leaf_state):
        '''Check terminal (game state)'''
        def __who_wins(leaf_state):
            if tictactoe.check_win(1,check_board=leaf_state):
                return 1
            if tictactoe.check_win(2,check_board=leaf_state):
                return 2
            return None

        def __is_terminal_in_conv(leaf_state):
            result = __who_wins(leaf_state)
            if result is not None:
                return result
            return None

        winner = __is_terminal_in_conv(leaf_state)
        if winner is not None:
            return winner

        if tictactoe.is_board_full(check_board=leaf_state):
            return 'draw'
        return None

    def _get_valid_actions(self, leaf_state):
        '''
        out:
        - set of possible actions ((row,col), action_idx)
        '''
        actions = []
        count = 0

        for i in range(3):
            for j in range(3):
                if leaf_state[i][j] == 0:
                    actions.append([(i, j), count])
                count += 1
        return actions

    def simulation(self, child_node_id):
        '''
        simulate game from child node's state until it reaches the resulting state of the game.
        in:
        - child node id (randomly selected child node id from `expansion`)
        out:
        - winner ('o', 'x', 'draw')
        '''
        self.total_n += 1
        state = copy.deepcopy(self.tree[child_node_id]['state'])
        previous_player = copy.deepcopy(self.tree[child_node_id]['player'])
        anybody_win = False

        while not anybody_win:
            winner = self._is_terminal(state)
            if winner is not None:
                anybody_win = True
            else:
                possible_actions = self._get_valid_actions(state)

                rand_idx = np.random.randint(low=0, high=len(possible_actions), size=1)[0]
                action, _ = possible_actions[rand_idx]

                if previous_player == 1:
                    current_player = 2
                    state[action] = 2
                else:
                    current_player = 1
                    state[action] = 1

                previous_player = current_player
        return winner

    def backprop(self, child_node_id, winner):

        if winner == 'draw':
            reward = 0
        elif winner == 2:
            reward = 1
        else:
            reward = -1

        finish_backprob = False
        node_id = child_node_id
        while not finish_backprob:
            self.tree[node_id]['n'] += 1
            self.tree[node_id]['w'] += reward
            self.tree[node_id]['q'] = self.tree[node_id]['w'] / self.tree[node_id]['n']
            parent_id = self.tree[node_id]['parent']
            if parent_id == (0,):
                self.tree[parent_id]['n'] += 1
                self.tree[parent_id]['w'] += reward
                self.tree[parent_id]['q'] = self.tree[parent_id]['w'] / self.tree[parent_id]['n']
                finish_backprob = True
            else:
                node_id = parent_id

    def best_move(self):
        best_q = CONST.MIN
        move = (-1,-1)

        if tictactoe.is_board_full():
            return False

        for _ in range(self.n_iterations):
            leaf_node_id, depth_searched = self.selection()
            child_node_id = self.expansion(leaf_node_id)
            winner = self.simulation(child_node_id)
            self.backprop(child_node_id, winner)

            if depth_searched > self.depth:
                break

        current_state_node_id = (0,)
        action_candidates = self.tree[current_state_node_id]['child']

        best_action = -1

        for a in action_candidates:
            q = self.tree[(0,)+(a,)]['q']
            if q > best_q:
                best_q = q
                best_action = a

        action = np.zeros([9])
        action[best_action] = 1

        if np.any(action) != 0:
            action_index = np.argmax(action)
            move = (int(action_index / 3), action_index % 3)

        if move != (-1,-1):
            tictactoe.mark_square(move[0], move[1], 2)
            return True
        
        return False