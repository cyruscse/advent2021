# Advent of Code 2021 Day 12 Part 1 solution
# Cyrus Sadeghi

import copy

def stislower(st):
    for c in st:
        if c.islower() == False:
            return False

    return True

def invalid(link, path):
    if stislower(link) == False:
        return False

    return (link in path)

def pathfind(links, path):
    if path[-1] == 'end':
        return 1

    paths = 0

    for link in links[path[-1]]:
        if invalid(link, path):
            continue

        npath = copy.deepcopy(path)
        npath.append(link)

        paths = paths + pathfind(links, npath)

    return paths

def main():
    in_file = open('input.txt', 'r')
    links = dict()

    for line in in_file:
        link = line.strip().split('-')
        
        if link[0] not in links.keys():
            links[link[0]] = set()

        if link[1] not in links.keys():
            links[link[1]] = set()

        links[link[0]].add(link[1])
        links[link[1]].add(link[0])

    path = list()
    path.append('start')

    print(pathfind(links, path))

main()