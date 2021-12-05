# Advent of Code 2021 Day 5 Part 1 solution
# Cyrus Sadeghi

import copy

def determine_points(pair):
    points = set()
    tpoint = copy.deepcopy(pair[0])

    if pair[0][0] == pair[1][0]:
        while tpoint != pair[1]:
            tp = (tpoint[0], tpoint[1])
            points.add(tp)

            if tpoint[1] > pair[1][1]:
                tpoint[1] = tpoint[1] - 1
            else:
                tpoint[1] = tpoint[1] + 1
        points.add((pair[1][0], pair[1][1]))
    elif pair[0][1] == pair[1][1]:
        while tpoint != pair[1]:
            tp = (tpoint[0], tpoint[1])
            points.add(tp)

            if tpoint[0] > pair[1][0]:
                tpoint[0] = tpoint[0] - 1
            else:
                tpoint[0] = tpoint[0] + 1
        points.add((pair[1][0], pair[1][1]))
    else:
        while tpoint != pair[1]:
            tp = (tpoint[0], tpoint[1])
            points.add(tp)

            if tpoint[0] > pair[1][0]:
                tpoint[0] = tpoint[0] - 1

            if tpoint[0] < pair[1][0]:
                tpoint[0] = tpoint[0] + 1

            if tpoint[1] > pair[1][1]:
                tpoint[1] = tpoint[1] - 1

            if tpoint[1] < pair[1][1]:
                tpoint[1] = tpoint[1] + 1
        points.add((pair[1][0], pair[1][1]))

    return points

def main():
    in_file = open('input.txt', 'r')
    pairs = list()
    points = set()
    havetwo = set()

    for line in in_file:
        pair = list()
        for point in line.strip().split(' -> '):
            pair.append(list(map(int, point.split(','))))
        pairs.append(pair)

    twos = 0

    for pair in pairs:
        det_points = determine_points(pair)

        for det_point in det_points:
            if det_point in points and det_point not in havetwo:
                twos = twos + 1
                havetwo.add(det_point)
            else:
                points.add(det_point)

    print(twos)

main()
