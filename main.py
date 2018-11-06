import random

def display_board(board):
    # to print a new screen between moves
    print('\n'*100)

    # set up our grid
    print('  ' + '| ' + '|')
    print(' ' + board[7] + '|' + board[8] + '|' + board[9])
    print('--|-|--')
    print(' ' + board[4] + '|' + board[5] + '|' + board[6])
    print('--|-|--')
    print(' ' + board[1] + '|' + board[2] + '|' + board[3])
    print('  ' + '| ' + '|')


def player_input():
    marker = ''
    print("Welcome to my tic-tac-toe game!")
    # assign markers

    while marker != 'X' and marker != 'O':
        marker = input("Please pick a marker 'X' or 'O'").upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
        (board[4] == mark and board[5] == mark and board[6] == mark) or   # across the middle
        (board[1] == mark and board[2] == mark and board[3] == mark) or   # across the bottom
        (board[1] == mark and board[4] == mark and board[7] == mark) or   # down left side
        (board[2] == mark and board[5] == mark and board[8] == mark) or  # down middle side
        (board[3] == mark and board[6] == mark and board[9] == mark) or  # down right side
        (board[1] == mark and board[5] == mark and board[9] == mark) or  # diagonal
        (board[3] == mark and board[5] == mark and board[7] == mark))  # diagonal


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range (1, 10):
        if space_check(board, i):
            return False

    return True


def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next spot 1-9'))

    return position


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


# lets start the game!
while True:
    main_board = [' '] * 10
    display_board(main_board)
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Players ready to start? Enter Yes.').lower()
    if play_game == 'yes':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # player 1's turn
            display_board(main_board)
            position = player_choice(main_board)
            place_marker(main_board,player1_marker, position)

            if win_check(main_board, player1_marker):
                display_board(main_board)
                print('Game Over, Player 1 won!')
                game_on = False
            else:
                if full_board_check(main_board):
                    display_board(main_board)
                    print('Game is a draw!')
                    break
                else:
                    turn = 'Player 2'
        else:
            # player 2's turn
            display_board(main_board)
            position = player_choice(main_board)
            place_marker(main_board, player2_marker, position)

            if win_check(main_board, player2_marker):
                display_board(main_board)
                print('Game Over, Player 2 won!')
                game_on = False
            else:
                if full_board_check(main_board):
                    display_board(main_board)
                    print('Game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
