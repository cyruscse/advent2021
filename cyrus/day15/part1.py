# Advent of Code 2021 Day 15 Part 1 solution
# Cyrus Sadeghi

import sys

def get_adjacent(idx, dimension):
    adjacent = list()

    if idx % dimension != 0:
        adjacent.append(idx - 1)
    
    if idx % dimension != (dimension - 1):
        adjacent.append(idx + 1)

    if idx > (dimension - 1):
        adjacent.append(idx - dimension)

    if idx <= ((dimension - 1) * dimension - 1):
        adjacent.append(idx + dimension)

    return adjacent

def test_adjacent(idx, dimension, grid, visited, distances, current_distance, destination, depth):
    adjacencies = get_adjacent(idx, dimension)
    visited.add(idx)

    for adjacent in adjacencies:
        if adjacent in visited:
            continue

        new_distance = grid[adjacent] + current_distance

        if distances[adjacent] == -1 or new_distance < distances[adjacent]:
            distances[adjacent] = new_distance

    if idx == destination:
        return

    next_distance = -1
    next_idx = -1

    for nidx in distances.keys():
        if distances[nidx] == -1 or nidx in visited:
            continue

        if next_distance == -1 or distances[nidx] < next_distance:
            next_distance = distances[nidx]
            next_idx = nidx

    test_adjacent(next_idx, dimension, grid, visited, distances, distances[next_idx], destination, depth + 1)

def main():
    in_file = open('input.txt', 'r')
    grid = list()
    point = 0
    visited = set()
    distance = dict()
    idx = 0

    # lol
    sys.setrecursionlimit(15000)

    for line in in_file:
        for digit in line.strip():
            grid.append(int(digit))
            distance[idx] = -1
            idx = idx + 1

    distance[0] = 0
    dimension = len(line.strip())

    test_adjacent(0, dimension, grid, visited, distance, 0, dimension * dimension - 1, 0)

    print(distance[dimension * dimension - 1])

main()