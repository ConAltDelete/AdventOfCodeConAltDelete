def gen_next(p,x0=0,x1=9,y0=0,y1=9,remove_p=False):
    M = [
             (1,-1), (1,0), (1,1),
             (0,-1), (0,0), (0,1),
            (-1,-1),(-1,0),(-1,1)
        ]
    ret = []
    if remove_p:
        M.remove((0,0))
    for m in M:
        new_p = (p[0] + m[0],p[1]+m[1])
        if all([y0 <= new_p[0] <= y1, x0 <= new_p[1] <= x1]):
            ret.append(new_p)

    return ret

def part1():
    file = open("input","r")
    
    dumbo = dict()
    i = 0
    for line in file:
        line = line[:-1]
        for col in enumerate(line):
            dumbo[(i,col[0])] = int(col[1])
        i += 1

    total = 0

    for i in range(100):
        flash = {n:False for n in dumbo}
        for octo in dumbo:
            dumbo[octo] += 1
        overload = list(filter(lambda x: (dumbo[x] > 9) and not(flash[x]),dumbo))
        while len(overload) != 0:
            next_step = dict()
            for octo in overload:
                    flash[octo] = True
                    total += 1
                    N = gen_next(octo)
                    for n in N:
                            dumbo[n] += 1

            overload = list(filter(lambda x: (dumbo[x] > 9) and not(flash[x]),dumbo))
        
        for octo in filter(lambda x: flash[x],flash):
            dumbo[octo] = 0

    print(total)

def part2():
    file = open("input","r")
    
    dumbo = dict()
    i = 0
    for line in file:
        line = line[:-1]
        for col in enumerate(line):
            dumbo[(i,col[0])] = int(col[1])
        i += 1

    total = 0

    flash = {n:False for n in dumbo}

    while any(not(flash[a]) for a in flash):
        flash = {n:False for n in dumbo}
        for octo in dumbo:
            dumbo[octo] += 1
        overload = list(filter(lambda x: (dumbo[x] > 9) and not(flash[x]),dumbo))
        while len(overload) != 0:
            for octo in overload:
                    flash[octo] = True
                    N = gen_next(octo)
                    for n in N:
                            dumbo[n] += 1

            overload = list(filter(lambda x: (dumbo[x] > 9) and not(flash[x]),dumbo))
        
        for octo in filter(lambda x: flash[x],flash):
            dumbo[octo] = 0
        total += 1

    print(total)

def test():
    file = open("test","r")
    dumbo = dict()
    i = 0
    for line in file:
        line = line[:-1]
        for col in enumerate(line):
            dumbo[(i,col[0])] = int(col[1])
        i += 1

    total = 0

    for i in range(100):
        flash = {n:False for n in dumbo}
        for octo in dumbo:
            dumbo[octo] += 1
        overload = list(filter(lambda x: (dumbo[x] > 9) and not(flash[x]),dumbo))
        while len(overload) != 0:
            next_step = dict()
            for octo in overload:
                    flash[octo] = True
                    total += 1
                    N = gen_next(octo)
                    for n in N:
                            dumbo[n] += 1

            overload = list(filter(lambda x: (dumbo[x] > 9) and not(flash[x]),dumbo))
        
        for octo in filter(lambda x: flash[x],flash):
            dumbo[octo] = 0

    print(total)


if __name__ == "__main__":
    print("test: ",end="")
    test()
    print("part 1: ",end="")
    part1()
    print("part 2: ",end="")
    part2()

