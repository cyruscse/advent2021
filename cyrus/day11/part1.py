# Advent of Code 2021 Day 11 Part 1 solution
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

    for line in in_file:
        for digit in line.strip():
            grid.append(int(digit))
        dimension = len(line.strip())

    turns = 100
    flash_tot = 0

    while turns != 0:
        flashes = set()
        for idx in range(0, len(grid)):
            grid[idx] = grid[idx] + 1
        
        for idx in range(0, len(grid)):
            flashes = flashes | flash_adjacent(grid, idx, dimension, flashes)

        for idx in range(0, len(grid)):
            if grid[idx] > 9:
                grid[idx] = 0
        turns = turns - 1
        flash_tot = flash_tot + len(flashes)

    print(flash_tot)

main()