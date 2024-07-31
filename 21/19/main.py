def part1():
    file = open("input","r")
    
    scanners = dict()
    
    current_scanner = ""

    for line in file:
        line = line[:-1]
        if line == "":
            continue
        if line[:4] == "--- ":
            current_scanner = int(line[12:-4])
            scanners[current_scanner] = []
            continue
        
        x,y,z = [int(a) for a in line.split(",")]

        scanners[current_scanner].append((x,y,z))







def part2():
	file = open("input","r")

if __name__ == "__main__":
	print("part 1: ",end="")
	part1()
	print("part 2: ",end="")
	part2()

