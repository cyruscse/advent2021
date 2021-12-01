# Advent of Code 2021 Day 1 Part 2 solution
# Cyrus Sadeghi

def main():
    in_file = open('input.txt', 'r')
    last = list()
    last_tot = -1
    increments = 0
    tot = 0

    for line in in_file:
        if len(last) < 3:
            last.append(int(line))
            continue

        tot = 0

        for val in last:
            tot = tot + val

        last.pop(0)
        last.append(int(line))

        if last_tot != -1 and tot > last_tot:
            increments = increments + 1

        last_tot = tot

    tot = 0

    for val in last:
        tot = tot + val

    if tot > last_tot:
        increments = increments + 1

    print(increments)

main()