# Advent of Code 2021 Day 7 Part 1 solution
# Cyrus Sadeghi

def main():
    in_file = open('input.txt', 'r')
    positions = list()

    for line in in_file:
        for digit in line.split(','):
            positions.append(int(digit))

    scores = dict()

    for fpos in positions:
        score = 0

        for spos in positions:
            score = score + abs(spos - fpos)

        scores[fpos] = score

    print(scores[min(scores, key=scores.get)])

main()
