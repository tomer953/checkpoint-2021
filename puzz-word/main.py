import pprint
import copy
import numpy as np

PIECE = '*'
HOLE = 'o'
BLANK = ' '


def create_board():
    row = [PIECE for i in range(7)]
    m = [row[:] for j in range(7)]
    invalid = [(0, 0), (0, 1), (1, 0), (1, 1),
               (5, 0), (5, 1), (6, 0), (6, 1),
               (0, 5), (0, 6), (1, 5), (1, 6),
               (5, 5), (5, 6), (6, 5), (6, 6)]
    for x, y in invalid:
        m[x][y] = BLANK
    m[3][3] = HOLE
    # board = np.array(m)
    return m


# level_dest = [
#     "  OOO  ",
#     "  ..O  ",
#     "OO.OO.O",
#     "O.O..OO",
#     "OOOO.OO",
#     "  OOO  ",
#     "  OOO  "
# ]

english_dest = [
    [' ', ' ', HOLE, HOLE, HOLE, ' ', ' '],
    [' ', ' ', HOLE, HOLE, HOLE, ' ', ' '],
    [HOLE, HOLE, HOLE, HOLE, HOLE, HOLE, HOLE],
    [HOLE, HOLE, HOLE, PIECE, HOLE, HOLE, HOLE],
    [HOLE, HOLE, HOLE, HOLE, HOLE, HOLE, HOLE],
    [' ', ' ', HOLE, HOLE, HOLE, ' ', ' '],
    [' ', ' ', HOLE, HOLE, HOLE, ' ', ' ']
]

# english_dest = [
#     "  ...  ",
#     "  ...  ",
#     ".......",
#     "...O...",
#     ".......",
#     "  ...  ",
#     "  ...  "
# ]




def importJsonDest(level_dest):
    result = []
    for x in level_dest:
        line = []
        for c in x:
            if c == ' ':
                line.append(BLANK)
            if c == 'O':
                line.append(PIECE)
            if c == '.':
                line.append(HOLE)
        result.append(line)
    return result


def dest_board():
    # dest_board = importJsonDest(english_dest)
    return english_dest


def valid_move(board, x, y, d):
    if not board[x][y] == PIECE:
        return False
    if d == '<' and y > 1 and board[x][y-1] == PIECE and board[x][y-2] == HOLE or \
       d == '>' and y < 5 and board[x][y+1] == PIECE and board[x][y+2] == HOLE or \
       d == '^' and x > 1 and board[x-1][y] == PIECE and board[x-2][y] == HOLE or \
       d == 'v' and x < 5 and board[x+1][y] == PIECE and board[x+2][y] == HOLE:
        return True
    return False


def move(m, x, y, d):
    m[x][y] = HOLE
    if d == '<':
        m[x][y-1] = HOLE
        m[x][y-2] = PIECE
    if d == '>':
        m[x][y+1] = HOLE
        m[x][y+2] = PIECE
    if d == '^':
        m[x-1][y] = HOLE
        m[x-2][y] = PIECE
    if d == 'v':
        m[x+1][y] = HOLE
        m[x+2][y] = PIECE


def valid_moves(m):
    return [(x, y, d)
            for x in range(7)
            for y in range(7)
            for d in ['<', '>', '^', 'v']
            if valid_move(m, x, y, d)]


def count_pieces(m):
    return (m[3][3] == PIECE) and len([m[i][j] for i in range(7)
                                       for j in range(7)
                                       if m[i][j] == PIECE]) == 1


def solved(m):
    # return np.array_equal(m, dest_board())
    return m == dest_board()
    # return count_pieces(m) == 1


def play(board, solution):
    if solved(board):
        return True

    to_test = valid_moves(board)
    for t in to_test:
        m_copy = copy.deepcopy(board)
        move(m_copy, *t)
        if play(m_copy, solution):
            solution.append(t)
            return True
    return False


if __name__ == '__main__':
    board = create_board()
    solution = []
    play(board, solution)
    solution.reverse()
    pprint.pprint(solution)
    print('done')
