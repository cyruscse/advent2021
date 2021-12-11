# Advent of Code 2021 Day 10 Part 1 solution
# Cyrus Sadeghi

def main():
    in_file = open('input.txt', 'r')
    score = 0

    for line in in_file:
        opening = list()
        bad_char = ''

        for cmd in line.strip():
            if cmd == '[' or cmd == '(' or cmd == '{' or cmd == '<':
                opening.append(cmd)
            else:
                expected = opening.pop(-1)

                if expected == '[' and cmd != ']':
                    bad_char = cmd
                    break

                if expected == '(' and cmd != ')':
                    bad_char = cmd
                    break

                if expected == '{' and cmd != '}':
                    bad_char = cmd
                    break

                if expected == '<' and cmd != '>':
                    bad_char = cmd
                    break

        if bad_char == ')':
            score = score + 3
        elif bad_char == ']':
            score = score + 57
        elif bad_char == '}':
            score = score + 1197
        elif bad_char == '>':
            score = score + 25137

    print(score)

main()