# Advent of Code 2021 Day 8 Part 1 solution
# Cyrus Sadeghi

def main():
    in_file = open('input.txt', 'r')
    tot = 0

    for line in in_file:
        idx = 0

        for combos in line.split(' | '):
            if idx == 0:
                idx = idx + 1
                continue
            else:
                outputs = combos.split()

                for output in outputs:
                    if len(output) == 2 or len(output) == 4 or len(output) == 3 or len(output) == 7:
                        tot = tot + 1

    print(tot)

main()
