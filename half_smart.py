def get_ai_move_medium(board, player):
    import random
    import copy
    from tic_tac_toe import has_won
    row, col = 0, 0
    letter = ''
    if player == 'X':
        letter = 'O'
    elif player == 'O':
        letter = 'X'

    for i in range(len(board)):
        for j in range(len(board)):
            board_copy = copy.deepcopy(board)
            board_copy[i][j] = player
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
            
    while True:
        row = random.randrange(len(board))
        col = random.randrange(len(board[row]))
        if board[row][col] == '.':
            return row, col
        else:
            continue
