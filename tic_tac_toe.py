import sys 
import string
import random
import time
from half_smart import get_ai_move_medium
from unbeatable import get_ai_move_hard_ai
from very_unbeatable import get_ai_move_hard_hu

def init_board():
    board_choice = input("Choose the size of the board: (3, 5, 7) :\n")
    if board_choice == "quit":  #quit
            sys.exit()
    board_choice = int(board_choice)
    if board_choice == 3:
        row_A = ['.', '.', '.']
        row_B = ['.', '.', '.']
        row_C = ['.', '.', '.']
        board = [row_A, row_B, row_C]

    if board_choice == 5:
        row_A = ['.', '.', '.', '.', '.']
        row_B = ['.', '.', '.', '.', '.']
        row_C = ['.', '.', '.', '.', '.']
        row_D = ['.', '.', '.', '.', '.']
        row_E = ['.', '.', '.', '.', '.']
        board = [row_A, row_B, row_C, row_D, row_E]

    if board_choice == 7:
        row_A = ['.', '.', '.', '.', '.', '.', '.']
        row_B = ['.', '.', '.', '.', '.', '.', '.']
        row_C = ['.', '.', '.', '.', '.', '.', '.']
        row_D = ['.', '.', '.', '.', '.', '.', '.']
        row_E = ['.', '.', '.', '.', '.', '.', '.']
        row_F = ['.', '.', '.', '.', '.', '.', '.']
        row_G = ['.', '.', '.', '.', '.', '.', '.']
        board = [row_A, row_B, row_C, row_D, row_E, row_F, row_G]

    return board


def get_move(board, player):
    row, col = 0, 0
    rows = list(string.ascii_uppercase)
    columns = [str(num) for num in range(len(board)+1)]
    while True:
        coordinates = input("\n Make a step: ")
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

def get_ai_move_easy(board, player):
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
    board[row][col] = player

def has_won(board, player):
    for row_index, row in enumerate(board):  #check the rows 
        if all(elem == row[0] for elem in row) and row[0] == player:  #check if all element in rows are the same
            return True
        for col_index in range(len(row)):            
            if all(row[col_index] == player for row in board):        #check if row's same column are the same
                return True
        rdiags = []
        for ix in range(len(board)):
                rdiags.append(board[ix][ix])
        if rdiags.count(rdiags[0]) == len(rdiags) and rdiags[0] == player:
            return True

        ldiags = []
        for idx, reverse_idx in enumerate(reversed(range(len(board)))):
            ldiags.append(board[idx][reverse_idx])

        if ldiags.count(ldiags[0]) == len(ldiags) and ldiags[0] == player:
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
        if index != (len(board)-1):
                print(" " + ("---+" *(len(board)-1)) + "---")

        else:
            break

def print_result(winner):
    if winner == 0:
        print("\n It's a tie!")
    else:
        print(f"\n\033[32m Congrats! {winner} has won!\033[0;0m \n")

def tictactoe_game(mode,diff):
    board = init_board()
    player = 'X'
    while True:
        print_board(board)
        if mode == "HUMAN-HUMAN":
            row, col = get_move(board, player)
        elif mode == "HUMAN-AI" and diff == 1:
            if player == 'X':
                row, col = get_move(board, player)
            else:
                time.sleep(1)
                row,col = get_ai_move_easy(board, player)
        elif mode == "HUMAN-AI" and diff == 2:
            if player == 'X':
                row, col = get_move(board, player)
            else:
                time.sleep(1)
                row,col = get_ai_move_medium(board, player)
        elif mode == "HUMAN-AI" and diff == 3:
            if player == 'X':
                row, col = get_move(board, player)
            else:
                time.sleep(1)
                row,col = get_ai_move_hard_hu(board, player)
        elif mode == "AI-HUMAN" and diff == 1:
            if player == 'X':
                time.sleep(1)
                row,col = get_ai_move_easy(board, player)
            else:
                row, col = get_move(board, player)
        elif mode == "AI-HUMAN" and diff == 2:
            if player == 'X':
                time.sleep(1)
                row,col = get_ai_move_medium(board, player)
            else:
                row, col = get_move(board, player)
        elif mode == "AI-HUMAN" and diff == 3:
            if player == 'X':
                time.sleep(1)
                row,col = get_ai_move_hard_ai(board, player)
            else:
                row, col = get_move(board, player)
                
        elif mode == "AI-AI":
            time.sleep(1)
            row,col = get_ai_move_hard_ai(board, player)

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

def difficulty():
    while True:    
        try:
            diff_choice = input("Choose a level: (easy-1, medium-2 ,hard-3)\n")
            if diff_choice == "quit":
                sys.exit()
            diff_choice = int(diff_choice)
            if diff_choice == 1:
                diff = 1
            elif diff_choice == 2:
                diff = 2
            elif diff_choice == 3:
                diff = 3
            else:
                continue
        except ValueError or UnboundLocalError:
            continue
        
        return diff

def main_menu():
    mode_choice = input("Two-player mode: 1, Against AI(player first): 2, Against AI(AI first): 3, Computer against itself: 4\n")
    if mode_choice == "quit":
        sys.exit()
    mode_choice = int(mode_choice)
    diff = difficulty()
    if mode_choice == 1:
        mode = "HUMAN-HUMAN"   
    elif mode_choice == 2:
        mode = "HUMAN-AI"
        diff
    elif mode_choice == 3:
        mode = "AI-HUMAN"
        diff
    elif mode_choice == 4:
        mode = "AI-AI"
    
    tictactoe_game(mode, diff)
    

if __name__ == '__main__':
    main_menu()
