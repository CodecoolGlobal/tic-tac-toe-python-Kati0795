def get_ai_move_hard_hu(board, player):
    import random
    row, col = 0, 0
    import copy
    from tic_tac_toe import has_won

    row, col = 0, 0
    list_row = board[row]
    last_element = len(list_row)-1
    corner_indexes = [0,last_element]
    coords = []

    letter = ''
    if player == 'X':
        letter = 'O'
    elif player == 'O':
        letter = 'X'
    
    middle_row = int(len(board) / 2)
    middle_col = int(len(board[middle_row]) / 2)
    if board[middle_row][middle_col] == '.':
            row = middle_row
            col = middle_col
            return row, col
    
    if board[middle_row][middle_col] == player and (board[0][middle_col] == player or board[middle_row][0] == player or board[middle_row][-1] == player or board[-1][middle_col] == player):
        coords = unbeatable(board, player)
        row = coords[0]
        col = coords[1]
        return row, col
    elif board[middle_row][middle_col] == letter:
        coords = unbeatable(board, player)
        row = coords[0]
        col = coords[1]
        return row, col

    elif board[middle_row][middle_col] == player:
        for i in corner_indexes:
            for j in corner_indexes:
                if board[i][j] == letter:
                    row = random.randrange(len(board))
                    
                    if row == 0 or row == last_element:
                        col = middle_col
                        if board[row][col] == '.':
                            return row, col
                    elif row == middle_row:
                        col = random.choice(corner_indexes)
                        if board[row][col] == '.':
                            return row, col
                else:
                    continue
    
    


def unbeatable(board, player):
    import copy
    import random
    from tic_tac_toe import has_won

    row, col = 0, 0
    list_row = board[row]
    last_element = len(list_row)-1
    corner_indexes = [0,last_element]
    
    letter = ''
    if player == 'X':
        letter = 'O'
    elif player == 'O':
        letter = 'X'
    
    for i in range(len(board)):
        for j in range(len(board)):
            board_copy = copy.deepcopy(board)
            board_copy[row][col] = player
            if has_won(board_copy, player) and board[i][j] == '.':
                row = i
                col = j
                return row, col
            else:
                board_copy[i][j] = '.'
                continue

        for i in range(len(board)):
            for j in range(len(board)):
                board_copy = copy.deepcopy(board)
                board_copy[i][j] = letter
                if has_won(board_copy, letter) and board[i][j] == '.':
                    row = i
                    col = j
                    return row, col
                else:
                    board_copy[i][j] = '.'
                    continue
    
    row = random.choice(corner_indexes)
    col = random.choice(corner_indexes)
    if board[row][col] == '.':
        return row, col
    elif board[row][col] != '.':
        for i in corner_indexes:
            for j in corner_indexes:
                if board[i][j] == '.':
                    return row, col
                else:
                    continue
        
    middle_row = int(len(board) / 2)
    middle_col = int(len(board[middle_row]) / 2)
    if board[middle_row][middle_col] == '.':
            row = middle_row
            col = middle_col
            return row, col
    
    while True:
        row = random.randrange(len(board))
        col = random.randrange(len(board[row]))
        if board[row][col] == '.':
            return row, col
        else:
            continue