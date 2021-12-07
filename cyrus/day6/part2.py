# Advent of Code 2021 Day 6 Part 2 solution
# Cyrus Sadeghi

def main():
    in_file = open('input.txt', 'r')
    ages = dict()
    days = 256
    tot_fish = 0

    for line in in_file:
        for digit in line.split(','):
            if int(digit) not in ages.keys():
                ages[int(digit)] = 1
            else:
                ages[int(digit)] = ages[int(digit)] + 1

    while days != 0:
        new_ages = dict()
        for age in ages.keys():
            if age != 0:
                if (age - 1) in new_ages.keys():
                    new_ages[age - 1] = new_ages[age - 1] + ages[age]
                else:
                    new_ages[age - 1] = ages[age]
            else:
                if 6 not in new_ages.keys():
                    new_ages[6] = ages[age]
                else:
                    new_ages[6] = new_ages[6] + ages[age]

                new_ages[8] = ages[age]

        ages = new_ages
        days = days - 1

    for age in ages.keys():
        tot_fish = tot_fish + ages[age]

    print(tot_fish)

main()