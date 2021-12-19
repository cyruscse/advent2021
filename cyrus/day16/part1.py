# Advent of Code 2021 Day 16 Part 1 solution
# Cyrus Sadeghi

def hextobin(hex):
    if hex == '0':
        return "0000"
    elif hex == '1':
        return "0001"
    elif hex == '2':
        return "0010"
    elif hex == '3':
        return "0011"
    elif hex == '4':
        return "0100"
    elif hex == '5':
        return "0101"
    elif hex == '6':
        return "0110"
    elif hex == '7':
        return "0111"
    elif hex == '8':
        return "1000"
    elif hex == "9":
        return "1001"
    elif hex == "A":
        return "1010"
    elif hex == "B":
        return "1011"
    elif hex == "C":
        return "1100"
    elif hex == "D":
        return "1101"
    elif hex == "E":
        return "1110"
    elif hex == "F":
        return "1111"

def bintodec(bin):
    value = 0
    multiplier = len(bin) - 1

    for idx in range(0, len(bin)):
        value = value + int(bin[idx]) * pow(2, multiplier)
        multiplier = multiplier - 1

    return value

def parse_values(idx, code):
    start_idx = idx - 6
    number = ''

    while code[idx] == '1':
        number = number + code[idx + 1 : idx + 5]
        idx = idx + 5

    number = number + code[idx + 1 : idx + 5]
    idx = idx + 5

    return bintodec(number), idx

def parse_version_type(idx, code):
    version = bintodec(code[idx : idx + 3])
    idx = idx + 3

    type = bintodec(code[idx : idx + 3])
    idx = idx + 3

    return idx, version, type

def parse_packet(idx, code):
    idx, version, type = parse_version_type(idx, code)

    if type == 4:
        number, idx = parse_values(idx, code)
    elif code[idx] == '0':
        idx = idx + 1
        remaining_bits = bintodec(code[idx : idx + 15])
        idx = idx + 15

        while remaining_bits != 0:
            oldidx = idx
            idx, dversion = parse_packet(idx, code)
            version = version + dversion
            remaining_bits = remaining_bits - (idx - oldidx)
    elif code[idx] == '1':
        idx = idx + 1
        remaining_pkts = bintodec(code[idx : idx + 11])
        idx = idx + 11

        while remaining_pkts != 0:
            idx, dversion = parse_packet(idx, code)
            version = version + dversion
            remaining_pkts = remaining_pkts - 1

    return idx, version

def main():
    in_file = open('input.txt', 'r')
    code = ''
    idx = 0
    number = 0
    version_sum = 0

    for line in in_file:
        for char in line.strip():
            code = code + hextobin(char)

    idx, version = parse_packet(idx, code)
    print(version)

main()