import sys 
import string
import random

def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    row_A = ['.', '.', '.']
    row_B = ['.', '.', '.']
    row_C = ['.', '.', '.']
    board = [row_A, row_B, row_C]

    return board


def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    rows = list(string.ascii_uppercase)
    columns = [str(num) for num in range(len(board)+1)]
    while True:
        coordinates = input("\n A1 - C3: ")
        if coordinates == "quit":  #quit
            sys.exit()
        coordinates = list(coordinates)
        coordinates[0] = coordinates[0].upper()
        if len(coordinates) != 2:
            continue        
        elif coordinates[0].upper() in rows and coordinates[1] in columns:
            row = rows.index(coordinates[0])
            col = int(coordinates[1])-1
            if board[row][col] == '.':
                break
            else:
                print('Reserved')
                continue
    
    return row, col

def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    while True:
        row = random.randrange(len(board))
        col = random.randrange(len(board[row]))
        if board[row][col] == '.':
            break
        else:
            continue
    return row, col

def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    board[row][col] = player
    # print (board)

def has_won(board, player):
    for row_index, row in enumerate(board):  #check the rows 
        if all(elem == row[0] for elem in row) and row[0] == player:
            return True
        for col_index in range(len(row)):            
            if all(row[col_index] == player for row in board):
                return True
        for row in board:            
            if board[0][0] == player and board[-1][-1] == player and board[1][1] == player: 
                return True
            if board[0][-1] == player and board[-1][0] == player and board[1][1] == player:    
                return True
    return False

def is_full(board):
    for row in board:
        if '.' in row:
            return False
    return True

def print_board(board):
    abc = list(string.ascii_uppercase)
    print(f"\n  {'   '.join([str(num + 1) for num in range(len(board))])}")
    for index, row in enumerate(board):
        print(f"{abc[index]} {' | '.join(row)}")
        if index != 2:
            print(" ---+---+---")
        else:
            break



    
def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    if winner == 0:
        print("\n It's a tie!")
    else:
        print(f"\n\033[32m Congrats! {winner} has won!\033[0;0m \n")
    
    
 

def tictactoe_game(mode):
    
    board = init_board()
    player = 'X'
    
    while True:
        print_board(board)
        if mode == "HUMAN-HUMAN":
            row, col = get_move(board, player)
        elif mode == "HUMAN-AI":
            if player == 'X':
                row, col = get_move(board, player)
            else:
                row,col = get_ai_move(board, player)
        elif mode == "AI-HUMAN":
            if player == 'X':
                row,col = get_ai_move(board, player)
            else:
                row, col = get_move(board, player)
        mark(board, player, row, col)   
        if has_won(board, player):
            winner = player
            break
        if is_full(board):
            winner = 0
            break
        if player == 'X':
            player = 'O'
        elif player == 'O':
            player = 'X' 
    print_board(board)    
    print_result(winner)



def main_menu():
    mode_choice = int(input("Single player: 1, Multiplayer:(player first) 2, Multiplayer:(AI first) 3\n"))
    if mode_choice == 1:
        mode = "HUMAN-HUMAN"   
    elif mode_choice == 2:
        mode = "HUMAN-AI"
    elif mode_choice == 3:
        mode = "AI-HUMAN"
    tictactoe_game(mode)


if __name__ == '__main__':
    main_menu()
