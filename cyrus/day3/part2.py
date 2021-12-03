# Advent of Code 2021 Day 3 Part 2 solution
# Cyrus Sadeghi

import copy

def main():
    in_file = open('input.txt', 'r')
    sequences = list()
    sequence_len = 0

    for line in in_file:        
        sequences.append(line.strip())
        sequence_len = len(line.strip())

    bkp_sequences = copy.deepcopy(sequences)

    idx = 0
    num_indicies = len(sequences)

    while num_indicies != 1:
        ones = 0
        zeros = 0

        for sequence in sequences:
            if sequence[idx] == '0':
                zeros = zeros + 1
            else:
                ones = ones + 1

        new_sequences = list()

        if ones >= zeros:
            for sequence in sequences:
                if sequence[idx] == '1':
                    new_sequences.append(sequence)
        else:
            for sequence in sequences:
                if sequence[idx] == '0':
                    new_sequences.append(sequence)

        sequences = new_sequences
        num_indicies = len(sequences)
        idx = idx + 1

    oxygen = sequences[0]
    sequences = bkp_sequences

    # lazy copy paste :)
    idx = 0
    num_indicies = len(sequences)

    while num_indicies != 1:
        ones = 0
        zeros = 0

        for sequence in sequences:
            if sequence[idx] == '0':
                zeros = zeros + 1
            else:
                ones = ones + 1

        new_sequences = list()

        if ones >= zeros:
            for sequence in sequences:
                if sequence[idx] == '0':
                    new_sequences.append(sequence)
        else:
            for sequence in sequences:
                if sequence[idx] == '1':
                    new_sequences.append(sequence)

        sequences = new_sequences
        num_indicies = len(sequences)
        idx = idx + 1

    carbon = sequences[0]

    oxyval = 0
    carval = 0

    for idx in range(0, sequence_len):
        oxyval = oxyval + int(oxygen[idx]) * pow(2, (sequence_len - 1) - idx)
        carval = carval + int(carbon[idx]) * pow(2, (sequence_len - 1) - idx)

    print(oxyval * carval)

main()