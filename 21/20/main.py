from io import FileIO


def point_filter(p, algo, image, r=0):
    matrix = [
            ( 1,-1),( 1, 0),( 1, 1),
            ( 0,-1),( 0, 0),( 0, 1),
            (-1,-1),(-1, 0),(-1, 1)
            ]
    coords = list()

    for m in matrix:
        coords.append((p[0] + m[0],p[1] + m[1]))

    index = 0
    if 0 in algo and (1<<9 - 1) not in algo:
        default = r % 2 == 0
    else:
        default = False

    for p in coords:
        if p in image:
            index += 1
        elif default:
            index += 1
        index <<= 1

    if index in algo:
        return True
    else:
        return False

def part1(file_str: str):
    # limit = [290,9582] <- er imellom der
    file = open(file_str,"r")
    algorithm = {i[0] for i in enumerate(file.readline().strip()) if i[1] == "#"}

    file.readline()

    pix = set()

    i = 0
    j = 0

    for line in file:
        j = 0
        for char in line[:-1]:
            if char == "#":
                pix.add((i,j))
            j += 1
        i += 1

    offset = 1
    
    for r in range(2):
        new_img = set()
        current = [-2*offset,-2*offset]

        while current != [i + 2*offset,0]:
            if point_filter(tuple(current),algorithm,pix, r = r):
                new_img.add(tuple(current))

            current[1] += 1
            if current[1] > j + 2*offset - 1:
                current[1] = -2*offset
                current[0] += 1

        pix = set(new_img)

        offset += 1

    print(len(pix))
    
def part2():
    file = open("input","r")

if __name__ == "__main__":
    print("part 1: ",end="")
    part1("test")
    print("part 2: ",end="")
    part2()

