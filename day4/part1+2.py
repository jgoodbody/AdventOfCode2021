#!/usr/bin/env python3

with open('input.txt') as f:
    bingo_game = f.read().splitlines()

numbers = list(map(int, bingo_game[0].split(',')))

class BingoBoard:
    def __init__(self, rows):
        for index, row in enumerate(rows):
            rows[index] = list(map(int, row.split()))
        self.board = [row for row in rows]

    def check_bingo(self):
        board = self.board
        # columns
        for i in range(5):
            if all(row[i] == "X" for row in board):
                return True
        # rows
        for row in board:
            if all(x == "X" for x in row):
                return True

    def called_number(self, number):
        if any(number in row for row in self.board):
            for i in range(5):
                 for row in self.board:
                     if row[i] == number:
                         row[i] = "X"

    def uncovered_sum(self):
        sums = []
        for row in self.board:
            sums.append(sum(i for i in row if isinstance(i, int)))
        return sum(sums)

board_list = []

#create boards
for index, line in enumerate(bingo_game):
    if not line:
        board_list.append([BingoBoard(bingo_game[index+1:index+6]), False])

#call numbers part 1
def play_bingo(played_nums, boards):
    for number in played_nums:
        for board in boards:
            board[0].called_number(number)
            if board[0].check_bingo():
                return board[0].uncovered_sum()*number

#print(play_bingo(numbers, board_list))

#part 2
def play_bingo_last(played_nums, boards):
    number_of_boards = len(boards)
    bingo_count = 0
    for number in played_nums:
        for board in boards:
            board[0].called_number(number)
            if board[0].check_bingo():
                if not board[1]:
                    board[1] = True
                    bingo_count += 1
                if bingo_count == number_of_boards:
                    return board[0].uncovered_sum()*number

print(play_bingo_last(numbers, board_list))