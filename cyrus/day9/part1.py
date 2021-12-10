# Advent of Code 2021 Day 9 Part 1 solution
# Cyrus Sadeghi

def get_adjacent(grid, idx, x_dimension, y_dimension):
    adjacent = list()

    if idx % y_dimension != 0:
        adjacent.append(grid[idx - 1])
    
    if idx % y_dimension != (y_dimension - 1):
        adjacent.append(grid[idx + 1])

    if idx > (y_dimension - 1):
        adjacent.append(grid[idx - y_dimension])

    if idx < ((x_dimension - 1) * y_dimension - 1):
        adjacent.append(grid[idx + y_dimension])

    return adjacent

def main():
    in_file = open('input.txt', 'r')
    tot = 0
    grid = list()
    y_dimension = 0
    x_dimension = 0
    total = 0

    for line in in_file:
        y_dimension = len(line.strip())

        for digit in line:
            if digit == '\n':
                continue

            grid.append(int(digit))

        x_dimension = x_dimension + 1

    for idx in range(0, len(grid)):
        point = grid[idx]
        low = True

        for apoint in get_adjacent(grid, idx, x_dimension, y_dimension):
            if apoint <= point:
                low = False
                break

        if low == True:
            total = total + point + 1

    print(total)

main()