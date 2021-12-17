# Advent of Code 2021 Day 14 Part 2 solution
# Cyrus Sadeghi

import copy

def main():
    in_file = open('input.txt', 'r')
    reading_rules = False
    rules = dict()
    pairs = dict()
    spairs = dict()
    base_pairs = dict()

    for line in in_file:
        if len(line.strip()) == 0:
            reading_rules = True
            continue

        if reading_rules == True:
            rules[line.strip().split(' -> ')[0]] = line.strip().split(' -> ')[1]
            pairs[line.strip().split(' -> ')[0]] = 0
        else:
            polymer = line.strip()

    last_letter = polymer[-1]
    base_pairs = copy.deepcopy(pairs)

    for idx in range(0, len(polymer) - 1):
        ppair = polymer[idx] + polymer[idx + 1]
        pairs[ppair] = pairs[ppair] + 1

    turns = 40

    while turns != 0:
        new_pairs = copy.deepcopy(base_pairs)
        new_spairs = copy.deepcopy(base_pairs)

        for pair in pairs.keys():
            fnpair = pair[0] + rules[pair]
            snpair = rules[pair] + pair[1]

            new_pairs[fnpair] = new_pairs[fnpair] + pairs[pair]
            new_pairs[snpair] = new_pairs[snpair] + pairs[pair]
            new_spairs[snpair] = new_spairs[snpair] + pairs[pair]

        pairs = new_pairs
        spairs = new_spairs

        turns = turns - 1

    for pair in pairs:
        pairs[pair] = pairs[pair] - spairs[pair]

    scores = dict()
    scores[last_letter] = 1

    for pair in pairs:
        if pair[0] not in scores.keys():
            scores[pair[0]] = 0

        if pair[1] not in scores.keys():
            scores[pair[1]] = 0

        scores[pair[0]] = scores[pair[0]] + pairs[pair]
        scores[pair[1]] = scores[pair[1]] + pairs[pair]

    inv_scores = {v: k for k, v in scores.items()}
    print(max(set(inv_scores.keys())) - min(set(inv_scores.keys())))

main()