"""
Tic Tac Toe Player
"""

from math import inf
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """

    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    count = 0
    for row in board:
        for cell in row:
            if cell:
                count += 1
    if count % 2 == 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    actions = set()

    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if not cell:
                actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if action not in actions(board):
        raise Exception("Invalid Action!")

    board_copy = deepcopy(board)
    board_copy[action[0]][action[1]] = player(board)

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for i in range(3):
        if board[i][0] == X and board[i][1] == X and board[i][2] == X:
            return X
        elif board[i][0] == O and board[i][1] == O and board[i][2] == O:
            return O

    for j in range(3):
        if board[0][j] == X and board[1][j] == X and board[2][j] == X:
            return X
        elif board[0][j] == O and board[1][j] == O and board[2][j] == O:
            return O

    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    elif board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    if board[2][0] == X and board[1][1] == X and board[0][2] == X:
        return X
    elif board[2][0] == O and board[1][1] == O and board[0][2] == O:
        return O

    return

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board):
        return True

    for row in board:
        for cell in row:
            if not cell:
                return False

    return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return

    if player(board) == X:
        return max_value(board, -inf, inf)[1]
    else:
        return min_value(board, -inf, inf)[1]

def max_value(board, Max, Min):
    move = None

    if terminal(board):
        return [utility(board), None]

    v = -inf

    for action in actions(board):
        test = min_value(result(board, action), Max, Min)[0]
        Max = max(Max, test)
        if test > v:
            v = test
            move = action

        if Max >= Min:
            break

    return [v, move]


def min_value(board, Max, Min):
    move = None

    if terminal(board):
        return [utility(board), None]

    v = inf

    for action in actions(board):
        test = max_value(result(board, action), Max, Min)[0]
        Min = min(Min, test)
        if test < v:
            v = test
            move = action

        if Max >= Min:
            break

    return [v, move]