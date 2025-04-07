"""
Tic Tac Toe Player
"""

import copy
import math  # noqa: F401

X = "X"
O = "O"  # noqa: E741
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


# board1 = initial_state()


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Count the number of X's and O's on the board
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    # If the counts are equal, it's X's turn (since X goes first)
    if x_count == o_count:
        return X
    else:
        return O


# player1 = player(board1)


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    for i in range(3):  # Loop through rows
        for j in range(3):  # Loop through columns
            if board[i][j] == EMPTY:  # Check if the spot is empty
                possible_actions.add((i, j))  # Add the action as a tuple (i, j)

    return possible_actions


# pos_act = actions(board1)


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # make a deepcopy so that the original board is not modified.
    new_board = copy.deepcopy(board)

    i, j = action  # unpack the action tuple (row, column)

    # Check if the action is a valid move (the spot must be empty)
    if new_board[i][j] != EMPTY:
        raise ValueError(f"Invalid action {action}: spot is not empty!")

    # Determine the current player
    current_player = player(board)

    # Make the move on the new board
    new_board[i][j] = current_player
    return new_board


# new_board1 = result(board1, [0, 0])
# new_board2 = result(new_board1, [1, 1])
# new_board3 = result(new_board2, [2, 2])


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]  # Return the symbol of the winner

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    # if no winner found:
    return None


# winner1 = winner(new_board3)


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    if len(actions(board)) == 0:
        return True

    # game not over:
    return False


# bFin = terminal(new_board3)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1

    # otherwise
    return 0


def minimax(board):
    """
    Returns the optimal move for the current player (X or O) on the given board.
    If the board is terminal, returns None.
    """
    # If the board is in a terminal state (game over), return None
    if terminal(board):
        return None

    # Initialize best score
    if player(board) == X:
        best_score = -math.inf  # Maximizing for X
        best_move = None
        for action in actions(board):
            # Apply the action to get the resulting board
            new_board = result(board, action)
            # Recursively call minimax for the new board
            score = minimax_score(new_board)
            if score > best_score:
                best_score = score
                best_move = action
    else:
        best_score = math.inf  # Minimizing for O
        best_move = None
        for action in actions(board):
            # Apply the action to get the resulting board
            new_board = result(board, action)
            # Recursively call minimax for the new board
            score = minimax_score(new_board)
            if score < best_score:
                best_score = score
                best_move = action

    return best_move


def minimax_score(board):
    """
    Helper function to calculate the score of the board.
    If it's X's turn, it tries to maximize the score.
    If it's O's turn, it tries to minimize the score.
    """
    if terminal(board):
        return utility(board)

    # If it's X's turn, we maximize the score
    if player(board) == X:
        best_score = -math.inf
        for action in actions(board):
            new_board = result(board, action)
            best_score = max(best_score, minimax_score(new_board))
        return best_score

    # If it's O's turn, we minimize the score
    else:
        best_score = math.inf
        for action in actions(board):
            new_board = result(board, action)
            best_score = min(best_score, minimax_score(new_board))
        return best_score


# best_action = minimax(new_board3)
