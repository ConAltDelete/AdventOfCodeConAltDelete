def count_lit(line):
    return len(line)

def count_mem(line):
    tot = 0

    i = 0

    while i < len(line):
        if line[i] == "\\":
            if line[i+1] == "x":
                i += 3
            else:
                i += 1
        tot += 1
        i += 1

    return tot-2

def count_ext(line):
    tot = 0

    for char in line:
        if char in ["\"","\\"]:
            tot += 2
        else:
            tot += 1

    return tot + 2

def part1():
    file = open("input","r")
    
    total = 0

    for line in file:
        
        literal = count_lit(line)
        memory = count_mem(line)

        total += literal - memory

    print(total)

def part2():
    file = open("input","r")
    
    total = 0

    for line in file:
        
        literal = count_lit(line)
        memory = count_ext(line)

        total += memory - literal

    print(total)

if __name__ == "__main__":
    part1()
    part2()
