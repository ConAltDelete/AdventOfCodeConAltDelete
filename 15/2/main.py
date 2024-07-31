def part1():
    file = open("input","r")
    
    total = 0

    for line in file.readlines():
        dim = [int(a) for a in line.split("x")]
        small = sorted(dim)[:-1]
        total += 2*(dim[0]*dim[1]+dim[1]*dim[2]+dim[2]*dim[0]) + small[0]*small[1]

    print(total)

def part2():
    file = open("input","r")
    
    total = 0

    for line in file.readlines():
        dim = [int(a) for a in line.split("x")]
        small = sorted(dim)[:-1]
        total += 2*(small[0] + small[1]) + dim[0]*dim[1]*dim[2]

    print(total)


part1()
part2()
