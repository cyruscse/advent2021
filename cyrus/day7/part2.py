# Advent of Code 2021 Day 7 Part 2 solution
# Cyrus Sadeghi

def calc_fuel(fpos, spos):
    score = abs(spos - fpos)
    fscore = 0

    for i in range(1, score + 1):
        fscore = fscore + i

    return fscore

def main():
    in_file = open('input.txt', 'r')
    positions = list()
    max_value = 0

    for line in in_file:
        for digit in line.split(','):
            positions.append(int(digit))

            if int(digit) > max_value:
                max_value = int(digit)

    scores = dict()

    for i in range(1, max_value):
        score = 0

        for spos in positions:
            score = score + calc_fuel(spos, i)

        scores[i] = score

    key = min(scores, key=scores.get)
    print(key, scores[key])

main()
