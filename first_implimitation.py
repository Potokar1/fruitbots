# My first implementaion of the bug program
# Jack Dubbs
# Unfortunately, I was never able to get this to compile :/ blame javascript

# "Main" for the bug program
def make_move():
    board = get_board()
    board_rows, board_cols = get_dimensions(board)
    seen = []

    #we found an item! take it!
    if check_on_me(board) >= 1:
        return TAKE
    my_x,my_y = find_me()

    # move around the board so we can get our yummy food
    return go_in_circles(my_x,my_y,board_rows,board_cols,seen)


# return the dimenions [x,y] for the size of the board
def get_dimensions(board):
    return [len(board),len(board[0])]

# return the location [x,y] of where the enemmy is
def find_enemy():
    return [get_opponent_x(),get_opponent_y()]

# return the location [x,y] of where I am
def find_me():
    return [get_my_x(),get_my_y()]

# returns true if there is a food on my current location. False O.W.
def check_on_me(board):
    x,y = find_me()
    return has_item(board[x][y])

def go_in_circles(x,y,rows,cols,seen):
    # if you can go down and havn't been there yet then go down
    if x < rows - 1 and [x + 1,y] not in seen:
        seen.append([x+1,y])
        return SOUTH
    # if you can't go down then go left if you havn't been there before
    if y > 0 and [x,y-1] not in seen:
        seen.append([x,y-1])
        return WEST
    # if you can't go down or left then go up if you havn't been there before
    if x > 0 and [x-1,y] not in seen:
        seen.append([x-1,y])
        return NORTH
    # if you can't go down or left or up then go right if you havn't been there before
    if y < cols - 1 and [x,y+1] not in seen:
        seen.append([x,y+1])
        return EAST
    # now we will cross a seen area if we can , going up first
    if x > 0:
        return NORTH
    if x < rows - 1:
        return SOUTH
    if y > 0:
        return WEST
    if y < cols - 1:
        return EAST

make_move()
