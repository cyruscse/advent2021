# Advent of Code 2021 Day 2 Part 1 solution
# Cyrus Sadeghi

def main():
    in_file = open('input.txt', 'r')
    horizontal = 0
    depth = 0

    for line in in_file:
        splitline = line.split()

        if splitline[0] == 'forward':
            horizontal = horizontal + int(splitline[1])
        elif splitline[0] == 'down':
            depth = depth + int(splitline[1])
        elif splitline[0] == 'up':
            depth = depth - int(splitline[1])

    print(horizontal * depth)

main()