# Advent of Code 2021 Day 18 Part 2 solution
# Cyrus Sadeghi

import copy

def reduce_digits(digits):
    reduced = False

    while reduced == False:
        idx = 0
        newdigits = copy.deepcopy(digits)
        lexplode = False
        exploded = False

        for digit in digits:
            if digit[1] > 4:
                # Explode Left
                if idx == 0:
                    newdigits[0] = (0, digit[1] - 1)
                else:
                    newdigits[idx] = (digits[idx][0] + digits[idx - 1][0], digits[idx - 1][1])
                    newdigits.pop(idx - 1)
                    lexplode = True

                idx = idx + 1

                # Explode Right
                if idx == len(digits) - 1:
                    newdigits[-1] = (0, digit[1] - 1)
                else:
                    newdigits[idx] = (digits[idx + 1][0] + digits[idx][0], digits[idx + 1][1])

                    if lexplode == False:
                        newdigits.pop(idx + 1)
                    else:
                        newdigits[idx - 1] = (0, digit[1] - 1)

                digits = newdigits
                exploded = True
                break
            else:
                idx = idx + 1

        if exploded == False:
            idx = 0

            for digit in digits:
                if digit[0] > 9:
                    if digit[0] % 2 == 0:
                        val1 = int(digit[0] / 2)
                        val2 = val1
                    else:
                        val1 = int(digit[0] / 2)
                        val2 = val1 + 1

                    newdigits[idx] = (val1, digit[1] + 1)
                    newdigits.insert(idx + 1, (val2, digit[1] + 1))

                    digits = newdigits
                    break

                idx = idx + 1

        reduced = True

        for digit in digits:
            if digit[0] > 9 or digit[1] > 4:
                reduced = False
                break

    return digits

def calculate_magnitude(digits):
    reduced = False

    while reduced == False:
        reduced = True
        idx = 0
        newdigits = copy.deepcopy(digits)

        for digit in digits:
            if digits[idx][1] == digits[idx + 1][1]:
                newdigits[idx] = (digits[idx][0] * 3 + digits[idx + 1][0] * 2, digits[idx][1] - 1)
                newdigits.pop(idx + 1)
                reduced = False
                digits = newdigits
                break
            idx = idx + 1

        if len(digits) == 1:
            return(digits[0][0])

def main():
    in_file = open('input.txt', 'r')
    depth = 0
    all_digits = list()
    largestmag = 0

    for line in in_file:
        digits = list()
        for char in line.strip():
            if char == '[':
                depth = depth + 1
            elif char == ']':
                depth = depth - 1
            elif char.isdigit():
                digits.append((int(char), depth))

        all_digits.append(digits)

    for fdigits in all_digits:
        for sdigits in all_digits:
            if fdigits == sdigits:
                continue

            digits = copy.deepcopy(fdigits)
            next_digits = copy.deepcopy(sdigits)
            idx = 0

            for digit in digits:
                digits[idx] = (digit[0], digit[1] + 1)
                idx = idx + 1

            for ndigit in next_digits:
                digits.append((ndigit[0], ndigit[1] + 1))

            digits = reduce_digits(digits)
            magnitude = calculate_magnitude(digits)

            if magnitude > largestmag:
                largestmag = magnitude

    print(largestmag)

main()