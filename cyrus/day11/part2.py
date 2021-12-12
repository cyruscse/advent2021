# Advent of Code 2021 Day 11 Part 2 solution
# Cyrus Sadeghi

def get_adjacent(idx, dimension):
    adjacent = list()

    if idx % dimension != 0:
        adjacent.append(idx - 1)

        if idx > (dimension - 1):
            adjacent.append(idx - 1 - dimension)

        if idx < (dimension * (dimension - 1)):
            adjacent.append(idx - 1 + dimension)
    
    if idx % dimension != (dimension - 1):
        adjacent.append(idx + 1)

        if idx > (dimension - 1):
            adjacent.append(idx + 1 - dimension)

        if idx < (dimension * (dimension - 1)):
            adjacent.append(idx + 1 + dimension)

    if idx > (dimension - 1):
        adjacent.append(idx - dimension)

    if idx < (dimension * (dimension - 1)):
        adjacent.append(idx + dimension)

    return adjacent

def flash_adjacent(grid, idx, dimension, flashed):
    if grid[idx] < 10:
        return set()

    if idx in flashed:
        return set()

    flashed.add(idx)

    for aidx in get_adjacent(idx, dimension):
        grid[aidx] = grid[aidx] + 1
        flashed = flashed | flash_adjacent(grid, aidx, dimension, flashed)

    return flashed

def main():
    in_file = open('input.txt', 'r')
    grid = list()
    dimension = 0
    turn = 1

    for line in in_file:
        for digit in line.strip():
            grid.append(int(digit))
        dimension = len(line.strip())

    while True:
        flashes = set()
        for idx in range(0, len(grid)):
            grid[idx] = grid[idx] + 1
        
        for idx in range(0, len(grid)):
            flashes = flashes | flash_adjacent(grid, idx, dimension, flashes)

        for idx in range(0, len(grid)):
            if grid[idx] > 9:
                grid[idx] = 0

        last_val = grid[0]
        done = True

        for idx in range(1, len(grid)):
            if grid[idx] != last_val:
                done = False
                break

        if done:
            break

        turn = turn + 1

    print(turn)

main()