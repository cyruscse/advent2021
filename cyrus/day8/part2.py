# Advent of Code 2021 Day 8 Part 2 solution
# Cyrus Sadeghi

def main():
    in_file = open('ginput.txt', 'r')
    allpatterns = list()
    alloutputs = list()
    total = 0

    for line in in_file:
        idx = 0

        patterns = list()
        outputs = list()

        for combos in line.split(' | '):
            if idx == 0:
                patterns = combos.split()
            else:
                outputs = combos.split()
            idx = idx + 1

        allpatterns.append(patterns)
        alloutputs.append(outputs)

    for idx in range(0, len(allpatterns)):
        patterns = allpatterns[idx]
        outputs = alloutputs[idx]

        segment_values = dict()
        segment_values[0] = list()
        segment_values[2] = list()
        segment_values[3] = list()
        segment_values[5] = list()
        segment_values[6] = list()
        segment_values[9] = list()

        for pattern in patterns:
            if len(pattern) == 2:
                segment_values[1] = pattern
            elif len(pattern) == 3:
                segment_values[7] = pattern
            elif len(pattern) == 4:
                segment_values[4] = pattern
            elif len(pattern) == 7:
                segment_values[8] = pattern
            elif len(pattern) == 5:
                segment_values[2].append(pattern)
                segment_values[3].append(pattern)
                segment_values[5].append(pattern)
            elif len(pattern) == 6:
                segment_values[0].append(pattern)
                segment_values[6].append(pattern)
                segment_values[9].append(pattern)

        for segment in segment_values[2]:
            if len(set(segment) & set(segment_values[1])) == 2:
                segment_values[3] = segment
                segment_values[2].remove(segment)
                segment_values[5].remove(segment)

        for segment in segment_values[2]:
            if len(set(segment) & set(segment_values[4])) == 3:
                segment_values[5] = segment
                segment_values[2].remove(segment)
                segment_values[2] = segment_values[2][0]

        for segment in segment_values[0]:
            if len(set(segment) & set(segment_values[1])) == 1:
                segment_values[6] = segment
                segment_values[0].remove(segment)
                segment_values[9].remove(segment)

        for segment in segment_values[0]:
            if len(set(segment) & set(segment_values[4])) == 4:
                segment_values[9] = segment
                segment_values[0].remove(segment)
                segment_values[0] = segment_values[0][0]


        inv_values = {v: k for k, v in segment_values.items()}
        output_val = 0
        multiplier = 1000

        for output in outputs:
            for segment in inv_values.keys():
                if len(segment) != len(output):
                    continue

                if len(set(output) & set(segment)) == len(segment):
                    output_val = output_val + inv_values[segment] * multiplier
                    break

            multiplier = multiplier / 10

        total = total + output_val

    print(int(total))

main()
