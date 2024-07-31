def coord_volum(*coords):
    if len(coords) < 6:
        raise ValueError("Too few values")

    return {(x,y,z) for x in range(coords[0],coords[1]+1)
                    for y in range(coords[2],coords[3]+1)
                    for z in range(coords[4],coords[5]+1)}


def part1():
    file = open("input","r")
    
    on = set()

    for line in file:
        power, coords = line[:-1].split(" ")
        coords = coords.split(",")
        coord_ranges = []
        for n in coords:
            leftright = n[2:].split("..")
            coord_ranges.append(int(leftright[0]))
            coord_ranges.append(int(leftright[1]))

        if any(abs(n) > 50 for n in coord_ranges):
            continue
        # legg til koordiantene til enten "on" eller "off" gitt at det ikke eksisterer verken.
        
        new = coord_volum(*coord_ranges)
        if power == "on":
            on = on | new
        else:
            on = on - new

        #breakpoint()
    print(len(on))


def part2():
    file = open("input","r")
    
    on = set()

    for line in file:
        power, coords = line[:-1].split(" ")
        coords = coords.split(",")
        coord_ranges = []
        for n in coords:
            leftright = n[2:].split("..")
            coord_ranges.append(int(leftright[0]))
            coord_ranges.append(int(leftright[1]))

        # Simulering fungerer ikke for |n|>50, eller den gjør men PC-dør


    print(len(on))

if __name__ == "__main__":
    print("part 1: ",end="")
    part1()
    print("part 2: ",end="")
    part2()

