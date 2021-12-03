# Advent of Code 2021 Day 3 Part 1 solution
# Cyrus Sadeghi

def main():
    in_file = open('input.txt', 'r')
    ones = dict()
    zeros = dict()
    lidx = 0
    gamma = list()
    epsilon = list()
    length = 0

    for line in in_file:
        idx = 0
        for digit in line:
            if digit == '\n':
                continue

            if digit == '1':
                if idx not in ones.keys():
                    ones[idx] = 1
                else:
                    ones[idx] = ones[idx] + 1
            elif digit == '0':
                if idx not in zeros.keys():
                    zeros[idx] = 1
                else:
                    zeros[idx] = zeros[idx] + 1
            
            idx = idx + 1
        lidx = lidx + 1
        length = idx

    for idx in range(0, length):
        if ones[idx] > zeros[idx]:
            gamma.append(1)
            epsilon.append(0)
        else:
            epsilon.append(1)
            gamma.append(0)

    gamval = 0
    epsilonval = 0

    for idx in range(0, length):
        gamval = gamval + gamma[idx] * pow(2, (length - 1) - idx)
        epsilonval = epsilonval + epsilon[idx] * pow(2, (length - 1) - idx)

    print(gamval * epsilonval)

main()