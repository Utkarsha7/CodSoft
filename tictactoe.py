import math
import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Initializing empty board
        print(" ")
        print("Welcome to Utkarsha's Tic Tac Toe game!!")
        print("The AI plays as 0 and you play as X.")
        print(" ")

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
        print(" ")

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            return True
        return False

    def winner(self, letter):
        for start, step in [(0, 1), (3, 1), (6, 1), (0, 3), (1, 3), (2, 3), (0, 4), (2, 2)]:
            if all(self.board[start+i*step] == letter for i in range(3)):
                return True
        return False

def minimax(game, maximizing):
    if game.winner('X'):
        return -1
    elif game.winner('O'):
        return 1
    elif len(game.available_moves()) == 0:
        return 0

    if maximizing:
        max_score = -math.inf
        for move in game.available_moves():
            game.make_move(move, 'O')
            score = minimax(game, False)
            game.board[move] = ' '  # Undo move
            max_score = max(score, max_score)
        return max_score
    else:
        min_score = math.inf
        for move in game.available_moves():
            game.make_move(move, 'X')
            score = minimax(game, True)
            game.board[move] = ' '  # Undo move
            min_score = min(score, min_score)
        return min_score

def play():
    game = TicTacToe()
    human = 'X'
    ai = 'O'
    current_player = random.choice([human, ai])

    while True:
        game.print_board()
        if current_player == human:
            move = int(input("Enter your move (0-8): "))
            if move not in game.available_moves():
                print("That square is already taken. Try again!!")
                continue
            game.make_move(move, human)
        else:
            best_score = -math.inf
            best_move = None
            for move in game.available_moves():
                game.make_move(move, ai)
                score = minimax(game, False)
                game.board[move] = ' '  # Undo move
                if score > best_score:
                    best_score = score
                    best_move = move
            game.make_move(best_move, ai)

        if game.winner(human):
            game.print_board()
            print("You win!")
            break
        elif game.winner(ai):
            game.print_board()
            print("AI wins!")
            break
        elif len(game.available_moves()) == 0:
            game.print_board()
            print("It's a tie!")
            break

        current_player = human if current_player == ai else ai

if __name__ == '__main__':
    play()
