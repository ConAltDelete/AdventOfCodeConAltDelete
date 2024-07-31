def part1():
    file = open("input","r")

    # retning, pos (mutible)

    sea_floor_e = set()
    sea_floor_s = set()
    i = 0

    MAX_X = 0

    for line in file:
        j = 0
        for char in line[:-1]:
            match char:
                case ".":
                    pass
                case ">":
                    sea_floor_e.add((i,j))
                case "v":
                    sea_floor_s.add((i,j))
                case _:
                    raise ValueError("unknown char: " + char)
            j += 1
            if j > MAX_X:
                MAX_X = j
        i += 1

    MAX_Y = i

    # 
    # (">" | "v")
    # 
    # east first, south secound

    moving = True
    n = 0
    while moving:
        current_seafloor = sea_floor_e | sea_floor_s
        n += 1
        new_seafloor_e = set()
        new_seafloor_s = set()
        for e_fish in sea_floor_e:
            if ( new_f :=  (e_fish[0] % MAX_Y, (e_fish[1] + 1) % MAX_X) ) not in current_seafloor:
                new_seafloor_e.add(new_f)
            else:
                new_seafloor_e.add(e_fish)
        
        current_seafloor = set( sea_floor_s | new_seafloor_e )

        for s_fish in sea_floor_s:
            if ( new_f :=  ((s_fish[0] + 1) % MAX_Y, s_fish[1] % MAX_X) ) not in current_seafloor:
                new_seafloor_s.add(new_f)
            else:
                new_seafloor_s.add(s_fish)

        if current_seafloor == (new_seafloor_s | new_seafloor_e):
            moving = False
        sea_floor_s = set(new_seafloor_s)
        sea_floor_e = set(new_seafloor_e)

    print(n)

def part2():
    file = open("input","r")

if __name__ == "__main__":
    print("part 1: ",end="")
    part1()
    print("part 2: ",end="")
    part2()
