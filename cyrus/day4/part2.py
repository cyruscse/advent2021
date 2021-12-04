# Advent of Code 2021 Day 4 Part 2 solution
# Cyrus Sadeghi

def build_combinations(length):
    combos = list()

    for i in range(0, 5):
        col_combo = set()
        row_combo = set()
        for j in range(0, 5):
            col_combo.add(i + j * length)
            row_combo.add(j + i * length)
        combos.append(col_combo)
        combos.append(row_combo)

    return combos

def main():
    in_file = open('input.txt', 'r')
    draws = list()
    boards = list()
    board = list()
    marks = list()
    marks_vals = list()
    length = 0
    idx = -1

    for line in in_file:
        if ',' in line:
            draws = list(map(int, line.strip().split(',')))
            continue
        if '\n' == line:
            if idx != -1:
                boards.append(board)
                marks.append(set())
                marks_vals.append(set())
            idx = idx + 1
            board = list()
            continue

        board.append(list(map(int, line.split())))
        length = len(board)

    combos = build_combinations(length)

    boards.append(board)
    marks.append(set())
    marks_vals.append(set())
    won_boards = set()

    winning_draw = -1
    winning_board = -1

    for draw in draws:
        idx = 0

        if len(won_boards) == len(boards):
            break

        for board in boards:
            if idx in won_boards:
                idx = idx + 1
                continue

            bidx = 0
            for row in board:
                for digit in row:
                    if digit == draw:
                        marks[idx].add(bidx)
                        marks_vals[idx].add(digit)
                    bidx = bidx + 1

            for combo in combos:
                if len(marks[idx] & combo) == len(combo):
                    won_boards.add(idx)
                    winning_board = idx
                    winning_draw = draw

            idx = idx + 1

    bidx = 0
    losing_sum = 0

    for row in boards[winning_board]:
        for digit in row:
            if digit not in marks_vals[winning_board]:
                losing_sum = losing_sum + digit
            bidx = bidx + 1

    print(losing_sum * winning_draw)

main()