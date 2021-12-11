# Advent of Code 2021 Day 10 Part 2 solution
# Cyrus Sadeghi

def main():
    in_file = open('input.txt', 'r')
    scores = list()

    for line in in_file:
        opening = list()
        broken = False

        for cmd in line.strip():
            if cmd == '[' or cmd == '(' or cmd == '{' or cmd == '<':
                opening.append(cmd)
            else:
                expected = opening.pop(-1)

                if expected == '[' and cmd != ']':
                    broken = True
                    break

                if expected == '(' and cmd != ')':
                    broken = True
                    break

                if expected == '{' and cmd != '}':
                    broken = True
                    break

                if expected == '<' and cmd != '>':
                    broken = True
                    break

        opening = opening[::-1]

        if len(opening) != 0 and broken == False:
            score = 0

            for cmd in opening:
                value = 0
                if cmd == '(':
                    value = 1
                elif cmd == '[':
                    value = 2
                elif cmd == '{':
                    value = 3
                else:
                    value = 4

                score = score * 5 + value

            scores.append(score)

    scores = sorted(scores)
    print(scores[int(len(scores) / 2)])

main()