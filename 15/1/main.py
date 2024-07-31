def part1():
    file = open("input","r")

    floor = 0
    while True:
        char = file.read(1)
        if char == "(":
            floor += 1
        elif char == ")":
            floor -=1
        else:
            break

    print(floor)

def part2():
    file = open("input","r")

    floor = 0
    pos = 0
    while floor >= 0:
        char = file.read(1)
        pos += 1
        if char == "(":
            floor += 1
        elif char == ")":
            floor -=1
        else:
            break
        

    print(pos)


if __name__ == "__main__":
    part1()
    part2()

