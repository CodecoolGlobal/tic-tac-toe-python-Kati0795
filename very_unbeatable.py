def get_ai_move_hard_hu(board, player):
    import random
    row, col = 0, 0
    import copy
    from tic_tac_toe import has_won
    from unbeatable import get_ai_move_hard_ai

    row, col = 0, 0
    list_row = board[row]
    last_element = len(list_row)-1
    corner_indexes = [0,last_element]
    coords = []
    colored_X = '\033[31mX\033[0m'
    colored_O = '\033[34mO\033[0m'

    letter = ''
    if player == colored_X:
        letter = colored_O
    elif player == colored_O:
        letter = colored_X
    
    middle_row = int(len(board) / 2)
    middle_col = int(len(board[middle_row]) / 2)
    if board[middle_row][middle_col] == '.':
            row = middle_row
            col = middle_col
            return row, col
    
    if board[middle_row][middle_col] == player and (board[0][middle_col] == player or board[middle_row][0] == player or board[middle_row][-1] == player or board[-1][middle_col] == player):
        coords = get_ai_move_hard_ai(board, player)
        row = coords[0]
        col = coords[1]
        return row, col
    elif board[middle_row][middle_col] == letter:
        coords = get_ai_move_hard_ai(board, player)
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
    
