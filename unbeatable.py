def get_ai_move_hard_ai(board, player):
    import random
    row, col = 0, 0
    import copy
    from tic_tac_toe import has_won
    row, col = 0, 0
    letter = ''
    colored_X = '\033[31mX\033[0m'
    colored_O = '\033[34mO\033[0m'
    if player == colored_X:
        letter = 'O'
    elif player == 'O':
        letter = colored_X

    for i in range(len(board)):
        for j in range(len(board)):
            board_copy = copy.deepcopy(board)
            board_copy[i][j] = player
            if has_won(board_copy, player) and board[i][j] == '.':
                row = i
                col = j
                return row, col
            else:
                board_copy[i][j] == '.'
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
    
    corner_indexes = [0,2]
    row = random.choice(corner_indexes)
    col = random.choice(corner_indexes)
    if board[row][col] == '.':
        return row, col
    elif board[row][col] != '.':
        for i in corner_indexes:
            for j in corner_indexes:
                if board[i][j] == '.':
                    row = i
                    col = j
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
    