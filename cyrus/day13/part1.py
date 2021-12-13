# Advent of Code 2021 Day 13 Part 1 solution
# Cyrus Sadeghi

def print_grid(points, dimension):
    for i in range(0, dimension):
        for j in range(0, dimension):
            if (j, i) in points:
                print('x', end='')
            else:
                print(' ', end='')
        print()

def fold_grid_x(points, foldpt):
    newpoints = set()

    for point in points:
        if point[0] > foldpt:
            npoint = (foldpt - (point[0] - foldpt), point[1])
            newpoints.add(npoint)
        else:
            newpoints.add(point)

    return newpoints

def fold_grid_y(points, foldpt):
    newpoints = set()

    for point in points:
        if point[1] > foldpt:
            npoint = (point[0], foldpt - (point[1] - foldpt))
            newpoints.add(npoint)
        else:
            newpoints.add(point)

    return newpoints

def main():
    in_file = open('input.txt', 'r')
    reading_folds = False
    points = set()
    folds = list()
    dimension = 0

    for line in in_file:
        line = line.strip()

        if len(line) == 0:
            reading_folds = True
            continue

        if reading_folds == False:
            point = line.split(',')
            point = ((list(map(int, point))[0]), (list(map(int, point))[1]))

            if point[0] > dimension:
                dimension = point[0]

            if point[1] > dimension:
                dimension = point[1]

            points.add(point)
        else:
            fold = line.split()[2].split('=')
            fold[1] = int(fold[1])
            folds.append(fold)

    fold = folds[0]
    if fold[0] == 'x':
        points = fold_grid_x(points, fold[1])
    else:
        points = fold_grid_y(points, fold[1])

    print(len(points))

main()