# Advent of Code 2021 Day 9 Part 2 solution
# Cyrus Sadeghi

def get_adjacent(idx, x_dimension, y_dimension):
    adjacent = list()

    if idx % y_dimension != 0:
        adjacent.append(idx - 1)
    
    if idx % y_dimension != (y_dimension - 1):
        adjacent.append(idx + 1)

    if idx > (y_dimension - 1):
        adjacent.append(idx - y_dimension)

    if idx < ((x_dimension - 1) * y_dimension - 1):
        adjacent.append(idx + y_dimension)

    return adjacent

def find_basin(grid, idx, x_dimension, y_dimension):
    adjacencies = get_adjacent(idx, x_dimension, y_dimension)
    point = grid[idx]
    basin = set()

    for aidx in adjacencies:
        apoint = grid[aidx]

        if apoint == 9:
            continue

        if apoint > point:
            basin.add(aidx)
            basin = basin | find_basin(grid, aidx, x_dimension, y_dimension)

    return basin

def main():
    in_file = open('input.txt', 'r')
    tot = 0
    grid = list()
    y_dimension = 0
    x_dimension = 0
    basin_lens = list()

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
        adjacent = get_adjacent(idx, x_dimension, y_dimension)

        for aidx in adjacent:
            apoint = grid[aidx]
            if apoint <= point:
                low = False
                break

        if low == False:
            continue

        basin = find_basin(grid, idx, x_dimension, y_dimension)
        basin.add(idx)

        basin_lens.append(len(basin))

    basin_lens = sorted(basin_lens)
    print(basin_lens[-1] * basin_lens[-2] * basin_lens[-3])

main()