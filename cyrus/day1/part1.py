# Advent of Code 2021 Day 1 Part 1 solution
# Cyrus Sadeghi

def main():
    in_file = open('input.txt', 'r')
    last = -1
    increments = 0

    for line in in_file:
        if last == -1:
            last = int(line)
            continue

        if int(line) > last:
            increments = increments + 1

        last = int(line)

    print(increments)

main()