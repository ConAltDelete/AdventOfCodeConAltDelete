def part1():
    file = open("input","r")

    houses = set()

    current = (0,0)

    houses.add(current)
    
    move = {
            "^":lambda x: (x[0],x[1]+1),
            "v":lambda x: (x[0],x[1]-1),
            ">":lambda x: (x[0]+1,x[1]),
            "<":lambda x: (x[0]-1,x[1])
        }

    while True:
        char = file.read(1)

        if char == "\n":
            break

        current = move[char](current)

        houses.add(current)

    print(len(houses))

def part2():
    file = open("input","r")

    houses = set()

    santa = (0,0)
    robot = (0,0)

    santa_move = False

    houses.add((0,0))
    
    move = {
            "^":lambda x: (x[0],x[1]+1),
            "v":lambda x: (x[0],x[1]-1),
            ">":lambda x: (x[0]+1,x[1]),
            "<":lambda x: (x[0]-1,x[1])
        }

    while True:
        char = file.read(1)

        if char == "\n":
            break
        
        if santa_move:
            santa = move[char](santa)
            houses.add(santa)
        else:
            robot = move[char](robot)
            houses.add(robot)

        santa_move ^= True

    print(len(houses))

part1()
part2()



