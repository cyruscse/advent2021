# Advent of Code 2021 Day 15 Part 2 solution
# Very slow (15+ minutes) but works
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

def dijkstra(visited, grid, idx, distances, dimension, current_distance, destination):
    while idx != destination:
        adjacencies = get_adjacent(idx, dimension)
        visited.add(idx)

        for adjacent in adjacencies:
            if adjacent in visited:
                continue

            new_distance = grid[adjacent] + current_distance

            if distances[adjacent] == -1 or new_distance < distances[adjacent]:
                distances[adjacent] = new_distance

        next_distance = -1

        for nidx in distances.keys():
            if distances[nidx] == -1 or nidx in visited:
                continue

            if next_distance == -1 or distances[nidx] < next_distance:
                idx = nidx
                next_distance = distances[idx]

        current_distance = distances[idx]

def main():
    grid = list()
    point = 0
    visited = set()
    distances = dict()
    idx = 0
    bigrepeat = 5

    while bigrepeat != 0:
        in_file = open('input.txt', 'r')
        for line in in_file:
            repeat = 5

            while repeat != 0:
                for digit in line.strip():
                    value = int(digit) + (5 - bigrepeat) + (5 - repeat)

                    while value > 9:
                        value = value - 9

                    grid.append(value)
                    distances[idx] = -1
                    idx = idx + 1
                repeat = repeat - 1

        bigrepeat = bigrepeat - 1

    distances[0] = 0
    dimension = len(line.strip() * 5)

    dijkstra(visited, grid, 0, distances, dimension, 0, dimension * dimension - 1)
    print(distances[dimension * dimension - 1])

main()