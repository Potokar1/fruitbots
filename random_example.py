# This would not work because it makes system calls?
from random import randint

def make_move():
    board = get_board()

    #we found an item! take it!
    if board[get_my_x()][get_my_y()] > 0:
        return TAKE

    rand = randint(1, 4)

    if rand == 1:
        return NORTH
    if rand == 2:
        return SOUTH
    if rand == 3:
        return EAST
    if rand == 4:
        return WEST

    return PASS
