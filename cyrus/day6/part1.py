# Advent of Code 2021 Day 6 Part 1 solution
# Cyrus Sadeghi

def main():
    in_file = open('input.txt', 'r')
    fish = list()
    days = 80

    for line in in_file:
        for digit in line.split(','):
            fish.append(int(digit))

    while days != 0:
        old_fish = list()
        new_fish = list()
        idx = 0
        for entry in fish:
            if fish[idx] == 0:
                old_fish.append(6)
                new_fish.append(8)
            else:
                old_fish.append(entry - 1)
            idx = idx + 1

        days = days - 1
        fish = old_fish + new_fish

    print(len(fish))

main()