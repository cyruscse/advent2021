# Advent of Code 2021 Day 14 Part 1 solution
# Cyrus Sadeghi

def main():
    in_file = open('input.txt', 'r')
    reading_rules = False
    rules = dict()
    polymer = ''

    for line in in_file:
        if len(line.strip()) == 0:
            reading_rules = True
            continue

        if reading_rules == True:
            rules[line.strip().split(' -> ')[0]] = line.strip().split(' -> ')[1]
        else:
            polymer = line.strip()

    turns = 10

    while turns != 0:
        new_polymer = ""

        for idx in range(0, len(polymer) - 1):
            pair = polymer[idx] + polymer[idx + 1]

            new_polymer = new_polymer + pair[0]
            new_polymer = new_polymer + rules[pair]

        new_polymer = new_polymer + polymer[-1]

        polymer = new_polymer
        turns = turns - 1

    score = dict()

    for letter in polymer:
        if letter not in score.keys():
            score[letter] = 0

        score[letter] = score[letter] + 1

    inv_scores = {v: k for k, v in score.items()}

    print(max(set(inv_scores.keys())) - min(set(inv_scores.keys())))

main()