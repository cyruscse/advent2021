# Advent of Code 2021 Day 17 Part 1 solution
# Cyrus Sadeghi

def coord_in_box(posx, posy, coords):
    if posx >= int(coords[0][0]) and posx <= int(coords[0][1]):
         if posy >= int(coords[1][0]) and posy <= int(coords[1][1]):
            return True

    return False

def overshot(posx, posy, coords):
    if posx > int(coords[0][1]) or posy < int(coords[1][0]):
        return True

    return False

def main():
    in_file = open('input.txt', 'r')

    for line in in_file:
        coords = line.strip().split(': ')[1].split(', ')

        coords[0] = coords[0].split('=')[1].split('..')
        coords[1] = coords[1].split('=')[1].split('..')

    ivolx = 0
    highmark = 0

    while ivolx < abs(int(coords[0][0])):
        ivolx = ivolx + 1
        ivoly = 0

        while ivoly < abs(int(coords[1][0])):
            ivoly = ivoly + 1

            posx = 0
            posy = 0
            volx = ivolx
            voly = ivoly
            local_highmark = 0
            inbox = False

            while overshot(posx, posy, coords) == False:
                posx = posx + volx
                posy = posy + voly

                if posy > local_highmark:
                    local_highmark = posy

                inbox = coord_in_box(posx, posy, coords)

                if inbox == True:
                    break

                if volx > 0:
                    volx = volx - 1

                if volx < 0:
                    volx = volx + 1

                voly = voly - 1

            if inbox == True and local_highmark > highmark:
                highmark = local_highmark

    print(highmark)

main()